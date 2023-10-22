import streamlit as st
from student import Student

def student_profile_page():
    st.title("Student Profile")
    
    if 'new_student' not in st.session_state:
        st.session_state.new_student = Student("", "", "", "", "", "")

    new_student = st.session_state.new_student

    display_student_profile(new_student)  # Display the profile at the top

    # Add a visual separation and style the "Edit Profile" section
    st.markdown("<hr style='margin: 10px;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-weight: bold;'>Edit Profile</h2>", unsafe_allow_html=True)

    first_name = st.text_input("First Name", new_student.first_name)
    last_name = st.text_input("Last Name", new_student.last_name)
    eid = st.text_input("EID", new_student.eid)
    major = st.text_input("Major", new_student.major)
    classification = st.selectbox("Classification", ["Freshman", "Sophomore", "Junior", "Senior"], index=2)  # Default to "Junior"
    minor = st.text_input("Minor", new_student.minor)

    if st.button("Save Changes"):
        # Update the student object with the modified information
        new_student.first_name = first_name
        new_student.last_name = last_name
        new_student.eid = eid
        new_student.major = major
        new_student.classification = classification
        new_student.minor = minor

def display_student_profile(student):
    st.write(f"Name: {student.first_name} {student.last_name}")
    st.write(f"EID: {student.eid}")
    st.write(f"Major: {student.major}")
    st.write(f"Classification: {student.classification}")
    st.write(f"Minor: {student.minor}")

if __name__ == "__main__":
    student_profile_page()