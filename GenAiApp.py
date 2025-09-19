import streamlit as st
import google.generativeai as genai
from nlu import get_intent
import json

# --- Configuration ---
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# --- Session State Initialization ---
# This ensures the 'messages' list is always available.
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Helper Function to handle button clicks ---
# This function will be called when a feedback button is clicked.
def handle_feedback(message_index, is_correct):
    """
    Updates the chat history based on user feedback.
    """
    # Get the original NLU data from the message that is being reviewed.
    nlu_data = st.session_state.messages[message_index]["content"]

    # Remove the message that contains the feedback buttons.
    st.session_state.messages.pop(message_index)

    if is_correct:
        # If correct, add a confirmation message to the chat history.
        st.session_state.messages.append({
            "role": "assistant",
            "content": f"Great! I've confirmed the following:\n```json\n{json.dumps(nlu_data, indent=2)}\n```",
            "type": "text"
        })
    else:
        # If incorrect, add a message asking the user to try again.
        st.session_state.messages.append({
            "role": "assistant",
            "content": "My apologies for the misunderstanding. Could you please rephrase your request?",
            "type": "text"
        })

# --- Display Chat History (This now runs every time) ---
# Loop through all stored messages and display them.
for index, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        # If it's a regular text message, just display it.
        if message.get("type", "text") == "text":
            st.markdown(message["content"])

        # If it's an NLU response waiting for feedback, display it with buttons.
        elif message.get("type") == "nlu_feedback":
            st.write("I understood the following. Is this correct?")
            st.json(message["content"])
            col1, col2 = st.columns(2)
            with col1:
                # When "Correct" is clicked, call the helper function.
                # The 'key' is crucial to make sure each button is unique.
                if st.button("Correct", key=f"correct_{index}"):
                    handle_feedback(index, is_correct=True)
                    st.rerun() # Rerun the script immediately to show the update.
            with col2:
                # When "Incorrect" is clicked, call the helper function.
                if st.button("Incorrect", key=f"incorrect_{index}"):
                    handle_feedback(index, is_correct=False)
                    st.rerun() # Rerun the script immediately.


# --- Handle New User Input ---
# This part only runs when the user types a new message.
if prompt := st.chat_input("What is up?"):
    # Add user's message to history and display it.
    st.session_state.messages.append({"role": "user", "content": prompt, "type": "text"})
    
    # Get the NLU interpretation from your function.
    nlu_data = get_intent(prompt)
    
    # Add the NLU response to history. We give it a special 'type'
    # so our display loop knows to add feedback buttons.
    st.session_state.messages.append({
        "role": "assistant",
        "content": nlu_data,
        "type": "nlu_feedback"
    })
    
    # Rerun the app to display the new message with its feedback buttons.
    st.rerun()