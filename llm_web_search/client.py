import streamlit as st
from get_links import get_links
from scrape import scrape_links, initialize_logs
from cleaning import combine_logs
from llm import call_gemini, context_combine_prompt

st.title("AI Web Search & Answer")

# Input for topic
topic = st.text_input("Enter your topic:", placeholder="e.g., latest AI news for today")

if st.button("Get Answer"):
    if topic:
        with st.spinner("Searching and processing..."):
            # Get links
            links = get_links(topic)
            
            # Initialize logs
            log_folder = initialize_logs(topic)
            
            # Scrape content
            scrape_links(links, save_logs=True, log_folder=log_folder)
            
            # Combine logs
            context_from_logs = combine_logs(log_folder)
            
            # Create prompt
            final_prompt = context_combine_prompt(context_from_logs, topic)
            
            # Get answer
            answer = call_gemini(final_prompt)
            
            # Display answer
            st.success("Answer:")
            st.write(answer)
    else:
        st.warning("Please enter a topic first!")
