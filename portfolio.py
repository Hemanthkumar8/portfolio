import streamlit as st
import pandas as pd  # Optional for future table/data usage

# Page Configuration
st.set_page_config(page_title="Hemanth Kumar Portfolio", layout="wide")

# Title
st.title("My Portfolio")

# Navigation Tabs
home_tab, about_tab, projects_tab, experience_tab, contact_tab = st.tabs(["Home", "About", "Projects", "Experience", "Contact"])

with home_tab:
    st.header("🏠 Home")

    # Profile Section
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("https://tse1.mm.bing.net/th?id=OIP.rVDfmJwnrS6PtliBeJvB4wHaHa&pid=Api&P=0&h=180", width=200, caption="Hemanth Kumar")

    with col2:
        st.markdown("""
        <h2 style='text-align: left;'>Welcome!</h2>
        <p style='text-align: left;'>I'm <strong>Hemanth Kumar</strong>, a passionate software engineer focused on building innovative, scalable, and user-centric applications.</p>
        <p style='text-align: left;'>I specialize in Python, .NET, and Machine Learning. I'm constantly exploring new technologies and love turning ideas into reality.</p>
        <p style='text-align: left;'>📫 Connect with me:</p>
        <p style='text-align: left;'>
            <a href='https://github.com/Hemanthkumar8' target='_blank'>🔗 GitHub</a> | 
            <a href='https://linkedin.com/in/yourlinkedin' target='_blank'>🔗 LinkedIn</a>
        </p>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Technical Skills Section
    st.markdown("### 🧠 Technical Skills")

    skill_col1, skill_col2, skill_col3, skill_col4 = st.columns(4)

    with skill_col1:
        st.markdown("""
        #### 💻 Programming Languages  
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="30"/> Python  
        <br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg" width="30"/> C  
        <br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg" width="30"/> C#
        """, unsafe_allow_html=True)

    with skill_col2:
        st.markdown("""
        #### 🌐 Web & Database  
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" width="30"/> HTML  
        <br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" width="30"/> MySQL  
        <br><img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg" width="30"/> Streamlit  
        <br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" width="30"/> SQLite  
        """, unsafe_allow_html=True)

    with skill_col3:
        st.markdown("""
        #### 🧪 Tools & Platforms  
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" width="30"/> Git  
        <br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="30"/> GitHub  
        <br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" width="30"/> VS Code  
        <br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/anaconda/anaconda-original.svg" width="30"/> Anaconda  
        <br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/windows8/windows8-original.svg" width="30"/> Windows
        """, unsafe_allow_html=True)

    with skill_col4:
        st.markdown("""
        #### 🤖 AI / ML / NLP  
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" width="30"/> TensorFlow  
        <br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/keras/keras-original.svg" width="30"/> Keras  
        <br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" width="30"/> NumPy  
        <br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="30"/> Pandas  
        <br><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/scikit-learn/scikit-learn-original.svg" width="30"/> Scikit-learn  
        <br><img src="https://huggingface.co/front/assets/huggingface_logo.svg" width="30"/> Transformers  
        """, unsafe_allow_html=True)


# ---------------------- ABOUT ------------------------
with about_tab:
    st.header("About Me")
    about_options = ["Education", "Skills", "Experience"]
    about_selection = st.radio("Select an option:", about_options)

    if about_selection == "Education":
        st.markdown("""
        ### 🎓 Education
        - B. Tech in CSE (Pursuing) – NRI INSTITUTE OF TECHNOLOGY, JNTU Kakinada (CGPA: 8.1)  
        - Intermediate – SRI SARADA JUNIOR COLLEGE, AP Board (CGPA: 6.0)  
        - SSC – SFS High School, SSC Board (CGPA: 7.3)
        """)
    elif about_selection == "Skills":
        st.markdown("""
        ### 🛠️ Skills
        - Programming: C, .NET (C#), Python  
        - Web Development: HTML  
        - Database: MySQL  
        - Operating Systems: Windows  
        - Soft Skills: Problem-solving, Communication, Teamwork
        """)
    elif about_selection == "Experience":
        st.markdown("""
        ### 💼 Experience

        #### Internship – DRDO RCI  
        - **Project:** 1553 Data Bus Control Protocol  
        - **Tech Stack:** C++  
        - **Duration:** Nov 2023 – Jan 2024  

        #### ChatBot – Blackbuck Engineers Pvt. Ltd  
        - **Tech Stack:** Python, AI/ML  
        - **Duration:** June – Sept 2022  
        """)

    st.subheader("📊 ML vs DL")
    st.markdown("""
    - **ML:** Needs feature engineering, works well with structured data  
    - **DL:** Learns features from unstructured data like images/text  
    - **Similarities:** Both are subsets of AI, need training data  
    """)

# ---------------------- PROJECTS ------------------------
with projects_tab:
    st.header("💻 Projects")

    project_options = ["AI-Powered Image Recognition", "ML-Based Sentiment Analysis"]
    project_selection = st.radio("Select a project:", project_options)

    if project_selection == "AI-Powered Image Recognition":
        st.subheader("🖼️ AI-Powered Image Recognition")
        st.markdown("""
        Built a CNN model to classify handwritten digits using the MNIST dataset.

        - **Tools:** Python, TensorFlow, Keras  
        - **Accuracy:** 98%  
        - **Features:** Automatic feature extraction, minimal preprocessing

        🔗 [GitHub Repository](https://github.com/Hemanthkumar8)
        """)
    elif project_selection == "ML-Based Sentiment Analysis":
        st.subheader("📝 ML-Based Sentiment Analysis")
        st.markdown("""
        A robust sentiment classifier for text data using BERT and RoBERTa.

        - **Tools:** Python, Transformers, NLTK, Scikit-learn  
        - **Accuracy:** 92.3%  
        - **Challenges:** Sarcasm, negation, noise in data  
        - **Deployment:** Streamlit App

        🔗 [GitHub Repository](https://github.com/Hemanthkumar8)
        """)


# ---------------------- EXPERIENCE ------------------------
with experience_tab:
    st.header("💼 Experience")

    st.markdown("""
    ## 🏢 Lyros Technologies  
    **Role:** Software Developer – AI/ML  
    **Duration:** Jan 2024 – Present  
    **Location:** Hyderabad

    ### 🔧 Technologies Used  
    - Python, Streamlit, Pandas, Scikit-learn, Matplotlib  
    - Machine Learning, Web Deployment  

    ### 💻 Project: Heart Disease Prediction App  
    - Built a predictive web app with ML models  
    - Trained using UCI dataset  
    - UI built with Streamlit for real-time input & output  
    - Accuracy improved from 81% to 90%  

    ### 🚀 Contributions  
    - Developed front-end & ML pipeline  
    - Collaborated in model tuning  
    - Focused on UX for non-technical users  

    🔗 [GitHub Repo](https://github.com/Hemanthkumar8)
    """)

# ---------------------- CONTACT ------------------------
with contact_tab:
    st.header("📬 Contact Me")
    st.markdown("""
    **Hemanth Kumar Polukonda**  
    📧 Email: phemanthkumar73@gmail.com  
    💼 LinkedIn: [linkedin.com/in/yourlinkedin](https://linkedin.com/in/yourlinkedin)
    """)

    user_message = st.text_area("Enter your message:")
    if st.button("Submit"):
        st.success("Thank you! Your message has been received.")
