def get_prompt(job_description: str) -> str:
    
    prompt = f"""
You are an expert technical recruiter, ATS optimizer, and resume writer.

Given the following job description:

{job_description}

Perform the following tasks:
Return five quality bullet points based on the process.

1. Extract Job Information
- Identify the exact job title.
- Identify the company name (if available).
- Determine the primary role category (e.g., Backend Engineer, Full-Stack Engineer, SDET, QA Engineer, DevOps Engineer, Data Engineer, Embedded Engineer, Mobile Engineer, etc.).
- Summarize the role's main objective in 2-3 sentences.

2. Prioritize Requirements
Analyze the Responsibilities, Requirements, Qualifications, Preferred Qualifications, and Skills sections.

Assign each requirement one of the following priorities:
- Critical (appears in the first few bullet points, repeated multiple times, or appears essential for success in the role)
- Important (frequently mentioned but not core to the role)
- Supporting (helpful but secondary)

Give significantly more weight to:
- The first 30% of responsibility bullets
- Repeated technologies and skills
- Explicitly stated required qualifications
- Technologies directly tied to day-to-day responsibilities


4. Resume Bullet Point Generation
Using the highest-priority ATS keywords, generate 5 highly technical resume bullet points.

Output Format:
Five bullet points in a list.

"""
    return prompt

