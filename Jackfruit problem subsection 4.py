def chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot. Type 'bye' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello there! How are you doing?")

        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing great! How about you?")

        elif "your name" in user_input:
            print("Chatbot: My name is Chatty! What’s yours?")

        elif "weather" in user_input:
            print("Chatbot: I can’t check the weather yet, but it’s always sunny in my code!")

        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a nice day!")
            break

        else:
            print("Chatbot: Sorry, I didn’t understand that. Try something else!")


chatbot()