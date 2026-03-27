# AI Resume Analyzer & Interviewer (CrewAI & Gemini)

This project demonstrates how to build an **Automated Resume Analysis and Interview Preparation System** using **CrewAI** and the **Google Gemini API**. It showcases a multi-agent system where specialized AI agents collaborate to evaluate a candidate and generate tailored interview questions.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1w_iB_f8vp_8MNBgxYPFWMhyOxrridIGL?usp=sharing)

By using **Agentic AI**, this project automates the manual work of HR analysts and technical interviewers, providing deep insights and structured preparation in seconds.

---

## What This Project Covers

- **Multi-Agent Orchestration**: Using CrewAI to manage specialized agents with distinct roles.
- **PDF Resume Parsing**: Automatically extracting text from uploaded resume files using `pypdf`.
- **Candidate Evaluation**: Identifying strengths, weaknesses, and calculating a skill score.
- **Smart Interview Prep**: Generating personalized technical, project, and HR questions based on the resume.
- **Gradio Interface**: Building a user-friendly web UI to upload resumes and view AI results.

---

## Tech Stack Used

- **LLM**: Google Gemini (gemini-1.5-flash)
- **Framework**: CrewAI (for Agentic Workflows)
- **Orchestration**: LangChain (langchain-google-genai)
- **UI**: Gradio
- **Language**: Python
- **Environment**: Google Colab

---

## Project Workflow

### 1. Resume Parsing
The system uses `pypdf` to read the uploaded PDF file and convert the resume content into raw text for the AI agents to process.

### 2. The Resume Analyzer Agent
- **Role**: Expert HR Analyst.
- **Task**: Analyzes the candidate's profile, identifies core strengths, and highlights areas for improvement.
- **Output**: A comprehensive evaluation report including a skill score (0-10).

### 3. The Interview Question Generator Agent
- **Role**: Senior Technical Interviewer.
- **Task**: Uses the analysis from the first agent to create a customized interview plan.
- **Output**: A structured list of 5 Technical, 3 Project-based, and 3 HR questions specific to the candidate.

---

## Key Features

- **Automated Workflows**: Tasks are passed seamlessly from the Analyzer to the Interviewer.
- **Context-Aware Responses**: Questions are derived from actual resume data, not generic templates.
- **Interactive UI**: Upload your resume through a Gradio interface and get instant feedback.
- **Efficiency**: Reduces hours of manual screening to just a few seconds of AI processing.

---

## Learning Outcome

By completing this project, you will understand:
- How to build **multi-agent systems** using CrewAI.
- How to integrate **Google Gemini** into agentic workflows.
- Basics of **Prompt Engineering** for specialized agent personas.
- How to deploy a simple **AI-powered web application** using Gradio.

This forms the foundation for building advanced tools like:
- Automated HR Screening Bots
- AI Career Coaches
- Enterprise Talent Acquisition Platforms

---

## 👤 Credits

Made with ❤️ by [Ashish Jangra](https://github.com/AshishJangra27)  
Powered by **CrewAI** and **Google Gemini API**
