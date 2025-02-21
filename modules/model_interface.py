import openai
import os
from dotenv import load_dotenv
 
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
 
def query_model(prompt: str) -> str:
    """
    Send the user prompt to the OpenAI API and return the response.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return response['choices'][0]['message']['content'].strip()