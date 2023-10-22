import streamlit as st
import Student  # Import Student class from student.py

def data_entry_page():
    st.title("Student Data Entry Form")
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    eid = st.text_input("EID")
    major = st.text_input("Major")
    classification = st.selectbox("Classification", ["Freshman", "Sophomore", "Junior", "Senior"])
    minor = st.text_input("Minor")

    if st.button("Submit"):
        if not first_name or not last_name or not eid or not major:
            st.error("Please fill out all the required fields.")
        else:
            # Return a success message
            st.success("Information submitted successfully!")
            st.write(f"Thank you {first_name} {last_name} for submitting your information.")
            st.write("Here is the information you submitted:")
            st.write("First Name: " + first_name)
            st.write("Last Name: " + last_name)
            st.write("EID: " + eid)
            st.write("Major: " + major)
            new_student = Student.Student(first_name, last_name, eid, major, classification, minor)
            st.session_state.new_student = new_student  # Store the new student in session_state

if __name__ == "__main__":
    data_entry_page()