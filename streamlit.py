import openai

openai.api_key = "your-api-key-here"

def get_explanation(question: str) -> str:
    messages = [
        {"role": "system", "content": "You are a friendly tutor who explains things to middle school kids using simple words and fun examples."},
        {"role": "user", "content": question}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )

    return response['choices'][0]['message']['content']
