import threading
from flask import Flask
from typing import List
from fastapi import FastAPI

########################################## Global variables ##########################################
# app = FastAPI()
app = Flask(__name__)
source_docs = None

# Define global llm container and llm object
global_llm_container = None
global_llm_obj = None

active_threads: List[threading.Thread] = []