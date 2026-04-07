import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"));

conversation_history = []

print("Claude chatbot")
print("-" * 40)

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Claude: Goodbye")
        break

    conversation_history.append({
        "role":"user",
        "content": user_input
    })

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system = "You are a helpful assistant called Claude.",
        messages=conversation_history

    )

    reply = response.content[0].text


    conversation_history.append({
        "role": "assistant",
        "content":reply
    })

    print(f"Claude: {reply}")
    print()
