import streamlit as st
import Student

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

# Initialize dict1 using st.session_state
if 'dict1' not in st.session_state:
    st.session_state.dict1 = {}

# Initialize optedIn as an empty list
if 'optedIn' not in st.session_state:
    st.session_state.optedIn = []

def matching_page():
    student = st.session_state.new_student
    st.markdown("<div style='" + header_style + "'>Buddy Finder</div>", unsafe_allow_html=True)
    st.write("")
    uniqueNumber = st.text_input("Enter unique number to OPT IN")

    if st.button("Submit"):
        if len(uniqueNumber) == 5:
            if not uniqueNumber in st.session_state.dict1:
                # new unique number not before seen before
                st.session_state.dict1[uniqueNumber] = []
            # for tracking purposes, add uniqueNumber to optedIn as well
            if not uniqueNumber in st.session_state.optedIn:
                st.session_state.optedIn.append(uniqueNumber)
            # there is now a dictionary entry so we can append to the array
            # if their eid is already in the dict, we don't need to append
            if not student.get_eid() in st.session_state.dict1[uniqueNumber]:
                st.session_state.dict1[uniqueNumber].append(student.get_eid())
            for course in st.session_state.optedIn:
                st.write(f"Course: {course} People: {st.session_state.dict1[course]}")
            # if their eid is already in the dict, we don't need to append
            if not student.get_eid() in st.session_state.dict1[uniqueNumber]:
                st.session_state.dict1[uniqueNumber].append(student.get_eid())
        else:
            st.error("Please enter a 5 digit unique number")
    

    if st.button("Opt out of ALL courses"):
        for course in st.session_state.optedIn:
            if len(course) == 5:
                st.session_state.dict1[course].remove(student.get_eid())
        st.session_state.optedIn = []



if __name__ == "__main__":
    if 'new_student' not in st.session_state:
        st.error("Please create a student profile first.")
    else:
        matching_page()

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