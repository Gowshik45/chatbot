from transformers import pipeline

print("Loading model... (first run takes 1–2 minutes)")

chatbot = pipeline(
    "text-generation",
    model="microsoft/DialoGPT-medium"
)

print("Chatbot started. Type 'exit' to quit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    result = chatbot(user_input, max_length=200)

    print("Bot:", result[0]["generated_text"])
