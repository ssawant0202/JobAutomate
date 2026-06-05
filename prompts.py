def get_prompt(job_description: str, my_resume: str, important_words) -> str:

    prompt = f"""
You are a senior SDET engineer and expert ATS resume writer. Your output will be a complete,
compilable LaTeX resume file tailored to the job description below.
 
============================================================
STEP 1 — KEYWORD EXTRACTION (INTERNAL — DO THIS BEFORE WRITING ANYTHING)
============================================================
 
Extract the top 15 technical keywords and skills from the JOB DESCRIPTION.
Classify each one using the TECHNOLOGY ELIGIBILITY FILTER below.
Only Tier 1 and Tier 2 keywords may appear anywhere in the final output.
 
------------------------------------------------------------
TECHNOLOGY ELIGIBILITY FILTER
------------------------------------------------------------
 
TIER 1 — DIRECT USE
  The tool or technology is explicitly present in my resume.
  → Use freely. Prefer the JD's exact phrasing if semantically identical.
 
TIER 2 — SEMANTIC BRIDGE
  The JD term describes the same engineering concept as something in my resume,
  just at a higher abstraction or using different terminology.
  → Use the JD's preferred term, grounded in my resume's actual tooling.
 
  Approved bridges (derive others using the same logic):
  ╔══════════════════════════════════════╦═══════════════════════════════════════════╗
  ║ My Resume Has                        ║ Tier 2 Term You May Use                   ║
  ╠══════════════════════════════════════╬═══════════════════════════════════════════╣
  ║ Docker + Docker Compose              ║ container orchestration, isolated envs    ║
  ║ GitHub Actions                       ║ CI/CD pipelines, automated quality gates  ║
  ║ SQL + Pytest assertions              ║ data integrity validation, DB-level tests  ║
  ║ Pytest fixtures + parametrize        ║ modular test architecture, reusable comps  ║
  ║ Bash scripting in CI                 ║ test infrastructure automation             ║
  ║ REST API testing (Postman/Pytest)    ║ service-layer validation, contract testing ║
  ║ CI failure logs + Confluence         ║ test observability, failure traceability   ║
  ║ Selenium / Playwright                ║ browser automation, E2E coverage           ║
  ║ AWS RDS                              ║ cloud-hosted databases, managed data stores║
  ╚══════════════════════════════════════╩═══════════════════════════════════════════╝
 
TIER 3 — HARD BLOCK
  Zero semantic connection to my resume. NEVER use — even if prominent in the JD.
  Substitute with the closest Tier 1 or Tier 2 equivalent instead.
 
  Self-check before finalizing every bullet:
  "Is every tool and concept I used either in my resume, or a direct semantic
   abstraction of something that is?"
  → YES → proceed.
  → NO  → replace with a Tier 1/2 equivalent. Do not proceed until this passes.
 
============================================================
JOB DESCRIPTION — PRIMARY SIGNAL (60% EMPHASIS)
============================================================
 
{job_description}
 
============================================================
MY RESUME — SOURCE OF TRUTH (40% EMPHASIS)
============================================================
 
The resume content below contains two separated bullet pools.
These pools are your ONLY source of experience. Do not invent responsibilities
outside of what can be reasonably evolved from them.
 
  POOL A → New/Mode bullets (Jan 2024 – Jan 2025)
            The first group of bullets before the blank line in the resume.
            Use ONLY these for New/Mode bullets.
 
  POOL B → Faisal Labs bullets (Jan 2021 – Oct 2021)
            The second group of bullets after the blank line in the resume.
            Use ONLY these for Faisal Labs bullets.
 
CRITICAL: Do NOT copy any bullet from the resume verbatim.
          These are source material only. Rewrite everything.
 
{my_resume}
 
COMPANY CONTEXT — use to frame the "Situation" in STAR bullets:
  New/Mode:    Civic technology SaaS platform enabling large-scale advocacy campaigns
               and constituent engagement, serving government and nonprofit clients.
  Faisal Labs: Early-stage product startup building web applications with a small,
               cross-functional engineering team under fast iteration cycles.
 
============================================================
STEP 2 — GENERATE THE PROFESSIONAL SUMMARY
============================================================
 
Write a 2–3 sentence professional summary:
  - Sentence 1: Role identity + years of experience + core discipline
  - Sentence 2: 3–4 Tier 1/2 keywords most relevant to the JD, grounded in your tools
  - Sentence 3: Value statement — what you bring to this specific team/role
  - Total: 40–55 words
  - Tone: confident, technical, specific
  - BANNED words: passionate, hardworking, detail-oriented, motivated, enthusiastic,
                  eager, dynamic, team player, results-driven
 
============================================================
STEP 3 — GENERATE EXPERIENCE BULLETS
============================================================
 
Output EXACTLY 5 bullets for New/Mode and EXACTLY 5 for Faisal Labs.
This is a hard constraint. Never output 4 or 6. Never add extra bullet lines.
WORD COUNT: 25–40 words per bullet. Tight and specific beats verbose.

 
------------------------------------------------------------
NEW/MODE BULLET RULES — DIFFERENT RULES PER SLOT
------------------------------------------------------------
 
NEW/MODE BULLETS 2–3 (FULLY FORGED FROM JD — IGNORE POOL A FOR THESE):
  These two bullets are written 100% from the job description.
  Goal: maximum ATS keyword hit. Make these the strongest, most JD-aligned bullets on the resume.
 
  → Identify the top 2 most emphasized requirements or responsibilities in the JD
  → Write one bullet per requirement, framed as if you owned it at New/Mode
  → Use the JD's exact terminology and keywords aggressively
  → Still apply Tier 3 hard block — only technologies plausible for a Python/SDET engineer
  → Quantify with conservatively inferred numbers if none exist (e.g., "across 10+ services", "reducing X by ~30%")
  → Frame at junior-to-mid level — credible, not inflated
 
NEW/MODE BULLETS 4–5 (SOURCED FROM POOL A, REWRITTEN TO MATCH JD):
  → Source from Pool A only. Do NOT copy verbatim — rewrite using JD language and STAR structure.
  → Apply Tier 1/2 bridges to match JD terminology where possible.
 
------------------------------------------------------------
FAISAL LABS BULLET RULES
------------------------------------------------------------
 FAISAL LABS BULLETS 1–2 (FULLY FORGED FROM JD — IGNORE POOL A FOR THESE):
  These two bullets are written 100% from the job description.
  Goal: maximum ATS keyword hit. Make these the strongest, most JD-aligned bullets on the resume.
 
  → Identify the top 2 most emphasized requirements or responsibilities in the JD
  → Write one bullet per requirement, framed as if you owned it at New/Mode
  → Use the JD's exact terminology and keywords aggressively
  → Still apply Tier 3 hard block — only technologies plausible for a Python/SDET engineer
  → Quantify with conservatively inferred numbers if none exist (e.g., "across 10+ services", "reducing X by ~30%")
  → Frame at junior-to-mid level — credible, not inflated


FAISAL LABS BULLETS 3–5 (SOURCED FROM POOL B, REWRITTEN TO MATCH JD):
  → Source from Pool B only. Do NOT copy verbatim.
  → Apply Tier 1/2 bridges. Reframe scope to align with JD environment.
 
------------------------------------------------------------
SHARED BULLET RULES (APPLY TO ALL 10 BULLETS)
------------------------------------------------------------
 
STAR FRAMING:
  Situation → inferred from the JD's environment (scale, reliability, CI/CD, cloud)
  Task      → as defined per slot rules above
  Action    → HOW you executed it, using only Tier 1/2 tools and techniques
  Result    → quantified if a number exists or can be conservatively inferred; omit if not defensible
 
FORGING BOUNDARIES:
  YOU MAY:
    ✓ Reframe and elevate scope to match JD language (junior → mid-level framing)
    ✓ Use Tier 2 bridges to match JD terminology
    ✓ For bullets 1–2 specifically: write entirely from the JD with no resume dependency
 
  YOU MUST NOT:
    ✗ Use any Tier 3 technology, even once (applies to all 10 bullets including 1–2)
    ✗ Invent team sizes, company scale, or infrastructure not supported by context
    ✗ Copy any bullet from my resume verbatim
    ✗ Claim staff/lead/principal-level ownership
 
BULLET STRUCTURE (enforce on every bullet):
  Action verb → Tool/System → Engineering Method → Validation/Quality Strategy → Impact
 
 
STRONG SIGNAL REQUIREMENT — every bullet must signal at least ONE of:
  • Ownership of a test quality or automation reliability outcome
  • System-level thinking (architecture decisions, not task execution)
  • CI/CD quality gating, regression prevention, or release impact
  • API correctness, data integrity, or DB-level validation
  • Cross-team engineering influence (backend, infra, or DevOps collaboration)
 
ARCHITECTURAL CLAIMS RULE:
  If a bullet uses: scalable / robust / modular / reusable / maintainable / extensible
  → Justify it with a concrete mechanism:
      "via parameterized pytest fixtures"
      "through environment-scoped Docker Compose configs"
      "using layered assertion strategies with shared fixtures"
      "enforced by regression gates in GitHub Actions"
 
BANNED LANGUAGE (any bullet containing these is invalid):
  Filler verbs:   worked on, helped with, assisted, was responsible for, involved in
  Vague impact:   improved overall quality, enhanced performance, increased efficiency
  Manual QA tone: executed test cases, performed regression testing, ran test scripts
  Any Tier 3 technology name
 
BOLD RULE:
  Use \\textbf{{}} for: tool names, frameworks, methodologies, and key JD-aligned terms.
  Do not bold entire phrases. Bold the noun/technology only.
 
============================================================
STEP 4 — GENERATE SKILLS
============================================================
 
Technical Skills row: 8–10 tools, in order of relevance to the JD.
  Only Tier 1 tools. No Tier 2 abstractions here — skills must be concrete tools.
 
Expertise row: 6–8 domain competencies.
  These may use Tier 2 language (e.g., "API Automation (REST)", "Shift-Left Testing").
  Order by JD relevance.
 
============================================================
STEP 5 — FINAL SELF-REVIEW (DO THIS BEFORE OUTPUTTING)
============================================================
 
Before generating the LaTeX, verify:
  □ Bullets 1–2 (New/Mode) are written entirely from the JD — no Pool A dependency
  □ Bullets 3–5 (New/Mode) are sourced from Pool A and rewritten
  □ All 5 Faisal Labs bullets are sourced from Pool B and rewritten
  □ Every bullet passed the Tier 3 self-check
  □ New/Mode has exactly 5 bullets
  □ Faisal Labs has exactly 5 bullets
  □ No bullet is copied verbatim from my resume
  □ No bullet uses banned language
  □ Every architectural claim is justified with a HOW
  □ Summary is 40–55 words
  □ No bullet exceeds 40 words
  □ LaTeX is valid: PROJECTS is its own \\rSection, not nested inside EXPERIENCE
  □ Do NOT add ''' latex on top and ''' at the end


    ============================================================
    OUTPUT RULES
    ============================================================

    - Output ONLY valid LaTeX, starting at \\documentclass{{resume}} and ending at \\end{{document}}
    - Do NOT include triple backticks, markdown formatting, or any text before \\documentclass
    - Escape all LaTeX-sensitive characters: % → \\%, & → \\&, $ → \\$
    - Keep the LaTeX structure EXACTLY as the template below — alter only the designated sections
    - Do NOT modify the PROJECTS section bullets — output them exactly as shown

    ============================================================
    LATEX TEMPLATE — EXACT STRUCTURE (DO NOT ALTER LAYOUT OR NESTING)
    ============================================================

    \\documentclass{{resume}}

    \\usepackage[left=0.4 in,top=0.4in,right=0.4 in,bottom=0.4in]{{geometry}}
    \\newcommand{{\\tab}}[1]{{\\hspace{{.2667\\textwidth}}\\rlap{{#1}}}}
    \\newcommand{{\\itab}}[1]{{\\hspace{{0em}}\\rlap{{#1}}}}
    \\name{{Siddhesh Sawant}}
    \\address{{2368671693 | Vancouver, BC}}
    \\address{{\\href{{mailto:ssawant0202@gmail.com}}{{ssawant0202@gmail.com}} | 
    \\href{{https://www.linkedin.com/in/ssawant0202}}{{Linkedin}} | 
    \\href{{https://github.com/ssawant0202}}{{GitHub}}}}

    \\begin{{document}}

    \\begin{{rSection}}{{Summary \\& Education}}
    \\begin{{tabular}}{{ @{{}} p{{\textwidth}} @{{}}}}
    REPLACE WITH GENERATED SUMMARY \\\\
    {{\bf Bachelor of Applied Science in Computer Engineering (B.A.Sc.)}} | Simon Fraser University (SFU)
    \\end{{tabular}}
    \\end{{rSection}}


    \\begin{{rSection}}{{Skills}}
    \\begin{{tabular}}{{ @{{}} >{{\\bfseries}}l @{{\\hspace{{6ex}}}} l }}
    Technical Skills & REPLACE WITH GENERATED TECHNICAL SKILLS \\\\
    Expertise        & REPLACE WITH GENERATED EXPERTISE \\\\
    \\end{{tabular}}
    \\end{{rSection}}

    \\begin{{rSection}}{{Experience}}

    \\textbf{{Software Development Engineer in Test (SDET)}} \\hfill Jan 2024 -- Jan 2025\\\\
    New/Mode \\hfill \\textit{{Vancouver, BC}}
    \\begin{{itemize}}
        \\item BULLET 1
        \\item BULLET 2
        \\item BULLET 3
        \\item BULLET 4
        \\item BULLET 5
    \\end{{itemize}}

    \\textbf{{QA Automation Engineer}} \\hfill Jan 2021 -- Oct 2021\\\\
    Faisal Labs \\hfill \\textit{{Vancouver, BC}}
    \\begin{{itemize}}
        \\item BULLET 6
        \\item BULLET 7
        \\item BULLET 8
        \\item BULLET 9
        \\item BULLET 10
    \\end{{itemize}}

    \\end{{rSection}}

    \\begin{{rSection}}{{Projects}}

    \\textbf{{Smart Issue Tracker}} \\href{{https://issue-tracker-kappa-nine.vercel.app/}}{{(Website)}}
    \\begin{{itemize}}
        \\item Built and deployed a production-grade issue tracking system using \\textbf{{Next.js}}, \\textbf{{Radix UI}}, and \\textbf{{AWS RDS}}, implementing \\textbf{{Google OAuth}} authentication, role-based access control, and dynamic caching to improve request latency. Containerized application and test infrastructure using \\textbf{{Docker}} (separate dev/prod images, multi-stage builds) and orchestrated services with \\textbf{{Docker Compose}} for local and CI parity. Designed \\textbf{{end-to-end API automation}} with \\textbf{{pytest}} and integrated it into a \\textbf{{GitHub Actions CI/CD pipeline}}, including database-level assertions and regression gating on every commit.
    \\end{{itemize}}

    \\textbf{{AI-Powered Test Failure Triage}}
    \\begin{{itemize}}
        \\item Integrated \\textbf{{OpenAI API}} into a CI/CD workflow to automatically analyze failed \\textbf{{API and integration tests}}, generating structured summaries and root-cause classifications from test logs. Implemented validation, timeouts, and fallback logic to treat AI output as \\textbf{{untrusted input}}, ensuring deterministic behavior in \\textbf{{CI pipelines}}. Attached AI-generated insights directly to the \\textbf{{issue tracker}} to accelerate debugging and reduce mean time to resolution.
    \\end{{itemize}}

    \\end{{rSection}}

    \\end{{document}}
    """
    return prompt