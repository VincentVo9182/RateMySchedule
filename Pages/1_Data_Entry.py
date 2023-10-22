import streamlit as st
import Student  # Import Student class from student.py

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

def data_entry_page():
    # Header with styling
    st.markdown("<div style='" + header_style + "'>Student Data Entry Form</div>", unsafe_allow_html=True)
    st.write("")
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