# 🤖 Level 8 — Agentic AI

<p align="center">
  <img src="https://img.shields.io/badge/Duration-2--3%20Months%20(Ongoing)-fb923c?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Difficulty-Expert-ef4444?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Prerequisites-Level%207-4ade80?style=for-the-badge" />
</p>

> **The frontier of AI.** Build autonomous AI agents that reason, plan, use tools, and collaborate to solve complex problems.

---

## 📚 What You'll Learn

| Module | Topics | Folder |
|---|---|---|
| 🧩 Agents Foundation | Architecture, tool use, memory systems, planning, multi-agent systems | [`01_AI_Agents_Foundation/`](01_AI_Agents_Foundation/) |
| 🌐 Use Cases | Domain-specific agent applications (DS, FinTech, Healthcare, Education) | [`02_Agent_Use_Cases/`](02_Agent_Use_Cases/) |
| 🔌 MCP | Model Context Protocol — connecting LLMs to tools universally | [`03_MCP/`](03_MCP/) |
| ⚙️ Frameworks | LangGraph, CrewAI, AutoGen, OpenAI Swarm, Semantic Kernel | [`04_Agent_Frameworks/`](04_Agent_Frameworks/) |
| 🔄 Workflows | n8n, trigger types, AI agent nodes, sub-workflows | [`05_Workflow_Automation/`](05_Workflow_Automation/) |
| 🚀 Deployment | FastAPI, Docker, observability, guardrails, human-in-the-loop | [`06_Agent_Deployment/`](06_Agent_Deployment/) |

---

## 🎯 Learning Objectives

- [ ] Design and build AI agents with tool use and memory
- [ ] Implement multi-agent systems with role-based collaboration
- [ ] Build MCP servers to connect LLMs with data sources
- [ ] Create production agent workflows with LangGraph
- [ ] Automate business processes with n8n + AI agents
- [ ] Deploy agents with proper observability and safety guardrails

---

## 🛠️ Key Tools

```python
from langgraph.graph import StateGraph
from crewai import Agent, Task, Crew
import n8n  # visual workflow automation
from langfuse import Langfuse  # observability
from fastapi import FastAPI
```

---

## 🏆 Flagship Project Idea

> **AI Career Counselor for Rural Youth** — Build a multi-agent system: one agent for skill gap analysis, one for job searching (web tool), one for resume review. Orchestrate with LangGraph, deploy via n8n webhooks, monitor in Langfuse.

---

## 🎉 Congratulations!

If you've reached Level 8, you've completed a comprehensive journey from zero to Data Scientist. But remember — **learning never stops.** The field evolves rapidly. Stay curious, keep building, keep contributing.