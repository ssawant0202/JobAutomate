def get_prompt(job_description: str, my_resume: str) -> str:
    
    prompt = f"""
You are an expert resume writer with over 20 years of experience helping job seekers land software engineering/developer roles.
Based on the following job description and my resume experience, generate high-quality .tex file an output example is provided and make sure the bullet points are also optimize and in LaTeX format.
Each bullet point should:
- Use a STAR approach (Situation, Task, Action, Result).
- Be concise (maximum 50 words per bullet point).
- Bold important keywords exactly as provided, using LaTeX's \\textbf{{}} syntax.
- Use compelling action verbs and quantify results where possible.
- Align with the responsibilities outlined in the job description.
Each bullet point should use a STAR-style structure, be concise (max 50 words), and bold key skills and keywords exactly as provided.
Do not make up any drastic information changes but add the significant and important software/technologies used in my resume; mainly use what is in the provided resume experience. Make sure to output the updated bullet points of projects and experience in the Latex code example provided below.
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
\\\\newcommand{{\\itab}}[1]{{\\hspace{{0em}}\\rlap{{#1}}}}
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
    \\item Led a team of 2 to automate \\textbf{{CI/CD workflows}} integrated with \\textbf{{Git}} and \\textbf{{Docker}}, catching \\textbf{{20\\% more errors}} pre-deployment and saving \\textbf{{10+ hours weekly}}
    \\item Improved regression testing by writing \\textbf{{Unit Tests}} in \\textbf{{Cypress}}, optimizing \\textbf{{deployment time from 2 days to 4 hours}}.
    \\item Designed \\textbf{{scalable and distributed systems}} using \\textbf{{Docker}} and \\textbf{{Kubernetes}}, improving infrastructure efficiency.
\\end{{itemize}}

\\textbf{{Software Development Intern}} \\hfill Jan 2021 - Jan 2021\\\\
Faisal Labs \\hfill \\textit{{Vancouver, BC}}
\\begin{{itemize}}
    \\item Collaborated with \\textbf{{data scientists}} to innovate \\textbf{{data segmentation techniques}} on \\textbf{{CT, MRI, and retina scans}}, increasing model accuracy by \\textbf{{10\\%}}.
    \\item Engaged in \\textbf{{team collaboration}} during Agile meetings to refine \\textbf{{user requirements}}, ensuring high-quality software delivery.
    \\item Researched distributed algorithms and implemented findings, \\textbf{{leading a team of 3}} to improve model accuracy by \\textbf{{15\\%}}.
\\end{{itemize}}

\\end{{rSection}}

\\begin{{rSection}}{{PROJECTS}}

\\item \\textbf{{Smart Issue Tracker}} \\href{{https://issue-tracker-kappa-nine.vercel.app/}}{{(Website)}}
\\begin{{itemize}}
    \\item Developed an issue tracker using \\textbf{{Next.js}}, \\textbf{{Radix UI}}, and \\textbf{{AWS RDS}}, achieving \\textbf{{8\\% speed improvement}} through \\textbf{{dynamic caching}}. Integrated \\textbf{{Google Authentication}} and \\textbf{{secure URL access}} for \\textbf{{data security}}. Deployed on \\textbf{{Vercel}}.
\\end{{itemize}}

\\item \\textbf{{Automated Chessboard}} \\href{{https://youtu.be/hdualDzNvGY}}{{(Video Demo)}}
\\begin{{itemize}}
    \\item \\textbf{{Led a team of six}} to develop an \\textbf{{automated chessboard}} using \\textbf{{Python}} and the \\textbf{{Lichess API}}. Designed the system, UI, and hardware for seamless gameplay integration.
\\end{{itemize}}

\\end{{rSection}}

\\begin{{rSection}}{{Leadership}}
\\begin{{itemize}}
    \\item Demonstrated \\textbf{{self-motivation}} by completing \\textbf{{Data Structures and Algorithms (DSA)}} courses, \\textbf{{SQL training}}, and self-learning \\textbf{{JavaScript}} and \\textbf{{React}}.
\\end{{itemize}}
\\end{{rSection}}

\\end{{document}}


### OUTPUT FORMAT ###
Use The exact same  LaTeX format resume just update the \\items (bullet points) nothing else so that the over structure remains the same.
please do not add '```latex' above \\documentclass{{resume}} and '```' below \\end{{document}}

Now, generate the bullet points in LaTeX format based on the above job description and resume experience.
"""
    return prompt

