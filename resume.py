import streamlit as st

def main():
    st.set_page_config(page_title="Promise Bansah - Bio", page_icon="📄", layout="wide")

    # Sidebar Navigation
    #st.sidebar.title("Navigation")
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
    st.markdown("### Researcher | Public Health Expert | Data Scientist")
    #st.image("https://via.placeholder.com/300", caption="Profile Picture", use_column_width=True)

    # Content Sections
    if choice == "About Me":
        st.header("About Me")
        st.markdown(
            """
            **Promise Bansah** I am a researcher and data scientist passionate about using data for positive social impact through
            evident-based research, particularly in Africa. With a strong foundation in epidemiology, public health, biostatistics
            and data science and machine learning, I have developed my skills in data analytics, machine learning and data visualization.
            My previous and current experiences have demonstrated my ability to apply data science to address complex challenges,
            such as developing a model to predict pneumonia using x-ray image by applying deep learning techniques. 
            In my current project “prediction of malaria recurrence in children under 5 years after ACT treatment using machine learning models 
            in the Central Region of Ghana.” Particularly focusing on environmental or climate factors or features that could contribute
            to recurrent malaria among children under 5 years. I am enthusiastic and eager to contribute to the development of predictive
            model and deploy for quality healthcare in Africa. I am seeking opportunities to join a dynamic lab or fellowship to learn, adaptability, 
            and apply an entrepreneurial approach to problem solving to contribute to data-driven solutions for sustainable development.. 

            With expertise in:
            RESEARCH
                - Infectious Disease Epidemiology
                - Clinical Research
                - Publication
                - Data Analysis and Presentation
            PROGRAMMING
                - Software Engineerring
                - Android Application Development
                - Python Coding
            DATA SCIENCE
                - Machine Learning and modelling
                - Data analytics 
                - AI
                - R
                - Digital Health
            
            Promise is dedicated to leveraging data-driven solutions for improved health outcomes.
            """
        )

    elif choice == "Key Projects":
        st.header("Key Projects")
        projects = {
            "Dengue Outbreak Forecasting": "Developing a multimodal machine learning framework to predict dengue outbreaks using heterogeneous data.",
            "Predicting Malaria Recurrence": "Using deep learning models to predict malaria recurrence in children under 5 years after ACT treatment.",
            "Pneumonia Detection App": "A Streamlit app leveraging AI for detecting pneumonia from chest X-rays.",
        }

        for title, description in projects.items():
            st.subheader(title)
            st.markdown(f"- {description}")

    elif choice == "Education":
        st.header("Education")
        st.markdown(
            """
            - **Bachelor's in Public Health, Disease Control** - University of Health and Allied Sciences, Ghana (2019)
            - **Advanced Data Science & Analytics Certification** - Koforidua Technical University, Ghana (2024)
            - **MPhil in Biomedical Data Science** (In Progress)
            """
        )

    elif choice == "Current Focus":
        st.header("Current Focus")
        st.markdown(
            """
            - Preparing for an examination covering Algebra, Calculus, Data Science, Molecular Biology, and diseases like malaria and cleft palate.
            - Developing Android Studio projects with Firebase integration.
            - Coordinating research manuscripts for publication.
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
