def get_prompt(job_description: str, my_resume: str) -> str:
    
    prompt = f"""
    Given my job description: {job_description} and my resume: {my_resume}. Analyze the job description.
    Make a list of 6-8 tech stack keywords from the job description that will make my resume atleast 80% ATS compliant.
    Make another list which analyzes what the job description carefully and captures the essense of what is actually required by the applicant. 
    Join both lists and return

"""
    return prompt

