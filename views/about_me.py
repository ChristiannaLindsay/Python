import streamlit as st

# Hero section
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/headshot.png", width=280)
with col2:
    st.title("Christianna Lindsay", anchor=False)
    st.write(
        """
        Email: christianna.lindsay@outlook.com

        LinkedIn: https://www.linkedin.com/in/christianna-lindsay-a79888229

        Github: https://github.com/ChristiannaLindsay
        """
    )

# About me
st.write("\n")
st.subheader("About Me", anchor=False)
st.write(
    """
    I am a recent graduate with a Masters in Statistics,
    seeking a full-time position where I can apply my analytical skills
    in the service of a meaningful purpose.
    I am passionate about data analysis and collaboration, and I am particularly interested in biological,
    engineering, and economic applications. I have experience in a range of areas,
    including statistical collaboration, biology field work and lab work, and teaching.
    """
)

# Education
st.write("\n")
st.subheader("Education", anchor=False)
st.write(
    """
    M.S. in Statistics - Virginia Tech - Blacksburg, VA (2024)

    B.S. in Biology and Applied Mathematics - Hillsdale College - Hillsdale, MI (2022)
    """
)

# Skills
st.write("\n")
st.subheader("Software", anchor=False)
st.write(
    """
    RStudio, Python, MATLAB, Git, GitHub, JMP, LaTex, Excel, PowerPoint, ImageJ, ChemDraw
    """
)