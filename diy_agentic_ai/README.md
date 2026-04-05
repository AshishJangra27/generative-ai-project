# AI Task Automation Agent (Gemini Function Calling Simulation)

This project demonstrates how to build an **AI-powered task automation agent** using the **Google Gemini API**. It showcases how an LLM can break down complex instructions into structured subtasks and execute them programmatically.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1mZOYsKMPFaaszyaYBGrEvD6jMz5MbqOr?usp=sharing)

By combining **prompt engineering** with **dynamic code execution**, this project simulates how modern AI agents can plan and perform real-world tasks step by step.

---

## What This Project Covers

- **Task Decomposition**: Breaking a complex instruction into smaller executable steps  
- **Structured Output Generation**: Using LLM to return tasks in dictionary format  
- **Function Mapping**: Mapping AI-generated tasks to actual Python functions  
- **Dynamic Execution**: Executing tasks using `eval()`  
- **Agent-like Behavior**: Simulating planning + execution loop  

---

## Tech Stack Used

- **LLM**: Google Gemini (gemini-2.5-flash)  
- **Language**: Python  
- **Core Concepts**: Prompt Engineering, Agentic AI  
- **Environment**: Google Colab  

---

## Project Workflow

### 1. Define Tools
Custom Python functions are defined:
- Create folder  
- Create file  
- Write content into file  

### 2. Prompt Design
A structured prompt is created to guide the LLM:
- Convert user instruction into task list  
- Return output strictly in list of dictionaries  

### 3. Task Generation
Gemini generates a sequence of tasks and reasoning steps.

### 4. Output Parsing
The response is cleaned and converted into a Python list using `ast.literal_eval`.

### 5. Task Execution
Each generated task is executed dynamically using `eval()`.

### 6. Logging
Thinking steps are printed to track execution flow.

---

## Key Features

- **Agent-like Planning**: LLM decides what steps to perform  
- **Executable Outputs**: Tasks are directly runnable Python commands  
- **Flexible Design**: Easily extendable with more tools  
- **Automation Ready**: Can automate file system operations  

---

## Learning Outcome

By completing this project, you will understand:

- How to design prompts for structured outputs  
- How LLMs simulate agentic workflows  
- How to connect LLM outputs with real function execution  
- Basics of building autonomous AI agents  

This forms the foundation for building:

- AI task automation systems  
- Developer copilots  
- Workflow automation agents  
- Autonomous assistants  

---

## Credits

Made by [Ashish Jangra](https://github.com/AshishJangra27)  
Powered by Google Gemini API  
