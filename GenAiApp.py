import streamlit as st
import google.generativeai as genai
from nlu import get_intent

# Configure the Gemini API with the key from secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Set up the model
# NOTE: You can change the model name to your preferred Gemini model  gemini-1.5-pro-latest
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- MODIFIED: Call the NLU function ---
    nlu_data = get_intent(prompt)
    
    # Display the structured NLU output
    with st.chat_message("assistant"):
        st.write("NLU Output:")
        st.json(nlu_data)

    # Get model response
    response = model.generate_content(prompt)

    # Display model response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response.text)
    # Add model response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response.text})