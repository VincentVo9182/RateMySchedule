import streamlit as st
from Student import Student

# Define CSS styles
header_style = """
    background-color: #E65100;
    color: white;
    font-size: 24px;
    padding: 10px;
    text-align: center;
    font-weight: bold;
"""

section_style = """
    margin: 20px;
    padding: 20px;
    background-color: #f0f0f0;
    border: 1px solid #ddd;
    border-radius: 10px;
"""

def student_profile_page():
    new_student = st.session_state.new_student

    # Header with styling
    st.markdown("<div style='" + header_style + "'>Student Profile</div>", unsafe_allow_html=True)
    st.write("")
    display_student_profile(new_student)  # Display the profile at the top

    # Add a visual separation and style the "Edit Profile" section
    st.markdown("<hr style='margin: 10px;'>", unsafe_allow_html=True)
    st.markdown("<div style='" + header_style + "'>Edit Profile</div>", unsafe_allow_html=True)
    st.write("")

    first_name = st.text_input("First Name", new_student.first_name)
    last_name = st.text_input("Last Name", new_student.last_name)
    eid = st.text_input("EID", new_student.eid)
    major = st.text_input("Major", new_student.major)
    classification = st.selectbox("Classification", ["Freshman", "Sophomore", "Junior", "Senior"], index=2)  # Default to "Junior"
    minor = st.text_input("Minor", new_student.minor)

    if st.button("Save Changes"):
        if not first_name or not last_name or not eid or not major:
            st.error("Please fill out all the required fields.")
        else:
            # Update the student object with the modified information
            new_student.first_name = first_name
            new_student.last_name = last_name
            new_student.eid = eid
            new_student.major = major
            new_student.classification = classification
            new_student.minor = minor
            st.experimental_rerun()
            


def display_student_profile(student):
    st.write(f"**Name**: {student.first_name} {student.last_name}")
    st.write(f"**EID**: {student.eid}")
    st.write(f"**Major**: {student.major}")
    st.write(f"**Classification**: {student.classification}")
    st.write(f"**Minor**: {student.minor}")

if __name__ == "__main__":
    if 'new_student' not in st.session_state:
        st.error("Please create a student profile first.")
    else:
        student_profile_page()

navigation = '''
<style>
    [data-testid="stSidebarNav"] {
        background-image: url(https://i.ibb.co/sPwZpRS/RMS.png);
        background-repeat: no-repeat;
        background-position: 0px 0px;
        background-size: 100%;
    }
    [data-testid='stSidebarNav'] > ul {
        min-height: 45vh;
    }
</style>
'''
sidebar = '''
<style>
    [data-testid=stSidebar] {
    }
</style>
'''

st.markdown(navigation, unsafe_allow_html=True)
st.markdown(sidebar, unsafe_allow_html=True)