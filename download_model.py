cache_dir = './cache'
token = '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'

import os
import argparse
from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer

parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str)
parser.add_argument('--type', type=str, default='llm', choices=['llm', 'embed'])
args = parser.parse_args()

save_path = os.path.join('models', args.model.split('/')[-1])

if not os.path.exists(save_path):

    if args.type == 'llm':
        model = AutoModelForCausalLM.from_pretrained(args.model, trust_remote_code=True, cache_dir=cache_dir, token=token)
        tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True, cache_dir=cache_dir, token=token)
    
        model.save_pretrained(save_path)
        tokenizer.save_pretrained(save_path)

    elif args.type == 'embed':
        model = SentenceTransformer(args.model, trust_remote_code=True, cache_folder=cache_dir, token=token)
        model.save(save_path)

    print("Model saved to {}".format(save_path))
    
else:
    print("Model already exists at {}".format(save_path))