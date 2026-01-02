# Text-to-SQL via Prompt Engineering

This project provides a comprehensive guide to building an intelligent **Text-to-SQL assistant**. This technology, also known as **Natural Language to SQL (NL2SQL)**, serves as a bridge between everyday human language and complex relational databases. By leveraging **Google Gemini** and advanced prompt engineering, users can retrieve data by simply asking questions in plain English, democratizing data access across an organization.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1qo5OZ2-uOpGbEWfeV5cMxVHLo8zA9z2o?usp=sharing)

The system functions as an intelligent translator, using **Natural Language Processing (NLP)** to interpret user intent and generate precise SQL queries.

---

## 📌 What This Project Can Do

- **Natural Language Understanding**: Translates everyday English questions into valid Structured Query Language (SQL) commands.
- **Multi-Table Reasoning**: Automatically handles complex operations like **JOINs** across multiple tables to find related information.
- **Schema Awareness**: Adapts to specific database structures (tables and columns) provided within the prompt context.
- **Automated Data Retrieval**: Directly executes generated queries against a database to fetch real-time results.
- **Conversational Insights**: Synthesizes raw database results into human-readable answers for the end user.

---

## 📁 About the Dataset

The project utilizes a relational database structure designed to represent a company's internal hierarchy:

- **Employees Table**: Contains `Employee_ID`, `Name`, `Role`, `Salary`, and `Department_ID`.
- **Departments Table**: Contains `Department_ID` and `Department_Name`.


---

## 🛠️ Getting Started

### Step 1: Install the required packages
To begin, you must install the Google Generative AI library.
Command: pip install -q -U google-generativeai

### Step 2: Configure your API Key
You will need a Google AI Studio API Key to access the Gemini models.
python: 
import google.generativeai as genai
genai.configure(api_key="YOUR_API_KEY")

---

## 🚀 How It Works


### 1. Database Setup
The system initializes a local **SQLite** database using Python's built-in libraries. It creates the necessary tables for employees and departments and populates them with sample records for testing.

### 2. Prompt Engineering
A detailed system instruction is crafted that includes the full **Database Schema**. This context guides the model to understand specific table relationships and the required SQL dialect.

### 3. SQL Generation
The user's question is sent to the Gemini model along with the schema context. The model processes this information to generate a valid SQL string tailored to the specific question.

### 4. Execution & Retrieval
The system extracts the SQL code from the model's response and executes it against the local database. This step ensures that the data returned is accurate and up-to-date.

### 5. Natural Language Response
The final step involves passing the raw query results back to the model, which then summarizes the findings into a clear, natural language answer for the user.

---

## 💬 Quick Example

**User Question**: "Who is the highest paid employee in the Engineering department?"

**Generated SQL**: SELECT Name, MAX(Salary) FROM Employees JOIN Departments ON Employees.Department_ID = Departments.Department_ID WHERE Department_Name = 'Engineering';

---

## 💡 Use It For

- **Business Intelligence**: Rapidly prototype data queries without requiring manual SQL coding.
- **Internal Tools**: Create bots that allow non-technical staff to search company records via chat.
- **Education**: Assist students in learning SQL by showing real-time translations of their questions into code.
- **Autonomous Agents**: Use as a core tool for AI agents that need to query live databases to perform complex tasks.

---

## ✅ Final Thoughts

Combining high-performance LLMs like Gemini with strategic prompt engineering makes data interaction as simple as a conversation. While this project uses a sample dataset, the foundation is scalable to enterprise-grade systems or specialized fine-tuned models for industry-specific needs.

---

## 👤 Credits

Made with ❤️ by [Ashish Jangra](https://github.com/AshishJangra27)  
Powered by: Google Gemini, SQLite, and Prompt Engineering.
