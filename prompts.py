def get_prompt(job_description: str, my_resume: str , important_words:str) -> str:
    
    prompt = f"""
You are an expert ATS-focused resume writer specializing in SDET, Backend, and Platform/Cloud-adjacent roles.

Your task is to rewrite my resume so that it strongly aligns with the target job description while remaining
defensible, realistic, and grounded in my actual experience.
Based on the following job description and my resume, generate a high-quality LaTeX `.tex` file containing highly ATS-optimized with high keyword recall and semantic alignment bullet points that emphasize **how** value was delivered — not just what was done.

------------------------------------------------------------
JOB DESCRIPTION (PRIMARY SIGNAL – 80% EMPHASIS):
{job_description}

------------------------------------------------------------
RESUME EXPERIENCE (SOURCE OF TRUTH – 20% EMPHASIS):
{my_resume}

------------------------------------------------------------
IMPORTANT WORDS & SKILLS (FROM JD):
{important_words}

------------------------------------------------------------
**Instructions for Bullet Points:**
OBJECTIVE:

Generate a high-quality LaTeX `.tex` resume that is:
- ATS-optimized with high keyword recall and semantic alignment
- Framed primarily through the job description’s priorities and system context
- Executed using my resume’s actual tools, workflows, and scope

Think of this as:
→ “What I did, described as if it were performed in a system like the JD describes.”

CONTROLLED FORGING RULES (READ CAREFULLY):

- You MAY lightly extend or generalize responsibilities to better match the job description,
  BUT ONLY if they are a reasonable evolution of what appears in my resume.
- You MUST NOT invent:
  • entirely new tech stacks
  • unrelated domains
  • senior-level ownership I could not plausibly defend
- Any added responsibility must be explainable as:
  “I didn’t own this end-to-end, but I meaningfully contributed to it.”

If a JD requirement is only partially supported by my resume:
- Emphasize overlap
- Abstract responsibility upward (system-level phrasing)
- DO NOT fabricate deep ownership

BULLET REWRITE RULES (STAR-BASED, JD-FRAMED):

Rewrite bullets using the STAR method with this emphasis:
- Situation: inferred from the JOB DESCRIPTION’s environment (scale, reliability, CI/CD, cloud, etc.)
- Task: mapped from my resume responsibilities
- Action: HOW I executed the task, using tools and techniques present in my resume
- Result: quantified where possible, otherwise conservatively inferred

ALIGNMENT STRATEGY:
- Target ~60% JD language and priorities, ~40% resume execution details
- Prefer JD terminology when semantically equivalent to resume terms
- Reframe existing work to highlight:
  • system reliability
  • automation impact
  • CI/CD integration
  • debugging and performance considerations

KEYWORD STRATEGY:

- Aggressively incorporate {important_words} into bullet points and skills
- Replace keywords ONLY with semantically equivalent concepts already present or implied in my resume
- Avoid raw keyword stuffing; prioritize natural technical phrasing

OUTPUT REQUIREMENTS:
- Generate exactly 5 rewritten bullets per experience.
- Generate Skills matching to the job description and fill in *Insert Skill* in Skills section 
- Each bullet must explain HOW the result was achieved (tools, techniques, design decisions).
- Use concrete technical language (APIs, CI/CD, Docker, SQL, pytest, etc.) ONLY if present in resume.
- Quantify results ONLY if numbers already exist or can be conservatively inferred.
- Each bullet: 25–30 words.
- Use LaTeX bold syntax for important technologies: \\textbf{{example}}.
- Avoid generic phrases like “worked on”, “responsible for”, “involved in”.

### Output Requirements:
- Output only valid LaTeX from `\\documentclass{{resume}}` to `\\end{{document}}`
- Do **not** include any Markdown like triple backticks (```).
- Escape all LaTeX-sensitive characters (`%`, `&`, '$' etc.) with a backslash.
- Keep the LaTeX structure **exactly the same** as the provided example.
- Replace only the `\\item` bullet point text.


------------------------------------------------------------

------------------------------------------------------------
**Output Format (Example):**


\\documentclass{{resume}} % Use the custom resume.cls style

\\usepackage[left=0.4 in,top=0.4in,right=0.4 in,bottom=0.4in]{{geometry}}
\\newcommand{{\\tab}}[1]{{\\hspace{{.2667\\textwidth}}\\rlap{{#1}}}}
\\newcommand{{\\itab}}[1]{{\\hspace{{0em}}\\rlap{{#1}}}}
\\name{{Siddhesh Sawant}}
\\address{{+1(236) 867-1693 \\\\ Vancouver, BC}}
\\address{{\\href{{mailto:ssawant0202@gmail.com}}{{ssawant0202@gmail.com}}\\\\ 
\\href{{https://www.linkedin.com/in/ssawant0202/}}{{linkedin.com}} \\\\ 
\\href{{https://ssawant.netlify.app/}}{{Portfolio}}}}

\\begin{{document}}

\\begin{{rSection}}{{Education}}
{{\\bf Bachelor of Computer Engineering}}, Simon Fraser University \\hfill {{October 2024}}\\\\
\\textbf{{Relevant Coursework}}:  DSA, OOP, Web Development, Database, Android, UI/UX, Networking \\& Security, Digital Logic
\\end{{rSection}}

\\begin{{rSection}}{{SKILLS}}
\\begin{{tabular}}{{ @{{}} >{{\\bfseries}}l @{{\\hspace{{6ex}}}} l }}
Technical Skills & *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*,\\\\   
Soft Skills & *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*\\\\   
Expertise & *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*,
\\end{{tabular}}
\\end{{rSection}}

\\begin{{rSection}}{{EXPERIENCE}}

\\textbf{{*Insert Job Title from job description*}} \\hfill Jan 2024 - Jan 2025\\\\
New/Mode \\hfill \\textit{{Vancouver, BC}}

\\begin{{itemize}}
    \\item * Insert Chat GPT Generated Bullet point 1  *
    \\item * Insert Chat GPT Generated Bullet point 2  *
    \\item * Insert Chat GPT Generated Bullet point 3  *
    \\item * Insert Chat GPT Generated Bullet point 4  *
    \\item * Insert Chat GPT Generated Bullet point 5  *

\\end{{itemize}}

\\textbf{{*Insert Job Title from job description*}} \\hfill Jan 2022 - Aug 2022\\\\
Faisal Labs \\hfill \\textit{{Vancouver, BC}}

\\begin{{itemize}}
    \\item * Insert Chat GPT Generated Bullet point 6  *
    \\item * Insert Chat GPT Generated Bullet point 7  *
    \\item * Insert Chat GPT Generated Bullet point 8  *
    \\item * Insert Chat GPT Generated Bullet point 9  *
    \\item * Insert Chat GPT Generated Bullet point 10  *

\\end{{itemize}}

\\begin{{rSection}}{{PROJECTS}}

\\textbf{{Smart Issue Tracker}} \\href{{https://issue-tracker-kappa-nine.vercel.app/}}{{(Website)}}
\\begin{{itemize}}
    \\item Built and deployed a production-grade issue tracking system using \\textbf{{Next.js}}, \\textbf{{Radix UI}}, and \\textbf{{AWS RDS}}, implementing \\textbf{{Google OAuth}} authentication, role-based access control, and dynamic caching to improve request latency.
Containerized application and test infrastructure using \\textbf{{Docker}} (separate dev/prod images, multi-stage builds) and orchestrated services with \\textbf{{Docker Compose}} for local and CI parity.
Designed \\textbf{{end-to-end API automation}} with \\textbf{{pytest}} and integrated it into a \\textbf{{GitHub Actions CI/CD pipeline}}, including database-level assertions and regression gating on every commit.
\\end{{itemize}}

\\textbf{{AI-Powered Test Failure Triage}}
\\begin{{itemize}}

   \\item Integrated \\textbf{{ChatGPT API}} into a CI/CD workflow to automatically analyze failed \\textbf{{API and integration tests}}, generating structured summaries and root-cause classifications from test logs.
    Implemented validation, timeouts, and fallback logic to treat AI output as \\textbf{{untrusted input}}, ensuring deterministic behavior in \\textbf{{CI pipelines}}.
    Attached AI-generated insights directly to the \\textbf{{issue tracker}} to accelerate debugging and reduce mean time to resolution.
\\end{{itemize}}


\\end{{rSection}}

\\end{{rSection}}
\\end{{document}}


### OUTPUT FORMAT ###
Use The exact same  LaTeX format resume just update the \\items (bullet points) nothing else so that the over structure remains the same.
please do not add '```latex' above \\documentclass{{resume}} and '```' below \\end{{document}}
"""
    return prompt

