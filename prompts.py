def get_prompt(job_description: str, my_resume: str , important_words:str) -> str:
    
    prompt = f"""

Based on the following job description and my resume experience, generate high-quality .tex file an output example is provided and make sure the bullet points are also optimize and in LaTeX format.
Each bullet point should:
- Replace the important_words:{important_words} and the stack they might use with the current significant words in my resume whereable applicable
- From {important_words}, find all technical skills, soft skills and speciality and replace with the current section
- Use a STAR approach (Situation, Task, Action, Result) to generate 4 points for each experience section
- Be concise (About 60 words per bullet point).
- Bold important keywords exactly as provided, using LaTeX's \\textbf{{}} syntax.
- Use compelling action verbs and quantify results where possible.
- Align with the responsibilities outlined in the job description.
Each bullet point should use a STAR-style structure, and replace the current keywords to match the job description, be concise (max 50 words), and bold key skills and keywords exactly as provided. For Projects section keep the STAR-style structure point be concise (min 75 words)
According to the job description rewrite my bullet points to make it 80% ATS compliant (Similar words found in the job description). Use my previous responses only as a reference. Make sure to output the updated bullet points of projects and experience in the Latex code example provided below.
Focus on the company's values and integrate it with my resume for action verbs or just in general
Just the Latex code nothing else because Im using the ouput to compile the code into a pdf. 3 Generated bullet points and 1 Original provided in the formatting.


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
Technical Skills & Python, JAVA, REST APIs, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill* \\\\   
Soft Skills & *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*\\\\   
Expertise & *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill*, *Insert Skill* 
\\end{{tabular}}
\\end{{rSection}}

\\begin{{rSection}}{{EXPERIENCE}}

\\textbf{{Software Development Intern}} \\hfill Jan 2023 - Jan 2024\\\\
New/Mode \\hfill \\textit{{Vancouver, BC}}

\\begin{{itemize}}
    \\item * Insert Chat GPT Generated Bullet point 1  *
    \\item * Insert Chat GPT Generated Bullet point 2  *
    \\item Improved regression testing suites by writing \\textbf{{Unit Tests in Cypress}}, to optimize deployment time from 2 days to 4 hours and increasing system efficiency in an \\textbf{{Agile environment.}}
    \\item * Insert Chat GPT Generated Bullet point 3  *
\\end{{itemize}}

\\textbf{{Software Development Intern}} \\hfill Jan 2021 - Aug 2021\\\\
Faisal Labs \\hfill \\textit{{Vancouver, BC}}

\\begin{{itemize}}
    \\item * Insert Chat GPT Generated Bullet point 4  *
    \\item * Insert Chat GPT Generated Bullet point 5  *
    \\item Collaborated with data scientists to innovate  \\textbf{{data segmentation}} techniques on CT, MRI, and retina scans \\textbf{{enhancing machine learning model accuracy by 10%}} through efficient data processing pipelines.
    \\item * Insert Chat GPT Generated Bullet point 6  *
\\end{{itemize}}

\\begin{{rSection}}{{PROJECTS}}

\\textbf{{Smart Issue Tracker}} \\href{{https://issue-tracker-kappa-nine.vercel.app/}}{{(Website)}}
\\begin{{itemize}}
    \\item Developed an issue tracker using \\textbf{{Next.js}}, \\textbf{{Radix UI}}, and \\textbf{{AWS RDS}}, achieving \\textbf{{8\\% speed improvement}} through \\textbf{{dynamic caching}}. Integrated \\textbf{{Google Authentication}} and \\textbf{{secure URL access}} for \\textbf{{data security}}. Deployed on \\textbf{{Vercel}}.
\\end{{itemize}}

\\textbf{{Automated Chessboard}} \\href{{https://youtu.be/hdualDzNvGY}}{{(Video Demo)}}
\\begin{{itemize}}
    \\item \\textbf{{Led a team of six}} to develop an \\textbf{{automated chessboard}} leveraging Python and the \\textbf{{Lichess API}} with \\textbf{{OAuthbased}} login. Designed and built the system, including UI for game initialization and detailed circuitry for seamless physical and digital gameplay integration.
\\end{{itemize}}

\\end{{rSection}}

\\begin{{rSection}}{{Certifications}}
\\begin{{itemize}}
   \\item \\textbf{{AWS}} Certified Solutions Architect - Associate, \\textbf{{Data Structures and Algorithms}}, \\textbf{{SQL}} Mastery
\\end{{itemize}}
\\end{{rSection}}

\\begin{{rSection}}{{Leadership}}
\\begin{{itemize}}
   \\item \\textbf{{Founded}} a university \\textbf{{table tennis group}}, \\textbf{{organizing}} multiple \\textbf{{events}} that brought together many table tennis enthusiasts, \\textbf{{creating}} an \\textbf{{engaging community for players}} of all skill levels.

\\end{{itemize}}


\\end{{rSection}}
\\end{{rSection}}
\\end{{document}}


### OUTPUT FORMAT ###
Use The exact same  LaTeX format resume just update the \\items (bullet points) nothing else so that the over structure remains the same.
please do not add '```latex' above \\documentclass{{resume}} and '```' below \\end{{document}}
if there is & or % sign in bullet points make sure to add backslash before it ex R\\&D

Now, generate the bullet points in LaTeX format based on the above job description with matching keywords.
"""
    return prompt

