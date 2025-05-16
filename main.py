import streamlit as st
from few_short import FewshotPosts
from post_generator import generate_post

length_language = ["short", "medium", "long"]
language = ["English", "Hinglish"]


def main():
    st.title("Linkedin Post Generator!")

    col1, col2, col3 = st.columns(3)
    fs = FewshotPosts()

    with col1:
        selected_tags = st.selectbox("Title", options=fs.get_tags())

    with col2:
        selected_length = st.selectbox("Length", options=length_language)

    with col3:
        selected_language = st.selectbox("Language", options=language)


    if st.button("Generate Post"):
        post = generate_post(selected_length, selected_language, selected_tags)
        st.write(post)   
             
        # posts = fs.get_filtered_posts(selected_length, selected_language, [selected_tags])
        # if posts:
        #     st.subheader("Here’s a matching LinkedIn post:")
        #     st.write(posts[0]['text'])  # Show the first matched post
        # else:
        #     st.warning("No posts found matching your selection.")


if __name__ == "__main__":
    main()
