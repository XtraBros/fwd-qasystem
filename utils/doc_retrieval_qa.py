from langchain.callbacks.manager import (
    CallbackManagerForChainRun,
)
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering.stuff_prompt import PROMPT_SELECTOR
from typing import Any, Dict, Optional
from langchain.load.dump import dumpd

class DocRetrievalQA( RetrievalQA):
    search_size: int = 30

    def _stream(
        self,
        inputs: Dict[str, Any],
        run_manager: Optional[CallbackManagerForChainRun] = None,
    ) -> Dict[str, Any]:

        _run_manager = run_manager or CallbackManagerForChainRun.get_noop_manager()
        question = inputs[self.input_key]
        prev_res = inputs['prev_response'] if 'prev_response' in inputs else ''
        start_idx = inputs['start_idx'] if 'start_idx' in inputs else 0
        alternative_questions = inputs['alt_questions'] if 'alt_questions' in inputs else []
        if not alternative_questions and self.newq_llm_chain:
            alt_inputs ={'question': inputs['query']}
            alternative_questions = [self.newq_llm_chain(alt_inputs)['stream_iter']]

        self.retriever.search_kwargs['k'] = start_idx + self.search_size

        docs = self._get_docs(question, run_manager=_run_manager)

        docs = docs[start_idx:start_idx+self.search_size]

        # dict_keys(['input_documents', 'question', 'used_sources', 'output_text'])
        outputs = self.combine_documents_chain.stream(
            {'input_documents': docs, 'question': question, 'prev_response': prev_res}, callbacks=_run_manager.get_child(),
            return_only_outputs=True
        )
        final_outputs = {}
        final_outputs[self.output_key] = outputs[self.combine_documents_chain.output_key]
        final_outputs['source_documents'] = outputs['docs']
        final_outputs['alt_questions'] = alternative_questions
        final_outputs['start_idx'] = start_idx + len(outputs['docs'])
        return final_outputs