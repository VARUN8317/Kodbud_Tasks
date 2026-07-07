def chatbot():
    print("Welcome to the Simple Chatbot!")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ")
        user = user.lower()

        if user == "hello":
            print("Bot: Hi!")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: My name is Python Chatbot.")

        elif user == "who created you":
            print("Bot: I was created using Python.")

        elif user == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Start the chatbot
chatbot()