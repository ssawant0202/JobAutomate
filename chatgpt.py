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
sys_prompt = "You're an expert Software engineer with 20+ years of experience in development and interviewing fresh graduates"#system_prompt.get_prompt()
usr_prompt = f""""
is it benefical to use star format bullet points or to make sure you provide maximum number of technical words in the bullet points. My worry is 
star format describes a story with less technical key words and more technical words bullet points is less star format like

"""
completion = client.chat.completions.create(
    # model="gpt-4-turbo",
    model="gpt-5.2",
    
    messages=[
        {
            "role": "system", 
            "content": sys_prompt
        },
        {
            "role": "user",
            "content": usr_prompt }
    ]
)
print("-------------------------------------")
print( completion.choices[0].message.content)
print("-------------------------------------")
