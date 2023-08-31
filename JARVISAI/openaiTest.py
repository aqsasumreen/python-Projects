import openai
openai.api_key = "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"


# Set your OpenAI API key

def ask_jarvis(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose a different engine based on your subscription
        prompt=prompt,
        max_tokens=50  # You can adjust this based on the desired response length
    )
    return response.choices[0].text.strip()

def main():
    print("Hello! I'm your virtual assistant. You can ask me anything.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        prompt = f"You: {user_input}\nJarvis:"
        response = ask_jarvis(prompt)

        print("Jarvis:", response)

if __name__ == "__main__":
    main()
