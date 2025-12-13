# Simple rule-based chatbot

print("Please enter your name to get to know u better")
user_name = input("Enter your name: ").strip().lower()

print("Chatbot: Hello, how are u? I am a simple rule-based chatbot.")
print("Chatbot: You can type 'bye' to exit.\n")

while True:
    user_input = input(f"{user_name}: ").strip().lower()

    # Exit
    if "bye" in user_input:
        print("Chatbot: Thanks, nice meeting u. See u next time.")
        break

    # Greeting
    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello, how are u?")
        if user_name in user_input:
            print(f"Chatbot: Nice meeting u, {user_name}. Let's chat.")

    # Emotion / Response
    elif "fine" in user_input or "good" in user_input:
        print("Chatbot: Nice to hear that.")

    # Name-related questions
    elif "name" in user_input:
        print("Chatbot: Are u asking about my name or your name?")
        
        follow = input(f"{user_name}: ").strip().lower()

        if "my" in follow or "me" in follow:
            print(f"Chatbot: Your name is {user_name}.")
        elif "yours" in follow:
            print("Chatbot: My name is PAL, your simple chatbot.")
        else:
            print("Chatbot: I don't understand.")

    # Asking chatbot's name directly
    elif "yours" in user_input or "your name" in user_input:
        print("Chatbot: U can call me 'PAL'.")

    # Default fallback
    else:
        print("Chatbot: Sorry, I don't understand.")
