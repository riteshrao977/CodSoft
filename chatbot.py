# Predefined rules and responses that is being used by Bot to answer the users.
predefined_rules = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi! How can I help you today?",
    "what is your name?": "I'm Vamp, your friendly chatbot!",
    "what is your name": "I'm Vamp, your friendly chatbot!",
    "how are you": "I'm doing great, thanks! How about you?",
    "how are you?": "I'm doing great, thanks! How about you?",
    "good bye": "See you later! Have a great day!",
    "default": "I didn't understand that. Can you please rephrase?"
}

def chatbot(user_input):
    # Convert the user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Check if the user input matches any of the predefined rules
    for i in predefined_rules:
        if i in user_input:
            return predefined_rules[i]
    
    # If no rule matches, return the default response
    return predefined_rules["default"]

# Test the chatbot
while True:
    user_input = input("Human: ")
    response = chatbot(user_input)
    print("Bot: ", response)