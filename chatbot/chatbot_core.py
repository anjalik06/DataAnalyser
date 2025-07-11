INTENTS = {
    "greeting": {
        "examples": ["hello", "hi", "hey", "good morning", "good evening"],
        "response": "Hello! How can I help you today?"
    },
    "name": {
        "examples": ["what's your name", "who are you", "your name"],
        "response": "I'm your friendly  Chatbot."
    },
    "bye": {
        "examples": ["bye", "goodbye", "see you"],
        "response": "See you soon. Take care!"
    },
    "thanks": {
        "examples": ["thank you", "thanks"],
        "response": "You're welcome!"
    },
    "help": {
        "examples": ["help", "can you help me", "assist me"],
        "response": "Sure! What do you need help with?"
    },
    
}

def get_bot_response(user_input):
    user_input = user_input.lower()

    for intent, data in INTENTS.items():
        for phrase in data["examples"]:
            if phrase in user_input:
                return data["response"]

    return "Hmm... I’m not sure how to answer that. Try something else?"
