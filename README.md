# Smart-Chatbot
# 🤖 Conversational AI Assistant: Real-Time Intelligent Chat Interface

A robust, enterprise-grade AI Chatbot application built using the official **Google GenAI SDK**, leveraging the high-speed **Gemini 3.5 Flash** model. This project features full session-state management for tracking user context and integrates low-latency, real-time response streaming inside an intuitive **Streamlit** user interface.

---

## 🎯 Project Purpose & Impact (Why This Matters)
In modern business environments, automated customer support, internal data retrieval, and user interaction layers rely heavily on intelligent conversational agents. 

This project goes beyond a simple API call; it demonstrates how to architect a production-ready interface that bridges advanced LLMs with a responsive frontend. 

*   **For AI Engineering Roles:** It showcases core GenAI implementation skills—handling streaming tokens via `send_message_stream`, system architecture management, configuration tuning, and real-time state management.
*   **For Data Analyst Roles:** It highlights an understanding of user interaction logic, structured context maintenance, optimization of compute resources (managing API rate limits), and the ability to deploy clean, data-driven application dashboards for stakeholders.

---

## 🚀 Key Features
*   **Low-Latency Token Streaming:** Implements immediate, live response rendering (`st.write_stream`) mimicking modern conversational apps (like ChatGPT) to significantly optimize user retention.
*   **Context-Aware Memory:** Utilizes Streamlit session states to perfectly manage chat history, ensuring the LLM maintains strict conversational context over multi-turn dialogues.
*   **Modular Technical Design:** Built with isolated configuration parameters (`GenerateContentConfig`) allowing rapid adjustment of system instructions and creativity indices (temperature controls).

---

## 🛠️ Tech Stack & Architecture
*   **Core Language:** Python 3.10+
*   **Frontend Interface:** Streamlit (Dynamic state components)
*   **AI SDK & Orchestration:** Official `google-genai` client layer
*   **Underlying Engine:** `gemini-3.5-flash`

---

## 💻 Setup & Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

2. Install Dependencies
pip install -r requirements.txt

3. Configure Your Environment
Open app.py and input your secure Google Gemini API key:
MY_GOOGLE_KEY = "YOUR_AQ_API_KEY_HERE"

4. Deploy the Local Server
streamlit run app.py

