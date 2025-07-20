import streamlit as st
import requests

# Streamlit UI
st.set_page_config(page_title="Local AI Chatbot", layout="centered")
st.title("🤖 Local AI Chatbot with Ollama")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:", key="input")

# Display past messages
for msg in st.session_state.messages:
    st.markdown(f"**{msg['role'].capitalize()}**: {msg['content']}")

# Handle input
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Send to Ollama API (localhost)
    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "mistral",  # You can change model name (e.g., llama3, codellama, etc.)
                "messages": st.session_state.messages,
                "stream": False
            }
        )
        bot_reply = response.json()["message"]["content"]
    except Exception as e:
        bot_reply = f"Error talking to Ollama: {e}"

    # Add bot response to chat
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.experimental_rerun()
