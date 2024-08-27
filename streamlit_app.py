import streamlit as st

# Page setup
about_page = st.Page(
    page = "views/about_me.py",
    title = "About Me",
    icon = ":material/face:",
    default = True,
)

project_1_page = st.Page(
    page = "views/project1.py",
    title = "Nutrition Tool",
    icon = ":material/nutrition:",
)

project_2_page = st.Page(
    page = "views/project2.py",
    title = "Predicting Happiness using GSS",
    icon = ":material/sentiment_satisfied:",  
)

# Navigation Setup (with sections)
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page]
    }
)

#Run navigation
pg.run()
