import streamlit as st
import student  # Import Student class from student.py

def data_entry_page():
    st.title("Student Data Entry Form")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    eid = st.text_input("EID")
    major = st.text_input("Major")
    classification = st.selectbox("Classification", ["Freshman", "Sophomore", "Junior", "Senior"])
    minor = st.text_input("Minor")

    if st.button("Submit"):
        new_student = student.Student(first_name, last_name, eid, major, classification, minor)
        st.session_state.new_student = new_student  # Store the new student in session_state
        st.experimental_rerun()  # Rerun the Streamlit app to trigger redirection

if __name__ == "__main__":
    data_entry_page()