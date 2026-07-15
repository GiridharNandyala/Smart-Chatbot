import streamlit as st
from google import genai
from google.genai import types

# 1. Page Config
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 My Smart Chatbot")

# 2. Set your Google API Key (Starting with AQ.)
# Paste your 'AQ.' key here without any spaces
MY_GOOGLE_KEY = ""

# 3. Initialize Google GenAI Client
@st.cache_resource
def get_genai_client(api_key):
    return genai.Client(api_key=api_key)

try:
    client = get_genai_client(MY_GOOGLE_KEY)
except Exception as e:
    st.error(f"Client Initialization Error: {e}")

# 4. Chat History Setup for Streamlit UI
if "ui_messages" not in st.session_state:
    st.session_state.ui_messages = []

if "chat_session" not in st.session_state:
    # Setting up the system instruction
    config = types.GenerateContentConfig(
        system_instruction="You are a helpful assistant.",
        temperature=0.7
    )
    # Starting a new chat session using a stable model name
    st.session_state.chat_session = client.chats.create(
        model="gemini-3.5-flash",
        config=config
    )

# 5. Display Past Messages
for message in st.session_state.ui_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. User Input Loop
if user_input := st.chat_input("Type your message here..."):
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.ui_messages.append({"role": "user", "content": user_input})

    # Show assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Sending message directly through the Google chat session
                response = st.session_state.chat_session.send_message(user_input)
                response_text = response.text
            except Exception as e:
                response_text = f"Error: {str(e)}\n\nPlease check if the API key is active or has sufficient credits."
            
            st.markdown(response_text)
            
    st.session_state.ui_messages.append({"role": "assistant", "content": response_text})