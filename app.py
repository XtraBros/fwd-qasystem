from pages.routes import pages
from api.routes import api
import json
import os, logging
from openai import OpenAI

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from globalvars import app, global_llm_container, global_llm_obj, source_docs, active_threads
from llm import LLM_Container, LLM_Obj, create_llm

# Global objects
CONFIG_FILE = 'config.json'
with open(CONFIG_FILE, 'r') as config_file:
    config_file = json.load(config_file)

openai_agent = OpenAI(
    api_key=config_file["OPENAI_API_KEY"]
)
openai_model = config_file["GPT_MODEL"]

################################## Instantiate global LLM objects ##################################
def launch_llm(model_type, device_type, return_source_documents=False, multi_source=False):
    """
    Instantiate global LLM related objects inlcuding LLM, DB, QA chain, and Retriever

    Parameters:
    model_type: llama or gpt
    device_type: cpu, mps or cuda
    """
    global_llm_container = LLM_Container()

    # Callbacks support token-wise streaming
    callback_manager = CallbackManager([])

    if model_type == "llama":
        global_llm_obj = LLM_Obj("llama", *create_llm(callback_manager=callback_manager, device_type=device_type, multi_source=False, model="llama", return_source_documents=return_source_documents))
    elif model_type == "gpt":
        global_llm_obj = LLM_Obj("gpt", *create_llm(callback_manager=callback_manager, device_type=device_type, multi_source=False, model="gpt", return_source_documents=return_source_documents))
    else:
        logging.error(f"The model type {model_type} is not supported yet.")
        pass
    global_llm_container.add_llm_obj(global_llm_obj)

# Register blueprints
app.register_blueprint(pages)
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)