import streamlit as st
from utils import write_message
from agent import generate_response

st.set_page_config("Ebert", page_icon="🎙️")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi, I'm Shaikh Ul Islam Chatbot!  How can I help you?",
        },
    ]


# Submit handler
def handle_submit(message):
    """
    Submit handler:

    You will modify this method to talk with an LLM and provide
    context using data from Neo4j.
    """

    # Handle the response
    with st.spinner("Thinking..."):
        # Call the agent
        response = generate_response(message)
        write_message("assistant", response)


# Display messages in Session State
for message in st.session_state.messages:
    write_message(message["role"], message["content"], save=False)

# Handle any user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    write_message("user", prompt)

    # Generate a response
    handle_submit(prompt)
