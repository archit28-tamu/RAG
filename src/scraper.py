import os
from langchain_community.document_loaders import FireCrawlLoader

def scrape(websites, documents_dir, api_key):
    for url in websites:
        raw_document_path = os.path.join(documents_dir, 'raw', url.split('/')[-2]) + '.md'

        if not os.path.exists(raw_document_path):
            loader = FireCrawlLoader( 
                url=url,
                api_key=api_key, 
                mode="scrape",
                params= {
                    'pageOptions': {
                        'onlyMainContent': True
                        }
                    }
            )
            docs = loader.load()

            content = docs[0].page_content
            
            os.makedirs(os.path.join(documents_dir, 'raw'), exist_ok=True)
            with open(raw_document_path, 'w') as f:
                f.write(content)
            
            print(f"Scraped {url} and Saved to {raw_document_path}")
        
        else:
            print(f'{url} already scraped to {raw_document_path}')