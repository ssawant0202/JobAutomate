import descriptionscrapper
import openAItest
import os, time ,sys

from openai import OpenAI
import os

from dotenv import load_dotenv, find_dotenv
import prompts 
import keywords_prompts
import system_prompt


def integrate_important_words_into_resume(job_description ):
        # load the file 
    _ = load_dotenv(find_dotenv())
    parent_dir = "/Users/siddheshsawant/Documents/JobApplications/AutomatedPDFs"
    resume_dir = "/Users/siddheshsawant/Projects/JobAutomate"

    client = OpenAI(
        api_key=os.environ.get('OPEN_API_KEY'),
    )
    # Get the prompt dynamically from prompt.py
    sys_prompt = system_prompt.get_prompt(job_description)
    keyword_prompt = keywords_prompts.get_prompt(job_description)

    key_words_completion = client.chat.completions.create(
        model="gpt-4-turbo",
        # model="gpt-5.2",


        messages=[
            {
                "role": "system", 
                "content": sys_prompt
            },
            {
                "role": "user",
                "content": keyword_prompt
            }
        ]
    )
    important_words  = key_words_completion.choices[0].message.content

    # Validate resume directory
    if not os.path.isdir(resume_dir):
        raise ValueError(f"Invalid resume_dir: {resume_dir}")

    # Base resume path
    base_resume_path = os.path.join(resume_dir, "my_resume_base.txt")

    if not os.path.exists(base_resume_path):
        raise FileNotFoundError(f"Base resume not found: {base_resume_path}")

    # Read base resume
    with open(base_resume_path, "r", encoding="utf-8") as file:
        my_resume_base = file.read().rstrip()

    # Output resume path
    modified_resume_path = os.path.join(resume_dir, "my_resume.txt")

    # Compose final resume
    final_resume = (
        my_resume_base
        + "\n\n"
        + "my_resume_keywords:\n"
        + important_words
        + "\n"
    )

    # Write (overwrite if exists)
    with open(modified_resume_path, "w", encoding="utf-8") as file:
        file.write(final_resume)


    return important_words
     


def get_latex_code():
    # Define the parent directory
    if sys.platform == "darwin":
        parent_dir = "/Users/siddheshsawant/Documents/JobApplications/AutomatedPDFs"
        resume_dir = "/Users/siddheshsawant/Projects/JobAutomate"
    elif sys.platform == "win32":
        parent_dir = r"\\192.168.5.3\JobApplications\AutomatedPDFs"  # Change to your desired path
        resume_dir = r"\\192.168.5.3\JobApplications"
    else:
        raise RuntimeError("Unsupported OS")
    
   
    # Loop through all subdirectories in AutomatedPDFs
    for folder in os.listdir(parent_dir):
        if folder == ".DS_Store":  # Ignore .DS_Store
            continue
        folder_path = os.path.join(parent_dir, folder)  # Full path to subfolder
        
        if os.path.isdir(folder_path):  # Ensure it's a directory
            job_des_path = os.path.join(folder_path, "jobDescription.txt")  # Path to job description
            if os.path.exists(job_des_path):  # Ensure job_description.txt exists
                with open(job_des_path, "r", encoding="utf-8") as file:
                    job_description = file.read()  # Read content

        #integrate imp words into my resume 
        important_words = integrate_important_words_into_resume(job_description)

         #Get Resume
        if os.path.isdir(resume_dir):  # Ensure it's a directory
                job_resume_path = os.path.join(resume_dir, "my_resume.txt")  
        if os.path.exists(job_resume_path):  
                    with open(job_resume_path, "r", encoding="utf-8") as file:
                        my_resume = file.read()  # Read content

        latex_file_path = os.path.join(folder_path, "latex_code.txt")
        # Check if the file already exists
        if not os.path.exists(latex_file_path):
            latex_code = openAItest.generate_latex_code(job_description, my_resume, important_words)
            if latex_code:
                print(f"✅ Got Latex Code for: {folder}")
            latex_file_path = os.path.join(folder_path, "latex_code.txt")
            with open(latex_file_path, "w", encoding="utf-8") as file:
                file.write(latex_code)

        else:
            print(f"⚠️ Skipping {folder} - LaTeX file already exists.")
    print("-----✅ All Resumes Code Generated!-----")
    




if __name__ == "__main__":
    #Get the job description from linkedin and generate text file contaning the job description
    descriptionscrapper.generate_description_files()
    get_latex_code()

    


