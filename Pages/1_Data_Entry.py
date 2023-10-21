import streamlit as st
from student import Student  # Import Student class from student.py

def main():
    st.title("Student Data Entry Form")

    students = []

    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    eid = st.text_input("EID")
    major = st.text_input("Major")
    classification = st.selectbox("Classification", ["Freshman", "Sophomore", "Junior", "Senior"])
    minor = st.text_input("Minor")

    if st.button("Submit"):
        new_student = Student(first_name, last_name, eid, major, classification, minor)
        students.append(new_student)

    st.header("Existing Student Profiles")

    for student in students:
        st.subheader(student)

if __name__ == "__main__":
    main()