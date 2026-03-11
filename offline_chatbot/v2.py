import streamlit as st
import ollama
import json
import os

CHAT_FILE = "chats.json"

# Load chats
def load_chats():
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "r") as f:
            return json.load(f)
    return {}


# Save chats
def save_chats(chats):
    with open(CHAT_FILE, "w") as f:
        json.dump(chats, f)


# Initialize session state
if "chats" not in st.session_state:
    st.session_state.chats = load_chats()

if "current_chat" not in st.session_state:
    if st.session_state.chats:
        st.session_state.current_chat = list(st.session_state.chats.keys())[0]
    else:
        st.session_state.current_chat = "chat1"
        st.session_state.chats["chat1"] = []


# Sidebar - Chat list
st.sidebar.title("Chats")

for chat_id in st.session_state.chats.keys():
    if st.sidebar.button(chat_id):
        st.session_state.current_chat = chat_id


# New chat button
if st.sidebar.button("New Chat"):
    new_chat = f"chat{len(st.session_state.chats)+1}"
    st.session_state.chats[new_chat] = []
    st.session_state.current_chat = new_chat
    save_chats(st.session_state.chats)


st.title("Local Chatbot")


messages = st.session_state.chats[st.session_state.current_chat]


# Display messages
for msg in messages:
    st.chat_message(msg["role"]).write(msg["content"])


# Chat input
prompt = st.chat_input("Ask something...")

if prompt:
    messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = ollama.chat(model="llama3.2", messages=messages)
    reply = response["message"]["content"]

    messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)

    save_chats(st.session_state.chats)