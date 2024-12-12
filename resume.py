import streamlit as st

def main():

    st.set_page_config(page_title="Promise Bansah - Bio", page_icon="📄", layout="wide")

    # Sidebar Navigation
    st.sidebar.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSIBfJxFgGX2d961bTaupSiOuAS8TmF_7BC0g&s",
        width=150,
    )
    menu = ["About Me", "Key Projects", "Education", "Current Focus", "Contact"]
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
    if choice == "Education":
        st.header("Education")
        st.markdown(
            """
            - **Bachelors in Public Health, Disease Control** - University of Health and Allied Sciences, Ghana (2019)  
            - **Advanced Data Science & Analytics Certification** - Koforidua Technical University, Ghana (2024)  
            - **MPhil in Biomedical Data Science** (In Progress)
            """
        )
    elif choice == "Contact":
        st.header("Contact")
        st.markdown(
            """
            - **Email:** promise.bansah@example.com  
            - **GitHub:** [Promisekel](https://github.com/Promisekel)  
            - **LinkedIn:** [Promise Bansah](https://www.linkedin.com/in/promisekel/)  
            """
        )

if __name__ == "__main__":
    main()
