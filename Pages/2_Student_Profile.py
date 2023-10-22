import streamlit as st
from student import Student

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
    st.image("RMS.png", width=300)
    st.title("Student Profile")
    
    if 'new_student' not in st.session_state:
        st.session_state.new_student = Student("", "", "", "", "", "")

    new_student = st.session_state.new_student

    # Header with styling
    st.markdown("<div style='" + header_style + "'>Student Profile</div>", unsafe_allow_html=True)

    # Display the student profile
    with st.container():
        st.markdown("<h3>Profile Information</h3>", unsafe_allow_html=True)
        display_student_profile(new_student)

    # Add a visual separation
    st.markdown("<hr style='margin: 10px;'>", unsafe_allow_html=True)

    # Edit Profile section with styling
    st.markdown("<div style='" + header_style + "'>Edit Profile</div>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<h3>Edit Your Profile</h3>", unsafe_allow_html=True)
        edit_profile(new_student)

def edit_profile(student):
    first_name = st.text_input("First Name", student.first_name)
    last_name = st.text_input("Last Name", student.last_name)
    eid = st.text_input("EID", student.eid)
    major = st.text_input("Major", student.major)
    classification = st.selectbox("Classification", ["Freshman", "Sophomore", "Junior", "Senior"], index=2)  # Default to "Junior"
    minor = st.text_input("Minor", student.minor)

    if st.button("Save Changes"):
        # Update the student object with the modified information
        student.first_name = first_name
        student.last_name = last_name
        student.eid = eid
        student.major = major
        student.classification = classification
        student.minor = minor

def display_student_profile(student):
    st.write(f"**Name**: {student.first_name} {student.last_name}")
    st.write(f"**EID**: {student.eid}")
    st.write(f"**Major**: {student.major}")
    st.write(f"**Classification**: {student.classification}")
    st.write(f"**Minor**: {student.minor}")

if __name__ == "__main__":
    student_profile_page()