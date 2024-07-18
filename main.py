########################################################################################
WEBSITES = ['https://bot-docs.cloudfabrix.io/beginners_guide/dashboards/',]

DOCUMENTS_DIR = './documents'
VECTOR_DB_DIR = './vector_db'
MODEL_DIR = './models'
NUM_RELEVANT_DOCS = 3
EMBEDDING_MODEL = 'paraphrase-MiniLM-L3-v2'
LLM = 'Meta-Llama-3-8B-Instruct'

QUERY = ['How to create a Dashboard?',
         'What are dashboard filters?',
         'How to configure a pie chart?'
        ]
########################################################################################


########################################################################################
# Imports
import os
import sys
import time
from tqdm import tqdm
########################################################################################


########################################################################################
# Scrape Websites
print('\n*****************')
print('SCRAPING WEBSITES')
print('*****************')
from src import scraper
scraper.scrape(WEBSITES, DOCUMENTS_DIR, None)
########################################################################################


########################################################################################
# Pre-Process Document Content
print('\n*********************')
print('Cleaning Website Data')
print('*********************')
from src import data_cleaner
data_cleaner.clean(DOCUMENTS_DIR)
########################################################################################


########################################################################################
# Chucking Documents
print('\n*************')
print('Chucking Data')
print('*************')
from src import chunker
chunks = chunker.chunk(DOCUMENTS_DIR)
print(f'Total Number of Chunks is {len(chunks)}')
########################################################################################


########################################################################################
# Initializing Embedding Model
print('\n**********************')
print('Loading Embedding Model')
print('***********************')

from langchain_huggingface import HuggingFaceEmbeddings

embedding_model_path = os.path.join(MODEL_DIR, EMBEDDING_MODEL)

if not os.path.exists(embedding_model_path):
    print(f"\n{embedding_model_path} DOES NOT EXIST.")
    sys.exit(0)
else:
    embedding_model = HuggingFaceEmbeddings(model_name=embedding_model_path)
    print(f'Loaded Embedding Model {EMBEDDING_MODEL} from {embedding_model_path}')
########################################################################################


########################################################################################
# Creating Vector Database
print('\n***********************')
print('Creating Vector Database')
print('************************')

from src import vector_db_builder

vector_db = vector_db_builder.build(chunks, VECTOR_DB_DIR, embedding_model, EMBEDDING_MODEL)

retriever = vector_db.as_retriever(search_type="similarity", search_kwargs={"k":NUM_RELEVANT_DOCS})

if isinstance(QUERY, str):
    relevant_docs = retriever.invoke(QUERY)

    print('\nRelevant Documents:')
    for i, doc in enumerate(relevant_docs):
        print(f'Document {i}:\n\n{doc.page_content}\n')
        if doc.metadata:
            print(f"Source: {doc.metadata.get('Header 1', 'None')} -> {doc.metadata.get('Header 2', 'None')} -> {doc.metadata.get('Header 3', 'None')} -> {doc.metadata.get('Header 4', 'None')}\n")

    times = []
    for _ in tqdm(range(1000)):
        start = time.time()
        retriever.invoke(QUERY)
        end = time.time()

        times.append(end - start)

    print(f'\nAverage Retreival Runtime: {(sum(times)/len(times))*1000} MilliSeconds')

    sys.exit(0)
########################################################################################


########################################################################################
# Creating Vector Database
print('\n***********************')
print('Creating Vector Database')
print('************************')

vector_db = vector_db_builder.build(chunks, VECTOR_DB_DIR, embedding_model, EMBEDDING_MODEL)

retriever = vector_db.as_retriever(search_type="similarity", search_kwargs={"k":NUM_RELEVANT_DOCS})

if isinstance(QUERY, str):
    relevant_docs = retriever.invoke(QUERY)

    print('\nRelevant Documents:')
    for i, doc in enumerate(relevant_docs):
        print(f'Document {i}:\n\n{doc.page_content}\n')
        if doc.metadata:
            print(f"Source: {doc.metadata.get('Header 1', 'None')} -> {doc.metadata.get('Header 2', 'None')} -> {doc.metadata.get('Header 3', 'None')} -> {doc.metadata.get('Header 4', 'None')}\n")

    times = []
    for _ in tqdm(range(1000)):
        start = time.time()
        retriever.invoke(QUERY)
        end = time.time()

        times.append(end - start)

    print(f'\nAverage Retreival Runtime: {(sum(times)/len(times))*1000} MilliSeconds')
########################################################################################


########################################################################################
# Initializing LLM
print('\n**********')
print('Loading LLM')
print('***********')

from langchain_community.llms import VLLM

llm_path = os.path.join(MODEL_DIR, LLM)

if not os.path.exists(llm_path):
    print(f"\n{llm_path} DOES NOT EXIST.")
    sys.exit(0)
else:
    llm = VLLM(
        model=llm_path,
        max_new_tokens=150,
        temperature=0.2,
        verbose=False
    )
    print(f'Loaded LLM {LLM} from {llm_path}')
########################################################################################


########################################################################################
# QA Chat
print('\n*******')
print('Q&A Chat')
print('********')

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from src import qa_rag_chain

rag_chain = qa_rag_chain.build_chain(llm, retriever)

store = {}
def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)

start = time.time()
for query in QUERY:

    print(f"\nUser: {query}")

    result = conversational_rag_chain.invoke(
                    {"input": query},
                    config={
                        "configurable": {"session_id": "abc123"}
                    },
                )["answer"]

    print(result)

end = time.time()

print(f"\nRuntime: {(end-start)} Seconds")
########################################################################################