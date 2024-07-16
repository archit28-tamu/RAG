import os
from langchain_chroma import Chroma

def build(docs, vector_db_dir, embedding_model, embedding_model_name):
    os.makedirs(vector_db_dir, exist_ok=True)
    vector_db_path = os.path.join(vector_db_dir, embedding_model_name.split('/')[-1].split('.')[0])

    if not os.path.exists(vector_db_path):
        db = Chroma.from_documents(
            documents=docs, 
            embedding=embedding_model, 
            persist_directory=vector_db_path
        )
        print(f'Vector Database Created at {vector_db_path}')
    
    else:
        db = Chroma(
            persist_directory=vector_db_path,
            embedding_function=embedding_model
        )
        print(f'Vector Database already exists at {vector_db_path}')

    return db