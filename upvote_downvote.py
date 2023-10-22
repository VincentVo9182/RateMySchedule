# Define a dictionary to store comments and their upvote/downvote counts
comments_data = {}

def upvote_comment(comment_id):
    if comment_id in comments_data:
        comments_data[comment_id]["upvotes"] += 1

def downvote_comment(comment_id):
    if comment_id in comments_data:
        comments_data[comment_id]["downvotes"] += 1

def add_comment(comment_text):
    comment_id = len(comments_data) + 1
    comments_data[comment_id] = {"text": comment_text, "upvotes": 0, "downvotes": 0}