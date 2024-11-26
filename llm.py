import logging, os
from langchain.chains import RetrievalQA
from constants import EMBEDDING_MODEL_NAME, CHINESE_EMBEDDING_MODEL_NAME, LLM_MODEL_PATH, MODEL_BASENAME, LLAMA_LLM_IN_OPENAI_API_IP, LAW_DB_PATH, LAW_SEARCH_K, USER_DB_SEARCH_K

from langchain_openai import ChatOpenAI
from langchain_community.llms import LlamaCpp
from langchain_community.embeddings import HuggingFaceEmbeddings, HuggingFaceInstructEmbeddings, OpenAIEmbeddings, HuggingFaceBgeEmbeddings
from langchain_chroma import Chroma
from langchain.chains.query_constructor.schema import AttributeInfo
from chromadb.config import Settings

from chains.prompts import LAW_PROMPT_WITH_SOURCE, LAW_PROMPT_NO_SOURCE, LAW_DOC_PROMPT, LAW_REFINE_PROMPT, LAW_NEWQ_PROMPT
from utils.doc_retrieval_qa import DocRetrievalQA

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(message)s", level=logging.INFO)

class LLM_Obj:
    def __init__(self, name, db, retriever, llm, qa, iqa, qa_no_source, embeddings):
        self.name = name
        self.db = db
        self.retriever = retriever
        self.llm = llm
        self.qa = qa
        self.iqa = iqa
        self.qa_no_source = qa_no_source
        self.embeddings = embeddings

    def __repr__(self):
        return f"<llm_obj(name={self.name})>"

class LLM_Container:
    def __init__(self):
        self.llm_obj_dict = {}

    def add_llm_obj(self, llm_obj):
        self.llm_obj_dict[llm_obj.name] = llm_obj

    def get_llm_obj(self, name):
        return self.llm_obj_dict.get(name)

    def remove_llm_obj(self, name):
        if name in self.llm_obj_dict:
            del self.llm_obj_dict[name]
        else:
            print(f"No llm_obj found with name: {name}")

def create_llm(callback_manager, device_type, return_source_documents, multi_source=False, model="llama"):
    if model == "llama":
        model_basename = MODEL_BASENAME
        model_full_path = f"{LLM_MODEL_PATH}/{model_basename}"
        if os.path.isfile(model_full_path):
            model_id = model_basename.split('.')[0]
            logging.info(f"Loading Model: {model_id}, on device: {device_type}")
            logging.info("This action may take some time!")

            # If the model is quantized in GGML or GGUF method, Llama.cpp is required
            if ".ggml" in model_basename or ".gguf" in model_basename:
                logging.info("Using Llamacpp for GGML/GGUF quantized models")
                model_path = f"{LLM_MODEL_PATH}/{model_basename}"

                # Common model settings
                kwargs = {
                    "model_path": model_path,
                    "n_ctx": 2048,
                    "n_batch": 512,
                    "max_tokens": 2048,
                    "verbose": False,
                    "callback_manager": callback_manager,
                    "streaming": True,
                    "use_mmap": True,
                    "use_mlock": True,
                    "temperature": 0.1,
                    "top_p": 0.95,
                    "top_k": 3,
                    "repeat_penalty": 1.3,
                    "n_threads": 4,
                    "echo": False
                }

                if device_type.lower() == "cpu":
                    kwargs["n_gpu_layers"] = 0
                elif device_type.lower() == "mps" or device_type.lower() == "cuda":
                    kwargs["n_gpu_layers"] = 100
                else:
                    logging.error("Device type is not supported yet. Exiting...")
                    return None
                if "70b" in model_basename.lower():
                    kwargs["n_gqa"] = 8
                llm = LlamaCpp(**kwargs)
            else:
                logging.error("Model formats not in ggml or gguf are not supported yet. Exiting...")
                llm = None
        else:
            logging.error("For local deployment, the basename should be explicitly defined and provided")
            llm = None
    elif model == "gpt":
        llm_args = {
            "model": "gpt-3.5-turbo",
            "temperature": 0.5,
            "max_tokens": 1024,
            "callback_manager": callback_manager,
            "n": 1,
            "openai_api_key": os.environ.get("OPENAI_API_KEY"),
            "streaming": True,
            "verbose": True,
        }
        if os.environ.get("LLM_OPENAI_MODEL", "None") != "None":
            llm_args["model"] = os.environ.get("LLM_OPENAI_MODEL")
        else:
            del llm_args["model"]
        if os.environ.get("LLM_OPENAI_API_BASE", "None") != "None":
            llm_args["openai_api_base"] = os.environ.get("LLM_OPENAI_API_BASE")
        llm = ChatOpenAI(**llm_args)
    else:
        logging.error(f"Unsupported mode: {model}")
        return None, None, None, None, None

    if os.environ.get("LLM_EMBEDDINGS_DEVICE", "None") != "None":
        embeddings_device = os.environ.get("LLM_EMBEDDINGS_DEVICE")
    else:
        embeddings_device = "cpu"
    embeddings = HuggingFaceInstructEmbeddings(
       model_name = 'hkunlp/instructor-xl',
       model_kwargs = {'device': embeddings_device},
    )

    db = Chroma(
        persist_directory=LAW_DB_PATH,
        embedding_function=embeddings,
        client_settings=Settings(anonymized_telemetry=False, is_persistent=True)
    )

    retriever = db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": LAW_SEARCH_K}
    )

    qa = DocRetrievalQA.from_args(llm=llm, retriever=retriever, prompt=LAW_PROMPT_WITH_SOURCE, document_prompt=LAW_DOC_PROMPT, search_size=LAW_SEARCH_K,
                                                  new_question=True, newq_prompt=LAW_NEWQ_PROMPT)
    iqa  = DocRetrievalQA.from_args(llm=llm, retriever=retriever,
                                                  prompt=LAW_PROMPT_WITH_SOURCE, document_prompt=LAW_DOC_PROMPT, search_size=LAW_SEARCH_K,
                                                  interactive=True, refine_prompt=LAW_REFINE_PROMPT,
                                                  new_question=True, newq_prompt=LAW_NEWQ_PROMPT)
    qa_no_source = DocRetrievalQA.from_args(llm=llm, retriever=retriever, prompt=LAW_PROMPT_NO_SOURCE, document_prompt=LAW_DOC_PROMPT)

    return db, retriever, llm, qa, iqa, qa_no_source, embeddings