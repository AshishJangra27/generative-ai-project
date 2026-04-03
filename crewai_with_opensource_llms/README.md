# Local Agentic AI with CrewAI & Gemma 4

This project demonstrates how to set up and run **intelligent, multi-agent systems locally** in Google Colab using **CrewAI** and **Ollama** with the **Gemma 4** LLM. By leveraging local LLMs, this project showcases private, cost-effective, and powerful automation without relying on external APIs.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/146PSRswOMfximNELDM6lHq5Mj4-Cj9PZ?usp=sharing)

By utilizing **Agentic AI** with local models, this project enables the creation of specialized AI "crews" that collaborate on complex tasks like coding and content writing directly within a hosted notebook environment.

---

## What This Project Covers

- **Environment Setup**: Installing `crewai`, `litellm`, and configuring the environment for local execution.
- **Local LLM Integration**: Installing **Ollama**, starting the background server, and pulling the `gemma4:e4b` model within Colab.
- **Agent Definition**: Creating specialized AI agents with distinct roles, goals, and backstories powered by Gemma 4.
- **Task Orchestration**: Assigning tasks to agents to collaboratively achieve objectives.
- **Multi-Agent Crews**: Assembling agents into functional Crews for complex problem-solving.
- **Input Handling & File I/O**: Passing dynamic inputs to tasks and programmatically saving agent outputs to local files.

---

## Tech Stack Used

- **LLM**: Google Gemma 4 (`gemma4:e4b` running via Ollama)
- **Framework**: CrewAI (for Agentic Workflows)
- **Orchestration**: Ollama & LiteLLM (for local LLM connectivity)
- **Language**: Python
- **Environment**: Google Colab

---

## Project Workflow

<img src="https://raw.githubusercontent.com/AshishJangra27/generative-ai-project/main/crewai_with_opensource_llms/src/img_1.png" alt="CrewAI + Gemma 4 Local Workflow Diagram" width="100%">

### 1. Environment & Ollama Setup
The system installs necessary Python libraries and dependencies (`zstd`). It then downloads and installs Ollama, starts the Ollama server in the background using Python's `subprocess`, and pulls the specific `gemma4:e4b` model.

### 2. Example 1: The Coding Crew
- **Agent**: Python Coder (specialized in clean, efficient utility scripts).
- **Task**: Write a recursive Python function to calculate the nth Fibonacci number, including usage examples.
- **Execution**: The crew runs the task, Gemma 4 generates the code snippet, and the result is printed.

### 3. Example 2: The Content Writing Crew
- **Agent**: Professional Content Writer (experienced in engaging, optimized articles).
- **Task**: Write a comprehensive, well-structured article based on a dynamically provided topic placeholder (`{topic}`).
- **Execution & Saving**: The crew runs with a specific input topic (e.g., "Life expectancy in India from 1500s to 2026"). Gemma 4 generates the article, and the system programmatically saves the final output to a Markdown (`.md`) file.

---

## Key Features

- **Fully Local Execution**: No data leaves the Colab environment, ensuring maximum privacy.
- **Specialized Agent Personas**: Different roles defined for coders, writers, and historians.
- **Automated workflows**: Tasks are defined and managed within a standard CrewAI pipeline.
- **Dynamic Inputs**: Tasks use placeholders to accept new topics at runtime.
- **Persistence**: Final agent outputs are saved directly to the Colab workspace for downloading.

---

## Learning Outcome

By completing this project, you will understand:
- How to manage **local LLMs** in a cloud environment using Ollama.
- How to configure **CrewAI** to point to a local server instead of proprietary APIs.
- Basics of building **AI agents** with distinct personas using small, efficient models.
- Workflow for executing **Crews** and handling dynamically generated text and code outputs.

This forms the foundation for building advanced, private tools like:
- Local Code Copilots
- Private Document Drafting Systems
- On-Premise Data Analysis Agents

---

## 👤 Credits

Made with ❤️ by [Ashish Jangra](https://github.com/AshishJangra27)  
Powered by **CrewAI**, **Ollama**, and **Google Gemma 4**
