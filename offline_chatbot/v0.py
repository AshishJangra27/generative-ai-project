import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "Who are you?"}
    ]
)

print(response["message"]["content"])
