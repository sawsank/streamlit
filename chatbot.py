import streamlit as st
import nltk
import re

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

# Function to clean user input
def clean_text(text):
    return word_tokenize(re.sub(r'[^\w\s]', '', text.lower()))

# Function to determine word type
def get_word_type(word):
    tag = nltk.pos_tag([word])[0][1]
    if tag.startswith('NN'):
        return 'noun'
    elif tag.startswith('PRP') or tag.startswith('PRP$'):
        return 'pronoun'
    elif tag.startswith('VB'):
        return 'verb'
    return None

# Function to generate chatbot response
def respond(user_input):
    cleaned_input = clean_text(user_input)
    word_types = [get_word_type(token) for token in cleaned_input]

    if any(token in ["hi", "hello"] for token in cleaned_input):
        return "Hello there!"
    
    if "bye" in cleaned_input:
        return "Goodbye! Have a great day! 👋"

    nouns = [token for token, wt in zip(cleaned_input, word_types) if wt == 'noun']
    if nouns:
        return f"I don't know much about {nouns[0]}. Can you help me understand it?"

    pv_words = [token for token, wt in zip(cleaned_input, word_types) if wt in ('pronoun', 'verb')]
    if pv_words:
        return f"I would like to know more about {pv_words[0]}."

    return "I'm still learning. Tell me more!"

# Streamlit UI
st.title("🤖 Simple Chatbot")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input text box
user_input = st.text_input("You:", "")

# Process user input
if st.button("Send") and user_input:
    response = respond(user_input)
    
    # Append conversation to history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Chatbot", response))

    # Display goodbye message and stop interaction
    if "bye" in user_input.lower():
        st.subheader("Chatbot: Goodbye! Have a great day! 👋")
        st.stop()

# Display chat history
st.subheader("Chat History:")
for role, text in st.session_state.chat_history:
    st.write(f"**{role}:** {text}")
