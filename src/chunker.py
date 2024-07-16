import os
from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter

def chunk(documents_dir):
    # Splitting Based on Markdown Tags
    docs = []

    text_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3"), ("###", "Header 4")],
        strip_headers=False
    )

    for document in os.listdir(os.path.join(documents_dir, 'processed')):
        
        with open(os.path.join(documents_dir, 'processed', document), 'r') as f:
            text = f.read()

        docs.extend(text_splitter.split_text(text))

    # Breaking Big Markdown chunks into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500, 
        chunk_overlap=200
    )

    docs = text_splitter.split_documents(docs)

    return docs