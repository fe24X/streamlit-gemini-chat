import streamlit as st
import google.generativeai as genai
from nlu import get_intent # <-- Import the new function

# Configure the Gemini API with the key from secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# ... (rest of your streamlit setup) ...

# Get user input
if prompt := st.chat_input("What is up?"):
    # ... (display user message) ...

    # --- MODIFIED: Call the NLU function ---
    nlu_data = get_intent(prompt)
    
    # Display the structured NLU output
    with st.chat_message("assistant"):
        st.write("NLU Output:")
        st.json(nlu_data)
    
    # ... (add to session state) ...