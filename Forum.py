import streamlit as st

# Define CSS styles
header_style = """
    background-color: #E65100;
    color: white;
    font-size: 24px;
    padding: 10px;
    text-align: center;
    font-weight: bold;
"""

post_title_style = """
    font-size: 20px;
    font-weight: bold;
"""

post_style = """
    background-color: #f2f2f2;
    border: 1px solid #ddd;
    border-radius: 10px;
    margin: 10px 0;
    padding: 20px;
"""

rating_style = """
    font-size: 20px;
    font-weight: bold;
"""

comment_header_style = """
    font-size: 18px;
    font-weight: bold;
"""

comment_style = """
    font-size: 14px;
"""

section_style = """
    margin: 20px;
    padding: 20px;
    background-color: #f0f0f0;
    border: 1px solid #ddd;
    border-radius: 10px;
"""

divider = """
    text-align: center
"""

def Forum_page():
    # Initialize a list to store user posts
    if 'user_posts' not in st.session_state:
        st.session_state.user_posts = []

    # Sidebar portion, allow the user to make a post
    st.sidebar.title("Post your Schedule")

    uploaded_title = st.sidebar.text_input("Post Title (Don't forget to include your major and year!)")
    uploaded_image = st.sidebar.file_uploader("Upload your Class Schedule (jpg, png, or pdf please!)", type=["jpg", "png", "jpeg", "pdf"])

    if st.sidebar.button("Post"):
        if uploaded_image:
            post = {
                "title": uploaded_title,
                "image": uploaded_image,
                "rating": 0,
                "comments": [],
            }
            st.session_state.user_posts.insert(0, post)  # Insert the post at the beginning of the list

    # Main page portion
    # Header with styling
    st.markdown("<div style='" + header_style + "'>RateMySchedule Forum</div>", unsafe_allow_html=True)
    st.write("")
    # Display the user posts in reverse order (most recent first)
    for i, post in enumerate(st.session_state.user_posts):
        post_id = f"post_{i}"
        comments_key = f"comments_{post_id}"

        st.markdown(f"<div style='{post_title_style}'>{post['title']}</div>", unsafe_allow_html=True)
        st.write("")
        st.image(post["image"], use_column_width=True, caption="Uploaded Schedule")
        
        # Create buttons for upvoting and downvoting to update post rating
        post_upvote_button_key = f"post_upvote_button_{i}"
        if st.button(f"Upvote", key=post_upvote_button_key) and post["rating"] < 1:
            post["rating"] += 1


        post_downvote_button_key = f"post_downvote_button_{i}"
        if st.button(f"Downvote", key=post_downvote_button_key) and post["rating"] > -1:
            post["rating"] -= 1

        st.markdown(f"<div style='{rating_style}'>Post Rating: {post['rating']}</div>", unsafe_allow_html=True)

        # Display comments under the post
        st.markdown("<div style='" + comment_header_style + "'>Comments</div>", unsafe_allow_html=True)
        for comment in post["comments"]:
            st.markdown(f"<div style='{comment_style}'>{comment}</div>", unsafe_allow_html=True)
                                     
        if 'new_student' not in st.session_state:
            st.error("Please create a student profile before you can comment.")
        # Text input for posting comments
        else:
            user_comment = st.text_input("Write a comment for this post", key=comments_key)
            post_comment_button_key = f"post_comment_button_{i}"

            if st.button(f"Post Comment", key=post_comment_button_key):
                if user_comment:
                    post["comments"].append(st.session_state.new_student.get_first_name() + " [" +
                                                                   st.session_state.new_student.get_major() + "][" + 
                                                                   st.session_state.new_student.get_classification() + "]: " + 
                                                                   user_comment)
                    user_comment = ""  # Clear the input field after posting
                st.experimental_rerun()   
        st.markdown("<div style='" + divider + "'>______________________________________________________________________________</div>", unsafe_allow_html=True)
        st.write("")

if __name__ == "__main__":
    Forum_page()

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