import streamlit as st

def main():
    # Page configuration
    st.set_page_config(page_title="Promise Bansah - Bio", page_icon="📄", layout="wide")

    # Sidebar Navigation
    st.sidebar.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIBfJxFgGX2d961bTaupSiOuAS8TmF_7BC0g&s",
        width=150,
    )
    menu = ["About Me", "Key Projects", "Education", "Skills & Competencies", "Current Focus", 
            "Training Workshops and Conferences", "Membership, License and Certification", 
            "Achievements", "Reviewed Manuscripts for Potential Publication", 
            "Community Involvement", "Interests/Hobbies", "Contact"]
    choice = st.sidebar.radio("Go to", menu)

    # Styling
    st.markdown(
        """
        <style>
        .main {background-color: #f8f9fa;}
        .stSidebar {background-color: #6c757d; color: white;}
        h1, h2, h3, h4, h5, h6 {color: #343a40;}
        .css-1aumxhk {background-color: #ffffff;}
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Header Section
    st.title("Promise Bansah")
    st.markdown("##### Researcher | Public Health Expert | Data Scientist")

    # Content Sections
    if choice == "About Me":
        st.header("About Me")
        st.markdown(
            """
            **Promise Bansah**  
            I am a researcher and data scientist passionate about using data for positive social impact through evidence-based research, particularly in Africa. 
            With a strong foundation in epidemiology, public health, biostatistics, and data science, I have developed my skills in data analytics, machine learning, 
            and data visualization.
            My previous and current experiences have demonstrated my ability to apply data science to address complex challenges, such as developing a model 
            to predict pneumonia using X-ray images by applying deep learning techniques. 
            In my current project, *Prediction of Malaria Recurrence in Children Under 5 Years After ACT Treatment Using Machine Learning Models in the Central Region of Ghana*, 
            I am particularly focusing on environmental or climate factors that could contribute to recurrent malaria among children under 5 years. 
            I am enthusiastic and eager to contribute to the development of predictive models and their deployment for quality healthcare in Africa. 
            I am seeking opportunities to join a dynamic lab or fellowship to learn, adapt, and apply an entrepreneurial approach to problem-solving 
            to contribute to data-driven solutions for sustainable development.
            """
        )
        st.markdown(
            """
            **With expertise in:**
            ### RESEARCH
            - **Infectious Disease Epidemiology**  
            - **Clinical Research**  
            - **Publication**  
            - **Data Analysis and Presentation** 

            ### PROGRAMMING
            - **Software Engineering**  
            - **Android Application Development**  
            - **Python Coding**

            ### DATA SCIENCE
            - **Machine Learning and Modeling**  
            - **Data Analytics**  
            - **AI**  
            - **R**  
            - **Digital Health**
            """
        )
    elif choice == "Reviewed Manuscripts for Potential Publication":
        st.header("Reviewed Manuscripts for Potential Publication")
        st.markdown(
            """
            **Manuscripts Currently Under Review:**
            - **Factors contributing to paracetamol overdoses (Intentional and Accidental) among the population in the United Kingdom: A Systematic Review Protocol** for BMJ Open  
              (Manuscript ID: bmjopen-2024-090135)
            - **Exploring family-based immigrant youth substance use prevention programs: a scoping review** for Substance Abuse: Research and Treatment  
              (Manuscript ID: SAT-23-0046)
            - **Correlates of Staff Acceptability of a Novel Telemedicine Buprenorphine Program in a Rural Detention Centre**  
              (Manuscript ID: SAT-23-0016)
            """
        )
    elif choice == "Key Projects":
        st.header("Key Projects")
        st.markdown(
            """
            <style>
            .key-project {
                background-color: #f8f9fa;
                padding: 15px;
                margin: 10px 0;
                border-radius: 10px;
                box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
            }
            .project-title {
                font-weight: bold;
                font-size: 18px;
                color: #343a40;
            }
            .project-link {
                color: #007bff;
                text-decoration: none;
                font-size: 16px;
            }
            .project-link:hover {
                text-decoration: underline;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        projects = [
            {
                "title": "Developed deep learning model for predicting pneumonia using X-ray images",
                "link": "https://github.com/Promisekel/pneumonia-detection",
            },
            {
                "title": "Developed Android app for File Management",
                "link": "https://play.google.com/store/apps/details?id=com.example.filemanager",
            },
            {
                "title": "Developed Android app for project management at KCCR",
                "link": "",
            },
            {
                "title": "Developed a Bible Verse Android App",
                "link": "https://play.google.com/store/apps/details?id=com.example.bibleverse",
            },
            {
                "title": "CEO of Premiere Scientific and Research Publication Club",
                "link": "https://premirescientific.com",
            },
        ]

        for project in projects:
            st.markdown(
                f"""
                <div class="key-project">
                    <div class="project-title">{project['title']}</div>
                    {'<a class="project-link" href="' + project['link'] + '" target="_blank">View Project</a>' if project['link'] else '<span style="color: #6c757d;">Link unavailable</span>'}
                </div>
                """,
                unsafe_allow_html=True,
            )
    elif choice == "Community Involvement":
        st.header("Community Involvement")
        st.markdown(
            """
            **Organized Data Analysis and Research Method Workshops for Undergraduate Students**  
            I have been actively involved in organizing workshops aimed at improving data analysis and research methods skills among undergraduate students. The goal of these workshops is to equip students with the skills they need to excel in their academic pursuits and contribute to their research projects. These sessions cover basic data analysis, research methodologies, and the importance of evidence-based approaches in research.
            """
        )
    elif choice == "Interests/Hobbies":
        st.header("Interests/Hobbies")
        st.markdown(
            """
            **Programming**  
            I enjoy programming and building applications to solve real-world problems, particularly in health and public health contexts.

            **Research**  
            My passion for research drives me to continuously explore new methodologies and technologies in the fields of data science, public health, and epidemiology.

            **Gaming**  
            In my free time, I indulge in gaming, which provides a fun and interactive way to unwind and sharpen my problem-solving skills.
            """
        )
    elif choice == "Training Workshops and Conferences":
        st.header("Training Workshops and Conferences")
        st.markdown(
            """
            **Workshops and Certifications:**
            - **Next Generation Sequencing (NGS) and Bioinformatics Workshop** on microbial pathogens | KCCR  
            - **Introduction to Biomedical and Health Research (B-HERE) Workshop** | KCCR  
            - **Building Self-Service Analytics with Snowflake Cortex Analyst** | Snowflake  
            - **5-Day Gen AI Intensive Course** | Kaggle/Google  
            - **GCP and GLCP Training** | FDA  
            - **Qualitative and Quantitative Data Analysis** | UHAS  
            - **Spatial Data Analysis using ArcMap GIS** | UHAS  
            - **REDCap Software Training** | UHAS  
            """
        )
    elif choice == "Membership, License and Certification":
        st.header("Membership, License and Certification")
        st.markdown(
            """
            **Memberships and Certifications:**
            - **Certified Data Analyst** | Data Science Academy  
            - **AI and Machine Learning Certification** | Coursera  
            - **Member of Global Health Research Network**  
            - **Member of Public Health Data Science Network**  
            - **Certified Health Informatics Professional (CHIP)** | Health Informatics Certification Organization  
            """
        )
    elif choice == "Achievements":
        st.header("Achievements")
        st.markdown(
            """
            **Notable Achievements:**
            - Developed **deep learning model for predicting pneumonia** using X-ray images  
              [View Model](https://github.com/Promisekel/pneumonia-detection)
            - Developed **Android app for File Management** on Google Play  
              [View App](https://play.google.com/store/apps/details?id=com.example.filemanager)
            - Developed **Android app for project management at KCCR**
            - Developed **Bible Verse Android App** on Google Play  
              [View App](https://play.google.com/store/apps/details?id=com.example.bibleverse)
            - CEO of **Premiere Scientific and Research Publication Club**  
              [View Club](https://premirescientific.com)
            """
        )
    elif choice == "Education":
        st.header("Education")
        st.markdown(
            """
            <style>
            .education-entry {
                background-color: #f8f9fa;
                padding: 15px;
                margin: 10px 0;
                border-radius: 10px;
                box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
            }
            .education-title {
                font-weight: bold;
                font-size: 18px;
                color: #343a40;
            }
            .education-institution {
                color: #6c757d;
                font-size: 16px;
            }
            .education-date {
                color: #007bff;
                font-size: 14px;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        education = [
            {
                "title": "Advanced Data Analytics",
                "institution": "Koforidua Technical University, Ghana",
                "date": "2024"
            },
            {
                "title": "Machine Learning and AI",
                "institution": "Koforidua Technical University, Ghana",
                "date": "2024"
            },
            {
                "title": "Bachelor of Science in Public Health (Disease Control)",
                "institution": "University of Health and Allied Sciences, Ghana",
                "date": "2019"
            }
        ]

        for entry in education:
            st.markdown(
                f"""
                <div class="education-entry">
                    <div class="education-title">{entry['title']}</div>
                    <div class="education-institution">{entry['institution']}</div>
                    <div class="education-date">{entry['date']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    elif choice == "Contact":
        st.header("Contact")
        st.markdown(
            """
            You can reach me via:
            - Email: **promisekel@healthscience.org**
            - Phone: **+233 123 456 789**
            - LinkedIn: **[Promise Bansah](https://www.linkedin.com/in/promisekel)**
            - GitHub: **[PromiseBansah](https://github.com/Promisekel)**
            """
        )

if __name__ == "__main__":
    main()
