def get_prompt(job_description: str) -> str:
    
    prompt = f"""
    Given my job description: {job_description}. Analyze the job description.
    - Fetch the job title
    - Make a list of 8-10 tech stack keywords mainly from the job description's Responsibilities and Qualifications section that will make my resume atleast 80% ATS compliant.
    

"""
    return prompt

