import streamlit as st
import os
from google import genai
from dotenv import load_dotenv
load_dotenv()

# gemini api
os.getenv("GOOGLE_GEMINI_KEY")

client = genai.Client(api_key=API_KEY)

#your resume data
my_data = """"
========================
PRACHI'S RESUME
========================

CONTACT
-------
Mobile: +91-9034461378


SKILLS
------

Programming Languages
• C
• C++
• Java
• JavaScript
• Python
• SQL
• Kotlin

Web & Mobile Development
• HTML
• CSS
• React
• Node.js
• Express.js
• JSON
• REST APIs
• JWT
• OAuth 2.0
• MongoDB

Machine Learning & AI
• Pandas
• NumPy
• Matplotlib
• Seaborn
• Scikit-learn

Data Visualization & Analytics
• Power BI
• Microsoft Excel

Tools & Development
• Git
• GitHub
• Postman
• Railway
• Android Studio

Soft Skills
• Adaptability
• Problem Solving
• Collaboration
• Team Management


==================================================
PROJECTS
==================================================

1. Society Help Desk – Complaint & Issue Tracker System
-------------------------------------------------------

• Developed a full-stack society management platform using
  Node.js, Express, and MongoDB for structured complaint
  lifecycle handling via RESTful APIs.

• Integrated Google OAuth 2.0 and JWT for secure authentication,
  implementing custom RBAC middleware to protect sensitive
  administrative management routes.

• Engineered a dual-mode authentication fallback
  (Popup/Redirect) and optimized MongoDB with
  unique/sparse indexing for high availability in production.

• Designed a responsive glassmorphism UI with real-time
  complaint tracking and filtering.

• Deployed the application using Railway with secure
  environment variable management.

Tech Stack:
Node.js, Express.js, MongoDB Atlas, Google OAuth 2.0,
JWT, REST API, JavaScript, HTML5, CSS3, Railway


--------------------------------------------------

2. Lifestyle Health Risk Prediction
   ML-Based Lifestyle Risk Analysis System
-------------------------------------------------------

• Developed an end-to-end machine learning pipeline to predict
  lifestyle-related health risks using real-world survey data
  collected through Google Forms.

• Performed comprehensive data preprocessing, feature
  engineering, and exploratory data analysis.

• Implemented regression, classification, and clustering
  models to identify risk patterns and predictive indicators.

• Leveraged AutoML for:
    - Automated model selection
    - Hyperparameter optimization
    - Performance evaluation

• Improved predictive accuracy while enabling efficient
  experimentation workflows.

Tech Stack:
Python, Scikit-learn, Pandas, NumPy,
Matplotlib, Machine Learning, AutoML


--------------------------------------------------

3. Process Visualizer
   CPU Scheduling Simulator with Real-Time Visualization
-------------------------------------------------------

• Developed a simulator implementing:
    - FCFS
    - SJF
    - Priority Scheduling
    - Round Robin

• Automated computation of:
    - Waiting Time
    - Turnaround Time

• Engineered a modular scheduling engine with dynamic
  process state transitions for both preemptive and
  non-preemptive scheduling.

• Built a Tkinter-based GUI integrated with Matplotlib
  Gantt Charts for real-time visualization of CPU scheduling.

Tech Stack:
Python, Tkinter, Matplotlib,
Data Structures & Algorithms,
Operating Systems


==================================================
TRAINING
==================================================

Lovely Professional University
(in collaboration with byteXL)

Data Structures & Algorithms Trainee

• Completed a two-month intensive training in Data Structures
  & Algorithms using C++.

• Strengthened problem-solving skills and algorithmic thinking
  with complexity optimization techniques.

• Designed and developed a Travel Expense Tracker web
  application using Object-Oriented JavaScript.

• Implemented:
    - Stack for Undo operations
    - Binary Search Tree (BST) for organization
    - Hash Map for O(1) currency lookup

Tech Stack:
C++, JavaScript (OOP), HTML, CSS,
Data Structures & Algorithms


==================================================
CERTIFICATIONS
==================================================

• Data Structures & Algorithms using C++ — byteXL

• Cloud Computing Certification — NPTEL


==================================================
EDUCATION
==================================================

Lovely Professional University
--------------------------------
Bachelor of Technology (B.Tech.)
Computer Science & Engineering

CGPA: 8.10


Bhartiya Public School
--------------------------------
Intermediate (PCM)

Percentage: 84%


Bhartiya Public School
--------------------------------
Matriculation

Percentage: 90.02%
"""

#page settings
st.set_page_config(
    page_title="Prachi AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("Prachi AI Resume Assistant")
st.write("Ask me anything about Prachi or any general question.")


#chat history

if "messages" not in st.session_state:
    st.session_state.messages=[]

#show old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


#user input
question = st.chat_input("Type your question.....")

if question:
    st.session_state.messages.append(
        {"role":"user","content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    prompt=f"""You are Prachi's AI Assistant.
            Rules:
            1. Answer using resume if possible.
            2. Otherwise answer using general knowledge.
            3. Keep answers simple.
            
            Resume:
            {my_data}

            Question:
            {question}
            """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        answer = response.text
    except Exception as e:
        answer = f"Error: {e}"

    st.session_state.messages.append(
        {"role":"assistant","content":answer}
    )

    with st.chat_message("assistant"):
        st.markdown(answer)
