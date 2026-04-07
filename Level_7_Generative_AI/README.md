# ✨ Level 7 — Generative AI

<p align="center">
  <img src="https://img.shields.io/badge/Duration-3--4%20Months-4ade80?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Difficulty-Advanced-ef4444?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Prerequisites-Level%206-818cf8?style=for-the-badge" />
</p>

> **The GenAI revolution is here.** Learn to harness, customize, and build with Large Language Models.

---

## 📚 What You'll Learn

| Module | Topics | Folder |
|---|---|---|
| 🧬 LLM Foundation | Architecture, training process, RLHF, model families, multimodal | [`01_LLM_Foundation/`](01_LLM_Foundation/) |
| 💬 Prompt Engineering | Zero/few-shot, CoT, ReAct, structured output, DSPy | [`02_Prompt_Engineering/`](02_Prompt_Engineering/) |
| 🔌 LLM Integration | OpenAI API, LangChain, LlamaIndex, Hugging Face, vector databases | [`03_LLM_Integration/`](03_LLM_Integration/) |
| 📚 RAG | Architecture, document processing, embedding models, retrieval strategies | [`04_RAG/`](04_RAG/) |
| 🎯 Fine-Tuning | LoRA, QLoRA, SFT, DPO, training frameworks | [`05_Fine_Tuning/`](05_Fine_Tuning/) |
| 🔧 Build SLM | Tokenizer, GPT architecture in PyTorch, training loop, text generation | [`06_Build_SLM/`](06_Build_SLM/) |

---

## 🎯 Learning Objectives

- [ ] Understand how LLMs work under the hood
- [ ] Master prompt engineering techniques (CoT, ReAct, few-shot)
- [ ] Build RAG applications with vector databases
- [ ] Fine-tune open-source models with LoRA/QLoRA
- [ ] Build a small language model from scratch with PyTorch
- [ ] Deploy LLM-powered applications

---

## 🛠️ Key Libraries

```python
from openai import OpenAI
from langchain_core.runnables import RunnablePassthrough
from llama_index.core import VectorStoreIndex
import chromadb
from transformers import AutoModelForCausalLM
```

---

## ➡️ Next Level

After mastering GenAI, move to **[Level 8 — Agentic AI](../Level_8_Agentic_AI/)**.