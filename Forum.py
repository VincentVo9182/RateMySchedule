# import streamlit as st
# from sidebar import manage_sidebar
# import student

# # Initialize upvote and downvote counts for comments
# upvote_counts = {}
# downvote_counts = {}

# if 'uploaded_title' not in st.session_state:
#     st.session_state.uploaded_title = ""
# if 'uploaded_image' not in st.session_state:
#     st.session_state.uploaded_image = None

# # Sidebar management
# manage_sidebar()

# student = st.session_state.new_student

# # Check if content has been posted
# if 'posted' in st.session_state:
#     # Create an empty container at the top of the page
#     top_container = st.empty()

#     # Display the uploaded title as a string on the main page
#     uploaded_title = st.session_state.uploaded_title
#     top_container.write(f"{uploaded_title}")
    
#     if 'uploaded_images' in st.session_state:
#         for image in st.session_state.uploaded_images:
#             st.image(image, width=300)
#             comment_key = f"comments_{image}"
#             if comment_key not in st.session_state:
#                 st.session_state[comment_key] = []

#             user_comment = st.text_input("Write a comment for this image", key=f"comment_input_{image}")
#             post_comment_button_key = f"post_comment_button_{image}"
#             if st.button("Post Comment", key=post_comment_button_key):
#                 if user_comment:
#                     st.session_state[comment_key].append(user_comment)
#                     user_comment = ""

#             # Display the comments for this image
#             st.subheader("Comments")
#             for comment in st.session_state[comment_key]:
#                 name = student.get_first_name()
#                 major = student.get_major()
#                 year = student.get_classification()
#                 fstring = f'<span style="color: gray; font-weight: bold;">{name}</span> [{major}][{year}]: {comment}'
#                 st.markdown(fstring, unsafe_allow_html=True)
import streamlit as st
from sidebar import manage_sidebar
import student

# Initialize upvote and downvote counts for comments
upvote_counts = {}
downvote_counts = {}

if 'uploaded_title' not in st.session_state:
    st.session_state.uploaded_title = ""
if 'uploaded_image' not in st.session_state:
    st.session_state.uploaded_image = None

# Sidebar management
manage_sidebar()

student = st.session_state.new_student

# Check if content has been posted
if 'posted' in st.session_state:
    # Create an empty container at the top of the page
    top_container = st.empty()

    # Display the uploaded title as a string on the main page
    uploaded_title = st.session_state.uploaded_title
    top_container.write(f"{uploaded_title}")

    if 'uploaded_images' in st.session_state:
        for image in st.session_state.uploaded_images:
            st.image(image, width=300)
            comment_key = f"comments_{image}"
            if comment_key not in st.session_state:
                st.session_state[comment_key] = []

            user_comment = st.text_input("Write a comment for this image", key=f"comment_input_{image}")
            post_comment_button_key = f"post_comment_button_{image}"
            if st.button("Post Comment", key=post_comment_button_key):
                if user_comment:
                    st.session_state[comment_key].append(user_comment)
                    user_comment = ""

            # Display the comments and upvote/downvote buttons for this image
            st.subheader("Comments")
            for comment_id, comment in enumerate(st.session_state[comment_key]):
                upvote_button_key = f"upvote_button_{comment_key}_{comment_id}"
                downvote_button_key = f"downvote_button_{comment_key}_{comment_id}"
                if upvote_button_key not in upvote_counts:
                    upvote_counts[upvote_button_key] = 0
                if downvote_button_key not in downvote_counts:
                    downvote_counts[downvote_button_key] = 0

                name = student.get_first_name()
                major = student.get_major()
                year = student.get_classification()
                fstring = f'<span style="color: gray; font-weight: bold;">{name}</span> [{major}][{year}]: {comment}'
                st.markdown(fstring, unsafe_allow_html=True)

                upvote_count = st.button(f"Upvote ({upvote_counts[upvote_button_key]})", key=upvote_button_key)
                downvote_count = st.button(f"Downvote ({downvote_counts[downvote_button_key]})", key=downvote_button_key)
                
                if upvote_count:
                    upvote_counts[upvote_button_key] += 1
                if downvote_count:
                    downvote_counts[downvote_button_key] += 1