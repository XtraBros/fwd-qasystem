import os
from chromadb.config import Settings
from langchain_community.document_loaders import CSVLoader, UnstructuredPDFLoader, TextLoader, UnstructuredExcelLoader, Docx2txtLoader
from utils.custom_loaders import CustomDocumentLoader

################ Server related constants ################
# Get shared data root path
SHARED_DATA_ROOT_PATH = os.getenv("SHARED_DATA_ROOT_PATH")
# Path of local Llama-2-70B full-precision model
LLAMA_LLM_70B_MODEL_PATH = f"{SHARED_DATA_ROOT_PATH}/models/Llama-2/full/llama-2-70b-chat-pytorch"
# Address of local Llama-2-70B full-precision model running locally
LLAMA_LLM_IN_OPENAI_API_IP = "http://localhost:8123/v1"
# Supported device types: "cpu", "mps", "cuda"
DEVICE_TYPE = "cuda"
# Server's root directory
SERVER_ROOT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "server")
# Root path of all types of resources
SERVER_RESOURCE_ROOT_PATH = f"{SERVER_ROOT_PATH}/resources"
# Local LLM models path
LLM_MODEL_PATH = f"{SERVER_RESOURCE_ROOT_PATH}/llm_models"
# Define the folder for all documents
DOCS_PATH = f"{SERVER_RESOURCE_ROOT_PATH}/source_document"
# Define the folder for current target document (testing purpose)
SINGLE_DOC_PATH = f"{SERVER_RESOURCE_ROOT_PATH}/single_source_document"
# Define the folder for storing the data when persisting by DuckDB
LOCAL_DB_PATH = f"{SERVER_ROOT_PATH}/DB"
# Local knowledge base for legalExpert
LAW_DB_PATH = f"{SHARED_DATA_ROOT_PATH}/vector-db/LawDB-SSO-524acts"
# Users' own data root path
USER_DATA_ROOT_PATH = f"{SHARED_DATA_ROOT_PATH}/user-data"
# The analysis output path
OUTPUT_PATH = f"{SERVER_ROOT_PATH}/output"
# Relational DB path
META_INFO_DB_PATH = f"{SERVER_RESOURCE_ROOT_PATH}/meta_db"
# Can be changed to a specific number
INGEST_THREADS = os.cpu_count() or 8
# Max queue size for buffering the tokens from LLM
MAX_TOKEN_QUEUE_SIZE = 8192
# Return the source documents for QA chain
RETURN_SOURCE_DOCS = True
# Vector DB maximum number of returned chunks in MyLib
USER_DB_SEARCH_K = 6
# Vector DB maximum number of returned chunks in LegalExpert
LAW_SEARCH_K = 30
# Define the Chroma settings
CHROMA_SETTINGS = Settings(
    chroma_db_impl="duckdb+parquet", is_persistent=True, persist_directory=LOCAL_DB_PATH, anonymized_telemetry=False
)
DOCUMENT_MAP = {
    ".txt": TextLoader,
    ".md": TextLoader,
    ".py": TextLoader,
    ".pdf": CustomDocumentLoader,
    ".csv": CSVLoader,
    ".xls": UnstructuredExcelLoader,
    ".xlxs": UnstructuredExcelLoader,
    ".docx": CustomDocumentLoader,
    ".doc": Docx2txtLoader,
}

# English embedding model
EMBEDDING_MODEL_NAME = "hkunlp/instructor-xl"

# Chinese embedding model
CHINESE_EMBEDDING_MODEL_NAME = "BAAI/bge-large-zh-v1.5"

########################################## GGML models ##########################################
# MODEL_BASENAME = "llama-2-7b-chat.ggmlv3.q8_0.bin"
# MODEL_BASENAME = "llama-2-13b-chat.ggmlv3.q8_0.bin"
# MODEL_BASENAME = "llama-2-70b-chat.ggmlv3.q5_K_M.bin"
# MODEL_BASENAME = "llama-2-70b-chat.ggmlv3.q8_0.bin"

########################################## GGUF models ##########################################
MODEL_BASENAME = "llama-2-7b-chat.q8_0.gguf"
# MODEL_BASENAME = "llama-2-13b-chat.q8_0.gguf"
# MODEL_BASENAME = "llama-2-70b-chat.q6_k.gguf"
# MODEL_BASENAME = "llama-2-70b-chat.q8_0.gguf"