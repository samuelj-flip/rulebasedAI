# Simple rule based chatbot
"""
Hello how are u I am a simple based chatbot 
follow my instructions

First safe your name to properly communicate properly
second follow the navigation of instructions to proper prompt
"""

print("Please enter your name to get to know u better")
user_name = input("Enter your name: ").lower()
print("Hello, how are u I am a simple rule based chatbot")
while True:
    user_input = input(f"{user_name}: ").lower()
    if "hello" in user_input:
        print("Chatbot: Hello how are u")
        if user_name.lower() in user_input.lower():
            print(f"Chatbot: Hello {user_name} nice meeting, Let's chat")
    elif "fine" in user_input.lower():
        print("Chatbot: Nice to hear that")
    elif "name" in user_input.lower():
        print("Chatbot: What do u mean which name, are u asking about my name or your name")
        if "yes" in user_input.lower() or "my name" in user_input.lower():
            print(f"Chatbot: Okay your name is {user_name}")
    elif "yours" in user_input:
        print("Chatbot: Now I understand you, I am just a simple Chatbot but u can call me 'PAL'")
    elif 'bye' in user_input.lower():
        print("Chatbot: Thanks nice meeting u, see u next")
        break
    else:
        print("Chatbot: sorry I don't understand")
