from langchain_community.llms import VLLM
import os

MODEL_DIR = 'models'
LLM = 'gemma-2b'

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