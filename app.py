import streamlit as st
from chatbot.chatbot_core import get_bot_response
import streamlit.components.v1 as components

st.set_page_config(page_title="Web Chatbot", layout="centered")

st.markdown("<h2 style='text-align: center; color: white;'>🤖Chatbot</h2>", unsafe_allow_html=True)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Append new message if available
if "new_user_msg" in st.session_state and st.session_state.new_user_msg:
    user_msg = st.session_state.new_user_msg
    bot_msg = get_bot_response(user_msg)
    st.session_state.chat_history.append(("You", user_msg))
    st.session_state.chat_history.append(("Bot", bot_msg))
    st.session_state.new_user_msg = ""  # Clear after use

# Generate HTML for dark chat UI
chat_html = """
<style>
body {
    background-color: #121212;
}
.chatbox {
    border: 1px solid #333;
    border-radius: 10px;
    padding: 10px;
    height: 400px;
    overflow-y: auto;
    background-color: #1e1e1e;
    color: white;
}
.msg {
    padding: 10px 15px;
    border-radius: 18px;
    margin: 10px;
    max-width: 75%;
    clear: both;
    word-wrap: break-word;
    font-size: 15px;
}
.user {
    background-color: #4a90e2;
    float: right;
    text-align: right;
    color: white;
}
.bot {
    background-color: #2c2c2c;
    float: left;
    text-align: left;
    color: #e0e0e0;
}
</style>
<div class="chatbox" id="chatbox">
"""

# Add messages to HTML
for sender, msg in st.session_state.chat_history:
    role = "user" if sender == "You" else "bot"
    chat_html += f'<div class="msg {role}">{msg}</div>'

# Auto-scroll JS
chat_html += """
</div>
<script>
    var chatbox = document.getElementById('chatbox');
    chatbox.scrollTop = chatbox.scrollHeight;
</script>
"""

# Display chatbox
components.html(chat_html, height=420, scrolling=True)

# Dark mode input form
with st.form("chat_form", clear_on_submit=True):
    st.markdown("""
        <style>
        .stTextInput > div > div > input {
            background-color: #2e2e2e;
            color: white;
            border: 1px solid #555;
        }
        </style>
    """, unsafe_allow_html=True)
    user_input = st.text_input("Message", placeholder="Type your message here...")
    submitted = st.form_submit_button("Send")
    if submitted and user_input.strip():
        st.session_state.new_user_msg = user_input.strip()
        st.rerun()
