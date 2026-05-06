# 🧠 Deep Research Agent

A **Deep Agent-powered research assistant** that autonomously plans, searches, analyzes, and synthesizes information into structured reports using tool-calling and sub-agent capabilities.

---

## 🚀 Overview

This project demonstrates how to build an **autonomous research agent** using the LangChain Deep Agents framework.

The agent:

* Breaks down complex queries into actionable steps
* Searches the web using Tavily
* Manages intermediate context via internal tooling
* Synthesizes results into a polished response

---

## 🏗️ Architecture

```
User Query
    ↓
Deep Agent (Planner)
    ↓
Tool Calls (internet_search)
    ↓
Context Management (internal FS tools)
    ↓
Sub-agents (if needed)
    ↓
Final Report Generation
```

---

## 🛠️ Tech Stack

* **Agent Framework**: LangChain Deep Agents
* **LLM Provider**: Google Gemini
* **Search API**: Tavily
* **Language**: Python

---

## 📦 Installation

```bash
pip install deepagents tavily-python python-dotenv
```

## ⚙️ How It Works

### 1. Planning

The agent uses an internal planner (`write_todos`) to decompose the task.

### 2. Research

Calls the `internet_search` tool to gather external data.

### 3. Context Management

Uses file system tools (`write_file`, `read_file`) to handle large intermediate data.

### 4. Delegation

Spawns sub-agents for complex subtasks when required.

### 5. Synthesis

Combines all findings into a coherent final report.

---

## ⭐ Acknowledgements

* LangChain for Deep Agents
* Tavily for search capabilities
* Google for Gemini models

---
