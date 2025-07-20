import random


responses = {
    "greetings": ["hey", "sup", "yo", "hi"],
    "whats_up": ["nothin much", "chillin", "same old", "this and that"],
    "questions": ["idk", "maybe", "could be", "ask again"],
    "goodbyes": ["later", "peace", "cya", "bye"]
}

def get_response(user_input):
    user_input = user_input.lower()
    
    if user_input in ["hi", "hello", "hey", "sup", "yo"]:
        return random.choice(responses["greetings"])
    elif user_input in ["what's up", "wassup", "whats up"]:
        return random.choice(responses["whats_up"])
    elif user_input.endswith("?"):
        return random.choice(responses["questions"])
    elif user_input in ["bye", "goodbye", "later"]:
        return random.choice(responses["goodbyes"])
    else:
        return random.choice(responses["whats_up"])


print("Bot: hey")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot:", random.choice(responses["goodbyes"]))
        break
    print("Bot:", get_response(user_input))