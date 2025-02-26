from openai import OpenAI
import os

from dotenv import load_dotenv, find_dotenv
import prompts 
import system_prompt


def generate_latex_code(job_description: str, my_resume: str) -> str:
    # load the file 
    _ = load_dotenv(find_dotenv())

    client = OpenAI(
        api_key=os.environ.get('OPEN_API_KEY'),
    )
    # Get the prompt dynamically from prompt.py
    user_prompt = prompts.get_prompt(job_description, my_resume)
    sys_prompt = system_prompt.get_prompt()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system", 
                "content": sys_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )
    return completion.choices[0].message.content
