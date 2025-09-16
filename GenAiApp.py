import streamlit as st
import google.generativeai as genai

# Configure the Gemini API with the key from secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest",
                              generation_config=generation_config)

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get model response
    convo = model.start_chat(history=[])
    convo.send_message(prompt)
    response = convo.last.text
    
    # Display model response
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add model response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})