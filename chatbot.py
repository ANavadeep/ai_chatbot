import nltk
import random
import string
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey 👋"]
    ],
    [
        r"what is your name ?",
        ["I am an AI Chatbot created by a CSE student 😄"]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?"]
    ],
    [
        r"what can you do ?",
        ["I can chat with you and answer basic questions."]
    ],
    [
        r"quit",
        ["Bye! Take care 👋"]
    ],
]

def chatbot():
    print("🤖 AI Chatbot: Hello! Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()