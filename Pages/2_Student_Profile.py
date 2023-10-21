import streamlit as st
from student import Student

def student_profile_page():
    st.title("Student Profile")
    
    if 'new_student' not in st.session_state:
        st.session_state.new_student = Student("", "", "", "", "", "")

    new_student = st.session_state.new_student

    if st.button("Edit Profile"):
        new_student = edit_profile(new_student)  # Get the updated student object
    
    display_student_profile(new_student)

def edit_profile(student):
    st.title("Edit Profile")
    
    first_name = st.text_input("First Name", student.first_name)
    last_name = st.text_input("Last Name", student.last_name)
    eid = st.text_input("EID", student.eid)
    major = st.text_input("Major", student.major)
    classification = st.selectbox("Classification", ["Freshman", "Sophomore", "Junior", "Senior"], index=2)  # Default to "Junior"
    minor = st.text_input("Minor", student.minor)

    if st.button("Save Changes"):
        # Create a new student with the modified information
        updated_student = Student(first_name, last_name, eid, major, classification, minor)
        st.session_state.new_student = updated_student  # Update the session state with the new student object
        st.experimental_rerun()
        return updated_student  # Return the updated student object

    return student  # Return the original student object if changes are not saved

def display_student_profile(student):
    st.write(f"Name: {student.first_name} {student.last_name}")
    st.write(f"EID: {student.eid}")
    st.write(f"Major: {student.major}")
    st.write(f"Classification: {student.classification}")
    st.write(f"Minor: {student.minor}")

if __name__ == "__main__":
    student_profile_page()
