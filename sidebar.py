import streamlit as st

# Sidebar management
def manage_sidebar():
    st.sidebar.title("Sidebar")

    # Create text input for title in the sidebar
    uploaded_title = st.sidebar.text_input("Upload Title")

    # Create file uploader for multiple images in the sidebar
    uploaded_images = st.sidebar.file_uploader("Upload Images", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    uploaded_title = st.sidebar.text_input("Image Title")
    
    # Check if images have been uploaded and store them in the session state
    if uploaded_images:
        st.session_state.uploaded_title = uploaded_title
        st.session_state.uploaded_images = uploaded_images

    # Create a "Post" button in the sidebar
    if st.sidebar.button("Post"):
        # Perform actions when the "Post" button is clicked
        st.session_state.posted = True  # Indicate that the content has been posted

    # Display the UT logo in the sidebar
    st.sidebar.image("UT_Logo.png")
