from openai import OpenAI
import os

from dotenv import load_dotenv, find_dotenv
import prompts 
import system_prompt


# load the file 
_ = load_dotenv(find_dotenv())

client = OpenAI(
    api_key=os.environ.get('OPEN_API_KEY'),
)
# Get the prompt dynamically from prompt.py
#user_prompt = prompts.get_prompt(job_description, my_resume)
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
            "content": "Can you describe a technical challenge or project you worked on in the past year that you are particularly proud of? What made it significant to you, and what impact did it have on the team or the project? write about my automated chess board project"
        }
    ]
)
print("-------------------------------------")
print( completion.choices[0].message.content)
print("-------------------------------------")
