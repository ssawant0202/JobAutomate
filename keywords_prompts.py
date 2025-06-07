def get_prompt(job_description: str, my_resume: str) -> str:
    
    prompt = f"""
    Given my job description: {job_description} and my resume: {my_resume}. Analyze the job description.
    - Make a list of 6-8 tech stack keywords from the job description that will make my resume atleast 80% ATS compliant.
    - Make another list which analyzes what the job description carefully and captures the essense of what is actually required by the applicant. 
    - There are three sections in my resume at the top as follows, 'Technical Skills', 'Soft Skills' and 'Speciality' according to the job description 
      analyze all the technical skills required and return a list with header 'Technical Skills'
      analyze all the Soft Skills required and return a list with header 'Soft Skills', 
      analyze all the Expertise required and return a list with header 'Expertise', 
    From the job description search the web and linkedin for what software they might use and return that list as well
    Join all lists and return

"""
    return prompt

