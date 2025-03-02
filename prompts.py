def get_prompt(job_description: str, my_resume: str) -> str:
    
    prompt = f"""
Run These two prompts in sequence: 
Prompt 1) 
You are an expert resume writer with over 20 years of experience helping job seekers land software engineering/developer roles.
Analyze the job Description provided below to find max 5 crucial tech stack words (exclude soft skills like colloboration, team player and action verbs). Make sure to integrate these words in my current resume.
**Job Description:**
{job_description}

Prompt 2)
Based on the following job description and my resume experience, generate high-quality .tex file an output example is provided and make sure the bullet points are also optimize and in LaTeX format.
Each bullet point should:
- Use a STAR approach (Situation, Task, Action, Result).
- Be concise (maximum 60 words per bullet point).
- Bold important keywords exactly as provided, using LaTeX's \\textbf{{}} syntax.
- Use compelling action verbs and quantify results where possible.
- Align with the responsibilities outlined in the job description.
Each bullet point should use a STAR-style structure, be concise (max 50 words), and bold key skills and keywords exactly as provided. For Projects section keep the STAR-style structure point be concise (min 75 words)
Integrate the 5 words from above in the job description. Make sure to output the updated bullet points of projects and experience in the Latex code example provided below.
Focus on the company's values and integrate it with my resume for action verbs or just in general
Just the Latex code nothing else because Im using the ouput to compile the code into a pdf. 


------------------------------------------------------------
**Job Description:**
{job_description}

------------------------------------------------------------
**Resume Experience:**
{my_resume}

------------------------------------------------------------
**Output Format (Example):**


\\documentclass{{resume}} % Use the custom resume.cls style

\\usepackage[left=0.4 in,top=0.4in,right=0.4 in,bottom=0.4in]{{geometry}}
\\newcommand{{\\tab}}[1]{{\\hspace{{.2667\\textwidth}}\\rlap{{#1}}}}
\\newcommand{{\\itab}}[1]{{\\hspace{{0em}}\\rlap{{#1}}}}
\\name{{Siddhesh Sawant}}
\\address{{+1(236) 867-1693 \\\\ Coquitlam, BC}}
\\address{{\\href{{mailto:ssawant0202@gmail.com}}{{ssawant0202@gmail.com}}\\\\ 
\\href{{https://www.linkedin.com/in/ssawant0202/}}{{linkedin.com}} \\\\ 
\\href{{https://ssawant.netlify.app/}}{{Portfolio}}}}

\\begin{{document}}

\\begin{{rSection}}{{Education}}
{{\\bf Bachelor of Computer Engineering}}, Simon Fraser University \\hfill {{}}\\\\
\\textbf{{Relevant Coursework}}: DSA, Computer Architecture, Testing, Modular code, Code quality, Computer Science
\\end{{rSection}}

\\begin{{rSection}}{{SKILLS}}
\\begin{{tabular}}{{ @{{}} >{{\\bfseries}}l @{{\\hspace{{6ex}}}} l }}
Technical Skills & NextJS, SSR, REST APIs, C++, MongoDB, Docker, Linux OS, Python, JAVA, JavaScript \\\\
Soft Skills & Communication, Problem solving, Critical thinking, Collaboration, Adaptability \\\\
Specialty & Automated testing, Data structures, Software architecture, Unit testing, Network protocols
\\end{{tabular}}
\\end{{rSection}}

\\begin{{rSection}}{{EXPERIENCE}}

\\textbf{{Software Development Intern}} \\hfill Jan 2023 - Jan 2024\\\\
New/Mode \\hfill \\textit{{Vancouver, BC}}
\\begin{{itemize}}
    \\itemsep -3pt {{}}
    \\item Integrate the new Bullet point 0 with original : "Led a team of 2 to create and automate CI/CD workflows integrated with Git and Docker, catching 20more
    errors pre-deployment and saving 10+ hours weekly in debugging time, ensuring seamless distributed system
    reliability with low cost solutions"

    \\item Bullet point 1 
    \\item Bullet point 2

\\end{{itemize}}

\\textbf{{Software Development Intern}} \\hfill Jan 2021 - Jan 2021\\\\
Faisal Labs \\hfill \\textit{{Vancouver, BC}}
\\begin{{itemize}}
    \\item Integrate the new Bullet point 3 with original : "Collaborated with data scientists to innovate data segmentation techniques on CT, MRI, and retina
    scans enhancing machine learning model accuracy by 10\% through efficient data processing pipelines"
    \\item Bullet point 4
    \\item Bullet point 5

\\end{{rSection}}

\\begin{{rSection}}{{PROJECTS}}

\\textbf{{Smart Issue Tracker}} \\href{{https://issue-tracker-kappa-nine.vercel.app/}}{{(Website)}}
\\begin{{itemize}}
    \\item Developed an issue tracker using \\textbf{{Next.js}}, \\textbf{{Radix UI}}, and \\textbf{{AWS RDS}}, achieving \\textbf{{8\\% speed improvement}} through \\textbf{{dynamic caching}}. Integrated \\textbf{{Google Authentication}} and \\textbf{{secure URL access}} for \\textbf{{data security}}. Deployed on \\textbf{{Vercel}}.
\\end{{itemize}}

\\textbf{{Automated Chessboard}} \\href{{https://youtu.be/hdualDzNvGY}}{{(Video Demo)}}
\\begin{{itemize}}
    \\item \\textbf{{Led a team of six}} to develop an \\textbf{{automated chessboard}} using \\textbf{{Python}} and the \\textbf{{Lichess API}}. Designed the system, UI, and hardware for seamless gameplay integration.
\\end{{itemize}}

\\end{{rSection}}

\\begin{{rSection}}{{Leadership}}
\\begin{{itemize}}
   \\item \\textbf{{Founded}} a university \\textbf{{table tennis group}}, \\textbf{{organizing}} multiple \\textbf{{events}} that brought together many table tennis enthusiasts, \\textbf{{creating}} an \\textbf{{engaging community for players}} of all skill levels.

\\end{{itemize}}
\\end{{rSection}}

\\begin{{rSection}}{{Interests}}
\\begin{{itemize}}
   \\item In my free time I like to play \\textbf{{chess}} and paint \\textbf{{acrylic portraits}}. I've won a couple of trophies in \\textbf{{table tennis}}.
\\end{{itemize}}
\\end{{rSection}}

\\begin{{rSection}}{{Five Most Important Keywords from the job description}}
\\begin{{itemize}}
   \\item Keyword1, Keyword1, Keyword1, Keyword1 
\\end{{itemize}}
\\end{{rSection}}
\\end{{document}}


### OUTPUT FORMAT ###
Use The exact same  LaTeX format resume just update the \\items (bullet points) nothing else so that the over structure remains the same.
please do not add '```latex' above \\documentclass{{resume}} and '```' below \\end{{document}}
if there is & or % sign in bullet points make sure to add backslash before it ex R\\&D

Now, generate the bullet points in LaTeX format based on the above job description and resume experience.
"""
    return prompt

