import streamlit as st
import Student

# Initialize dict1 using st.session_state
if 'dict1' not in st.session_state:
    st.session_state.dict1 = {}

# Initialize optedIn as an empty list
if 'optedIn' not in st.session_state:
    st.session_state.optedIn = []

def matching_page():
    st.title("Buddy Finder")
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
    student = st.session_state.new_student
    if student.get_eid() == "":
        st.error("Please create a student profile first.")
    else:
        matching_page()