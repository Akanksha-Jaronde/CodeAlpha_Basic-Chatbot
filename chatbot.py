# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()   # convert input to lowercase for matching
    
    if user_input in ["hello", "hi", "hey"]:
        return "Hi! 👋"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm fine, thanks! How about you?"
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a great day! 👋"
    else:
        return "Sorry, I don't understand that. 🤔"

def run_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        
        if user_input.lower() in ["bye", "goodbye", "see you"]:
            break

# Run chatbot
if __name__ == "__main__":
    run_chatbot()
