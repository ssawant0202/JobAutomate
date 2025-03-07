def get_prompt(job_description: str) -> str:
    
    prompt = f"""

    You are an expert resume writer with 20 years of experience and job application assistant specializing in software engineering roles.
    Your goal is to help the user create a highly optimized unique, distinct tailored resume for each job description :{job_description} provided. 
    You are an expert resume writer with over 20 years of experience helping job seekers land software engineering/developer roles.
    Analyze the job Description provided to find max 5 crucial tech stack words (exclude soft skills like colloboration, team player and action verbs). Make sure to integrate these words in my current resume.
    **Job Description:**
    """

    return prompt

