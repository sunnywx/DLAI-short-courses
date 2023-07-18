import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # load local .env, auto search parent dir

"""check env loaded"""
# print("openai key %s" % os.getenv('OPENAI_API_KEY'))

openai.api_key = os.getenv("OPENAI_API_KEY")

"""
see: https://platform.openai.com/docs/models/gpt-3-5
"""


def get_completion(prompt, system_prompt="", model='gpt-3.5-turbo', temperature=0, max_tokens=4096):
    messages = [
        {'role': 'user', 'content': prompt},
        {'role': 'system', 'content': system_prompt},
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        # max_tokens=max_tokens
    )
    content = response.choices[0].message['content']
    # token_dict = response['usage']
    return content
