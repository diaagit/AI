def chatbot():
    print("🤖 Welcome to ElectroBot - Your Online Electronics Assistant!")
    print("Type 'help' to see what I can do or 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == "exit":
            print("🤖 ElectroBot: Thank you for chatting with us. Have a great day!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("🤖 ElectroBot: Hello! How can I help you today?")
        elif "help" in user_input:
            print("🤖 ElectroBot: I can help you with:")
            print(" - Order status (e.g., 'track my order')")
            print(" - Product info (e.g., 'tell me about laptops')")
            print(" - FAQs (e.g., 'return policy', 'warranty')")
        elif "track" in user_input and "order" in user_input:
            print("🤖 ElectroBot: Please provide your order ID to check the status.")
        elif "laptop" in user_input:
            print("🤖 ElectroBot: We have a wide range of laptops from HP, Dell, and Lenovo.")
            print("You can ask specifically about 'HP laptop', 'Dell laptop', or 'Lenovo laptop'.")
        elif "hp laptop" in user_input:
            print("🤖 ElectroBot: HP offers a variety of laptops including:")
            print(" - 💼 HP Pavilion: Great for students and daily use.")
            print(" - ⚡ HP Omen: High-performance for gaming and heavy tasks.")
            print(" - 🧳 HP Envy: Sleek design with premium features.")
            print("Price Range: ₹40,000 to ₹1,20,000 based on model and configuration.")
            print("Would you like links to the latest HP laptops or compare models?")
        elif "return" in user_input:
            print("🤖 ElectroBot: Our return policy allows returns within 10 days of delivery. Want to initiate a return?")
        elif "warranty" in user_input:
            print("🤖 ElectroBot: Most electronics come with a 1-year manufacturer warranty. Specific details are on the product page.")
        else:
            print("🤖 ElectroBot: I'm sorry, I didn't understand that. Type 'help' to see what I can do.")

if __name__ == "__main__":
    chatbot()
