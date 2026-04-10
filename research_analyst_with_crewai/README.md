# CrewAI for Data Analysts: Comparative Multi-Agent Study

This project demonstrates how different **CrewAI configurations** impact the quality of research and summarization tasks. It provides a side-by-side comparison of simple, tool-assisted, and multi-agent systems using a real-world topic.

The objective is to understand how **agent capability, tool usage, and collaboration** influence output depth and accuracy.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1QZgPpdXiZw-HzrTU4cmxJK7r07IALqI0?usp=sharing)

---

## 📌 Project Objective

- Compare **three CrewAI setups** for the same problem  
- Analyze differences in:
  - Output quality  
  - Depth of insights  
  - Use of external data  
- Showcase evolution from **basic AI → tool-augmented AI → collaborative AI**

---

## 🧠 Problem Statement

All systems work on:

> **“Changes in life expectancy in India from 1600s to 2026”**

---

## ⚙️ Crew Configurations Compared

### 1. Simple Crew (No Tools)

- **Agents**: 1 (Basic Summarizer)  
- **Tools**: None  

**Capabilities:**
- Uses only internal knowledge  
- Produces short summaries  

**Key Insight:**  
Fast but limited depth and outdated context.

---

### 2. Advanced Crew (With Web Tools)

- **Agents**: 1 (Web Search Summarizer)  
- **Tools**:
  - `SerperDevTool`
  - `ScrapeWebsiteTool`

**Capabilities:**
- Fetches real-time data  
- Produces structured summaries  

**Key Insight:**  
More accurate and up-to-date.

---

### 3. Multi-Agent System (Collaborative AI)

- **Agents**: 2

#### 🔹 Data Collector
- Role: Lead Data Acquisition Specialist  
- Tools: Search + Scraping  
- Task: Gather verified data  

#### 🔹 Data Analyst
- Role: Principal Insights Architect  
- Task:
  - Trend analysis  
  - Insight extraction  
  - Final report generation  

**Workflow:**
1. Data Collection  
2. Data Analysis  
3. Report Generation  

**Key Insight:**  
Highest quality, structured and insight-rich output.

---

## 🛠️ Tech Stack

- **Framework**: CrewAI  
- **LLM**: Ollama (Gemma model)  
- **Language**: Python  

**Tools Used:**
- `SerperDevTool`  
- `ScrapeWebsiteTool`  

---

## 🔄 Workflow

### Step 1: Environment Setup
- Install dependencies  
- Configure Ollama  

### Step 2: Agent Design
- Define roles and goals  

### Step 3: Task Creation
- Assign structured tasks  

### Step 4: Crew Execution
```python
crew.kickoff(inputs={...})
```

### Step 5: Save Outputs
- `simple_crew_report.md`  
- `web_search_crew_report.md`  
- `universal_analysis_report.md`  

---

## 📊 Output Comparison

| Setup | Tools | Agents | Output Quality |
|------|------|--------|---------------|
| Simple Crew | ❌ | 1 | Basic |
| Advanced Crew | ✅ | 1 | Good |
| Multi-Agent | ✅ | 2 | Excellent |

---

## 🎯 Key Learnings

- Simple agents → fast but shallow  
- Tool-based agents → more accurate  
- Multi-agent systems → best reasoning + insights  

---

## 🚀 Use Cases

- Research Automation  
- Data Analysis Pipelines  
- AI Reporting Systems  
- Market Intelligence  

---

## 👤 Credits

Made with ❤️ by **Ashish Jangra**  
Powered by **CrewAI & Ollama**
