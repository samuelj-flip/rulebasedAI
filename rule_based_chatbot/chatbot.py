# A simple rule based chatbot

print("Chatbot: Hi I am simple chatbot, Type 'bye' to exit the chat!")
while True:
    user_input = input("You: ").lower()
    if user_input == "hello":
        print("Chatbot: Hello! how are you?")
    elif user_input == "how are you?":
        print("Chatbot: I am just a program, but I am doing well, Thank you")
    elif user_input == "bye":
        print("Chatbot: Goodbye")
        break
    else:
        print("Chatbot: Sorry Don't understand what u mean")