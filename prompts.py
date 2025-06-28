def get_prompt(job_description: str, my_resume: str , important_words:str) -> str:
    
    prompt = f"""

Based on the following job description and my resume, generate a high-quality LaTeX `.tex` file containing bullet points that emphasize **how** value was delivered — not just what was done.

------------------------------------------------------------
**Job Description:**
{job_description}

------------------------------------------------------------
**Resume Experience:**
{my_resume}

------------------------------------------------------------
**Important Words & Skills (from JD):**
{important_words}

------------------------------------------------------------
**Instructions for Bullet Points:**

- Rewrite each bullet point using the **STAR method** (Situation, Task, Action, Result).
- **Prioritize the “how”**: Each bullet must explain how the outcome was achieved — the **tools, techniques, technical approaches, design decisions, or problem-solving steps** used.
  - Examples of “how” phrasing to use: “by implementing...”, “through optimizing...”, “using X to solve Y...”, “leveraging A to refactor B...”, etc.
- Include:
  - **Technical depth** — specific stack, libraries, frameworks, optimization techniques, CI/CD tools, data handling approaches, etc.
  - **Concrete action** — what you built, improved, or debugged and how you tackled it.
  - **Quantified results** — latency reduced, costs saved, users onboarded, bugs fixed, etc.
- Replace any keywords in `{important_words}` with matching terms already in my resume when possible.
- For each experience:
  - Generate **3 new bullet points** focused on “how”
  - Keep **1 original bullet point** exactly as-is
- Each bullet must:
  - Be **concise** (60–70 words)
  - Use **bold LaTeX syntax** for important technologies and keywords: \\textbf{{example}}
  - Avoid generic phrases — be specific and technically insightful

### Output Requirements:
- Output only valid LaTeX from `\\documentclass{{resume}}` to `\\end{{document}}`
- Do **not** include any Markdown like triple backticks (```).
- Escape all LaTeX-sensitive characters (`%`, `&`, etc.) with a backslash.
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
\\address{{+1(236) 867-1693 \\\\ Coquitlam, BC}}
\\address{{\\href{{mailto:ssawant0202@gmail.com}}{{ssawant0202@gmail.com}}\\\\ 
\\href{{https://www.linkedin.com/in/ssawant0202/}}{{linkedin.com}} \\\\ 
\\href{{https://ssawant.netlify.app/}}{{Portfolio}}}}

\\begin{{document}}

\\begin{{rSection}}{{Education}}
{{\\bf Bachelor of Computer Engineering}}, Simon Fraser University \\hfill {{October 2024}}\\\\
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
    \\item * Insert Chat GPT Generated Bullet point 3  *
    \\item * Insert Chat GPT Generated Bullet point 4  *
\\end{{itemize}}

\\textbf{{Software Development Intern}} \\hfill Jan 2021 - Aug 2021\\\\
Faisal Labs \\hfill \\textit{{Vancouver, BC}}

\\begin{{itemize}}
    \\item * Insert Chat GPT Generated Bullet point 4  *
    \\item * Insert Chat GPT Generated Bullet point 5  *
    \\item * Insert Chat GPT Generated Bullet point 6  *
    \\item * Insert Chat GPT Generated Bullet point 7  *
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
"""
    return prompt

