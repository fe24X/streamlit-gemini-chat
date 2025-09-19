import google.generativeai as genai
import json
import streamlit as st
#import os <-- 1. Import the os library
# Configure the Gemini API with the key from secrets

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# --- 2. Configure the API key right after the imports ---

# Configure the Gemini API with the key from secrets

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])


def get_intent(prompt: str) -> dict:
    """
    Takes a user prompt and returns a dictionary with intent and entities.
    """
    # NOTE: Configuration is now handled outside the function.
    model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")
    
    nlu_prompt = f"""
    Your task is to act as an NLU (Natural Language Understanding) service.
    From the user's message, extract the intent and any relevant entities.
    The output should be a JSON object with two keys: "intent" and "entities".
    If you cannot determine an intent, set the intent to "unknown".

    User message: "{prompt}"

    JSON Output:
    """
    
    convo = model.start_chat(history=[])
    convo.send_message(nlu_prompt)
    response_text = convo.last.text

    try:
        json_response_string = response_text.strip().replace("```json", "").replace("```", "")
        return json.loads(json_response_string)
    except json.JSONDecodeError:
        return {
            "intent": "parsing_error",
            "entities": {"raw_response": response_text},
            "user_check_question": "Is the extracted intent and entities correct? If not, please specify the correct ones."
        }


# The rest of your test code remains the same
if __name__ == "__main__":
    test_sentence_1 = "Can you run the sales report for Q3 in the US region"
    test_sentence_2 = "I need to book a meeting with the marketing team for next Friday"
    
    print(f"Testing sentence: '{test_sentence_1}'")
    result_1 = get_intent(test_sentence_1)
    print(json.dumps(result_1, indent=2))
    
    print("\n" + "="*20 + "\n") # Separator
    
    print(f"Testing sentence: '{test_sentence_2}'")
    result_2 = get_intent(test_sentence_2)
    print(json.dumps(result_2, indent=2))