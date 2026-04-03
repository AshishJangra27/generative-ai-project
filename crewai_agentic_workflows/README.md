# Multi-Agent AI with CrewAI: A Comprehensive Demonstration

This project serves as a comprehensive deep dive into **CrewAI**, a powerful framework for orchestrating autonomous AI agents to collaborate on complex objectives. It provides practical demonstrations through several distinct "Crews," showcasing agent design, task definition, crew formation, and the integration of diverse external tools.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1iH0kViqut95JwbfB2gLCtNyWqaWxC6vu?usp=sharing)

By using **Agentic AI**, this notebook automates diverse workflows ranging from friendly tutoring to advanced software engineering, reducing complex tasks to simple, automated executions.

---

## What This Project Covers

- **Agent Persona Design**: Defining specific roles, goals, and backstories for diverse AI agents.
- **Dynamic Task Orchestration**: Assigning tasks with reusable inputs (`{topic}`) for automated execution.
- **External Tool Integration**: Connecting agents to the real world using the `crewai_tools` library.
- **Workflow Logging**: Utilizing verbose output to trace agent thought processes.
- **Output Management**: Programmatically saving generated content (e.g., saving articles as `.md` files).
- **Usage Metrics**: Tracking token consumption for cost and performance monitoring.

---

## Tech Stack Used

- **LLM**: Google Gemini (e.g., gemini-2.5-flash)
- **Framework**: CrewAI (for Agentic Workflows)
- **Tools**:
    * `ScrapeWebsiteTool`: For web scraping and information extraction.
    * `FileReadTool`: For reading local files (e.g., code).
    * `FileWriterTool`: For saving outputs to local files.
    * `PGSearchTool`: For querying PostgreSQL databases (concept demonstration).
    * `DallETool`: For image generation via DALL-E (concept demonstration).
    * `SerperDevTool`: For real-time Google search functionality.
- **Orchestration**: LiteLLM (implicit via CrewAI for LLM connectivity).
- **Language**: Python
- **Environment**: Google Colab

---

## Project Workflow (General CrewAI Lifecycle)

While multiple specific projects are included, they all follow a standardized standard workflow for building agentic systems.

### 1. Environment & API Setup
The system installs necessary libraries (`crewai`, `crewai_tools`) and configures necessary API keys (e.g., GEMINI_API_KEY, SERPER_API_KEY) in the Colab environment.

### 2. Define Agent Personas
Agents are instantiated with distinct capabilities. For example, in the Code Refactoring Crew:
- **Agent**: Principal Software Engineer (focused on clean code and PEP 8).
- **Tools**: Assigned `FileReadTool` and `FileWriterTool`.

### 3. Define Tasks
Tasks are created outlining specific descriptions and expected outputs, linking variables (like `{topic}`) for kickoff. For example, in the Content Writer Crew:
- **Task**: Write a 500-800 word comprehensive and engaging article on a given topic.

### 4. Execute the Crew
Crews are assembled with the defined agents and tasks. Verbose logging is usually enabled to watch the agents "think." The kickoff method initiates execution, passing in variables if necessary. Result objects are returned containing raw output and usage metrics.

---

## Key Features Demonstrations Included

- **Topic Explainer**: A Friendly Tutor agent that uses simple analogies to explain complex topics.
- **Content Writer**: A Professional Content Writer agent that generates well-structured articles and saves them to `.md` files.
- **Web Scraper**: A Web Researcher agent that scrapes specific URLs (e.g., Wikipedia) and summarizes key information.
- **Code Refactorer**: A Software Engineer agent that reads existing Python code, applies PEP 8 standards, docstrings, and type hints, and saves the refined code as a new file.
- **Database Analyst (Concept)**: Demonstration of querying a PostgreSQL database using `PGSearchTool`.
- **Digital Artist (Concept)**: Demonstration of generating images from text using `DallETool`.
- **Market Researcher (Concept)**: Demonstration of performing real-time internet searches using `SerperDevTool`.

---

## Learning Outcome

By completing this project, you will understand:
- How to manage **CrewAI installation and tool configuration** in a cloud environment.
- How to define **specialized agents** with distinct personas using Google Gemini.
- Standard workflows for **Task design, Crew assembly, and dynamic execution**.
- How to trace agent logic using **verbose output** and monitor token usage.
- Practical methods for **integrating vision, web search, database querying, and file I/O tools** into agent workflows.

This forms the foundation for building advanced, automated enterprise agents such as:
- Autonomous Content & Research Pipelines
- AI Code Auditors and DevOps Agents
- Autonomous Data Analysts and BI Reporters

---

## 👤 Credits

Made with ❤️ by [Ashish Jangra](https://github.com/AshishJangra27)  
Powered by **CrewAI** and **Google Gemini API**
