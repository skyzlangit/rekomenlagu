import streamlit as st
from pytube import Search

# Function to search for songs on YouTube using pytube
def search_youtube(query, max_results=5):
    search = Search(query)
    results = search.results[:max_results]
    return results

# App title
st.title("Song Recommendation App")

# Input: User preferences
user_input = st.text_input("Enter a song, artist, or genre you like:")

if user_input:
    # Fetch results from YouTube
    results = search_youtube(user_input, max_results=5)

    if results:
        st.write("### We recommend you listen to:")
        for index, result in enumerate(results, start=1):
            video_url = result.watch_url
            title = result.title
            
            # Handle the views attribute safely
            try:
                views = f"{int(result.views):,} views" if result.views else "Views not available"
            except (TypeError, ValueError):
                views = "Views not available"

            # Handle the publication date safely
            published = result.publish_date.strftime('%Y-%m-%d') if result.publish_date else "Date not available"
            
            st.write(f"**{index}. {title}**")
            st.write(f"*Views: {views} | Published on: {published}*")
            st.video(video_url)
    else:
        st.write("No results found. Try a different input.")
