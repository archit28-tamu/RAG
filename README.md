## Resources
- [Local LLM](https://python.langchain.com/v0.2/docs/how_to/local_llms/)
- [Local RAG](https://python.langchain.com/v0.2/docs/tutorials/local_rag/)
- [Conversational RAG](https://python.langchain.com/v0.2/docs/tutorials/qa_chat_history/)

## Model Client
```
srun --nodes=1 --ntasks-per-node=8 --mem=32G --time=03:00:00 --pty bash -i
ml GCC/13.2.0
```

# Runtimes

## Embedding Models
| Model                                 | Avg Time (millisec) |
|---------------------------------------|---------------------|
| all-mpnet-base-v2                     | 94.50               |
| paraphrase-multilingual-MiniLM-L12-v2 | 33.90               |
| all-MiniLM-L6-v2                      | 17.50               |
| LaBSE                                 | 91.50               |
| distiluse-base-multilingual-cased-v1  | 55.72               |
| stsb-distilbert-base                  | 48.37               |
| all-MiniLM-L12-v2                     | 30.28               |
| all-distilroberta-v1                  | 56.26               |
| multi-qa-mpnet-base-dot-v1            | 91.20               |
| multi-qa-distilbert-cos-v1            | 49.13               |
| multi-qa-MiniLM-L6-cos-v1             | 16.02               |
| paraphrase-multilingual-mpnet-base-v2 | 108.86              |
| paraphrase-albert-small-v2            | 36.49               |
| paraphrase-MiniLM-L3-v2               | 9.17                |
| distiluse-base-multilingual-cased-v2  | 56.03               |

## LLMs
| Model                                 | Time for first prompt | Answer Quality | # of Parameters (B) |
|---------------------------------------|-----------------------|----------------|---------------------|
| Mistral                               | 8 min                 | Good           | 7                   |
| Meta-Llama-3-8B-Instruct              | 6.21 min              | Good           | 8                   |
| gpt2                                  | 6 sec                 | Bad            | 1.5                 |
| Qwen2-0.5B                            | 10 sec                | Bad            | 0.5                 |
| DialoGPT-medium                       | 12 sec                | Bad            | 0.147               |
| distilgpt2                            | 3 sec                 | Bad            | 0.08                |
| pythia-160m                           | 8 sec                 | Bad            | 0.16                |
| pythia-410m                           | 23 sec                | Bad            | 0.41                |
| bloom-560m                            | 23 sec                | Bad            | 0.56                |

## System Configurations for CPU Only
| Model     | RAM | # of Cores | KV_cache | Time for first prompt | # of CPU blocks |
|-----------|-----|------------|----------|-----------------------|-----------------|
| gemma-2b  | 32  | 8          | 4        | 2.15                  | 14563           |
| gemma-2b  | 32  | 8          | 5        | 2.09                  | 18240           |
| gemma-2b  | 32  | 8          | 8        | 2.16                  | 29127           |
| gemma-2b  | 32  | 32         | 4        | 2.12                  | 14563           |
| gemma-2b  | 32  | 32         | 8        | 2.08                  | 29127           |
| gemma-2b  | 32  | 32         | 10       | 2.13                  | 36408           |
| gemma-2b  | 32  | 32         | 16       | Killed                | 58254           |
| gemma-2b  | 64  | 8          | 4        | 2.09                  | 14563           |
| gemma-2b  | 64  | 32         | 4        | 2.11                  | 14563           |
| gemma-2b  | 64  | 32         | 8        | 2.07                  | 29127           |
| gemma-2b  | 64  | 32         | 10       | 2.07                  | 36408           |
| gemma-2b  | 128 | 32         | 4        | 2.12                  | 14563           |
| gemma-2b  | 128 | 32         | 10       | 2.08                  | 36408           |
| gemma-2b  | 128 | 32         | 12       | 2.08                  | 43690           |
| gemma-2b  | 128 | 32         | 16       | 2.08                  | 58254           |
| gemma-2b  | 128 | 32         | 20       | 2.08                  | 72817           |
| gemma-2b  | 128 | 32         | 24       | 2.07                  | 87381           |
| gemma-2b  | 128 | 32         | 30       | 2.16                  | 109226          |
