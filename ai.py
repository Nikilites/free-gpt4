from g4f.client import Client

client = Client()

while True:
    input_user = input("Message: ")

    if input_user.lower() == 'exit':
        break  

    # server request
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": input_user}],
        # here you can put other parameters if you need to
    )

    print("AI:", response.choices[0].message.content)
