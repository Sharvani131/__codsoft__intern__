print("AI Chatbot (Type 'bye' to exit)")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello! Nice to meet you.")
    
    elif user == "how are you":
        print("Bot: I am doing great!")

    elif user == "your name":
        print("Bot: I am CodSoft AI Chatbot.")

    elif user == "what can you do":
        print("Bot: I can answer simple questions.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")