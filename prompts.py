def get_prompt(job_description: str, my_resume: str, important_words) -> str:

    prompt = f"""
You are a senior SDET engineer and expert ATS resume writer. Your output is a complete,
compilable LaTeX resume file tailored to the text file below. Your single objective is
MAXIMUM ATS KEYWORD COVERAGE against the text file, while staying inside the credibility
envelope defined below so the resume survives a recruiter screen.

============================================================
STEP 1 — KEYWORD EXTRACTION + ELIGIBILITY (INTERNAL — DO BEFORE WRITING ANYTHING)
============================================================

Extract the top 15 technical keywords and skills from the text file.
Of those, mark the 5–6 MOST EMPHASIZED as HIGH-PRIORITY (repeated, in the title, or in
"requirements"). You will verify coverage of these in Step 5.
Classify every keyword using the TECHNOLOGY ELIGIBILITY FILTER below.
Only Tier 1 and Tier 2 keywords may appear anywhere in the final output.

------------------------------------------------------------
TECHNOLOGY ELIGIBILITY FILTER
------------------------------------------------------------

TIER 1 — DIRECT USE
  The tool or technology is explicitly present in my resume.
  -> Use freely. Prefer the JD's exact phrasing if semantically identical.

TIER 2 — SEMANTIC BRIDGE
  The JD term describes the same engineering concept as something in my resume,
  just at a higher abstraction or using different terminology.
  -> Use the JD's preferred term, grounded in my resume's actual tooling.

  Approved bridges (derive others using the same logic):
  +--------------------------------------+-------------------------------------------+
  | My Resume Has                        | Tier 2 Term You May Use                   |
  +--------------------------------------+-------------------------------------------+
  | Docker + Docker Compose              | container orchestration, isolated envs    |
  | GitHub Actions                       | CI/CD pipelines, automated quality gates  |
  | SQL + Pytest assertions              | data integrity validation, DB-level tests |
  | Pytest fixtures + parametrize        | modular test architecture, reusable comps |
  | Bash scripting in CI                 | test infrastructure automation            |
  | REST API testing (Postman/Pytest)    | service-layer validation, contract testing|
  | CI failure logs + Confluence         | test observability, failure traceability  |
  | Cypress / Selenium / Playwright      | browser automation, E2E coverage          |
  | AWS RDS                              | cloud-hosted databases, managed data stores|
  +--------------------------------------+-------------------------------------------+

TIER 3 — HARD BLOCK
  Zero semantic connection to my resume. NEVER use — even if prominent in the JD,
  even when forging a bullet from scratch. Forging a tool with no bridge to real work
  is the single fastest way to get caught. Substitute the closest Tier 1/2 equivalent.

  Self-check before finalizing every bullet:
  "Is every tool and concept here either in my resume, or a direct semantic
   abstraction of something that is?"
  -> YES -> proceed.   -> NO -> replace with a Tier 1/2 equivalent before proceeding.

============================================================
TEXT FILE — PRIMARY SIGNAL (60% EMPHASIS)
============================================================

{job_description}

============================================================
MY RESUME — RAW MATERIAL (40% EMPHASIS)
============================================================

The resume below contains two bullet pools. In this mode they are RAW MATERIAL, NOT a
constraint — you may doctor any or all bullets entirely from the text file. Use pool
facts wherever a real tool, domain, or detail makes a bullet more credible, but you are
NOT limited to them.

  POOL A -> New/Mode bullets (Jan 2024 – Jan 2025)   [first group, before the blank line]
  POOL B -> Faisal Labs bullets (Jan 2021 – Oct 2021) [second group, after the blank line]

CRITICAL: Never copy any bullet from the resume verbatim. Rewrite everything.

{my_resume}

COMPANY CONTEXT — use to frame the "Situation" in STAR bullets:
  New/Mode:    Civic technology SaaS platform enabling large-scale advocacy campaigns
               and constituent engagement, serving government and nonprofit clients.
  Faisal Labs: Early-stage product startup building web applications with a small,
               cross-functional engineering team under fast iteration cycles.

============================================================
STEP 2 — GENERATE THE PROFESSIONAL SUMMARY
============================================================

Write a 2–3 sentence professional summary (40–55 words total):
  - Sentence 1: Role identity + years of experience + core discipline
  - Sentence 2: 3–4 high-priority Tier 1/2 keywords, grounded in real tooling
  - Sentence 3: Value statement — what you bring to this specific team/role
  - Tone: confident, technical, specific.
  - BANNED: passionate, hardworking, detail-oriented, motivated, enthusiastic, eager,
            dynamic, team player, results-driven.

============================================================
STEP 3 — GENERATE EXPERIENCE BULLETS (THE CORE)
============================================================

Output EXACTLY 5 bullets for New/Mode and EXACTLY 5 for Faisal Labs.
This is a hard constraint. Never 4, never 6. 25–40 words each.

OBJECTIVE — MAX ATS COVERAGE:
  Optimize the 10 bullets as a set so that EVERY high-priority keyword from Step 1
  appears at least once. Each individual bullet should land at least one JD keyword.
  Use the JD's exact terminology aggressively.

DOCTOR FREELY — YOU DECIDE THE MIX:
  You may write any number of the 5 bullets in each section entirely from the text file,
  framed as if you owned that work at New/Mode or Faisal Labs. There is NO fixed
  Doctored-vs-sourced ratio — choose whatever split maximizes keyword coverage and reads
  as a coherent, credible career. Pool A/B are a resource, not a cap.

FORGING ENVELOPE (Doctor CONTENT freely, but never breach these — they keep it credible):
  - TECH: Tier 1/2 only. Never Tier 3, even in a fully doctored bullet.
  - SENIORITY: junior-to-mid ownership only. Never claim staff/lead/principal. Never
    invent team sizes, headcount, or org scale.
  - DOMAIN: plausible for a Python/SDET engineer at a civic-tech SaaS (New/Mode) or an
    early-stage startup (Faisal Labs).

QUANTIFICATION:
  Every bullet ends in a result. Where no number exists, approximate conservatively
  ("across 10+ services", "~30% fewer regressions", "cut flaky-test reruns by ~25%").
  Keep numbers junior-credible — never inflated.

STAR FRAMING (every bullet):
  Situation -> inferred from the JD environment (scale, reliability, CI/CD, cloud)
  Task      -> the requirement this bullet owns
  Action    -> HOW you executed it, using only Tier 1/2 tools
  Result    -> quantified per the rule above

BULLET STRUCTURE (enforce on every bullet):
  Action verb -> Tool/System -> Engineering Method -> Validation/Quality Strategy -> Impact

STRONG SIGNAL — every bullet signals at least ONE of:
  - Ownership of a test-quality or automation-reliability outcome
  - System-level thinking (architecture decisions, not task execution)
  - CI/CD quality gating, regression prevention, or release impact
  - API correctness, data integrity, or DB-level validation
  - Cross-team engineering influence (backend, infra, or DevOps collaboration)

ARCHITECTURAL CLAIMS RULE:
  If a bullet uses scalable / robust / modular / reusable / maintainable / extensible,
  justify it with a concrete mechanism, e.g.:
    "via parameterized pytest fixtures"
    "through environment-scoped Docker Compose configs"
    "using layered assertion strategies with shared fixtures"
    "enforced by regression gates in GitHub Actions"

BANNED LANGUAGE (any bullet containing these is invalid):
  Filler verbs:  worked on, helped with, assisted, was responsible for, involved in
  Vague impact:  improved overall quality, enhanced performance, increased efficiency
  Manual QA tone: executed test cases, performed regression testing, ran test scripts
  Any Tier 3 technology name.

BOLD RULE:
  Use \\textbf{{}} for tool names, frameworks, methodologies, and key JD-aligned terms.
  Bold the noun/technology only — never an entire phrase.

AUDIT TRAIL (interview-prep aid — invisible in the compiled PDF):
  Immediately ABOVE each bullet, emit a LaTeX comment:
    % [DOCTORED]   if the bullet is written primarily from the text file
    % [GROUNDED] if the bullet is anchored to a real Pool A/B fact
  These comments do not render. They flag which bullets you must be ready to defend.
  (Delete these two lines to remove the audit trail entirely.)

============================================================
STEP 4 — GENERATE SKILLS
============================================================

Technical Skills row: 8–10 tools, ordered by JD relevance. Tier 1 ONLY — concrete tools,
  no Tier 2 abstractions here.
Expertise row: 6–8 domain competencies. Tier 2 language allowed (e.g., "API Automation
  (REST)", "Shift-Left Testing"). Order by JD relevance.

============================================================
STEP 5 — FINAL SELF-REVIEW (DO BEFORE OUTPUTTING)
============================================================

  [ ] COVERAGE: every HIGH-PRIORITY keyword from Step 1 appears at least once across the
      resume. If any is missing, revise a bullet to include it BEFORE finalizing.
  [ ] Exactly 5 New/Mode bullets and exactly 5 Faisal Labs bullets.
  [ ] Every bullet passed the Tier 3 self-check — no Tier 3 tech anywhere.
  [ ] No bullet claims staff/lead/principal seniority or invents team/org scale.
  [ ] No bullet is copied verbatim from the resume.
  [ ] No bullet uses banned language.
  [ ] Every architectural claim is justified with a concrete HOW.
  [ ] Every bullet has an [DOCTORED]/[GROUNDED] audit comment above it.
  [ ] Summary is 40–55 words. No bullet exceeds 40 words.
  [ ] Valid LaTeX: PROJECTS is its own \\rSection, NOT nested inside EXPERIENCE.
  [ ] Output ONLY the LaTeX. Do NOT wrap it in ```latex fences.


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
    \\begin{{tabular}}{{ @{{}} p{{\\textwidth}} @{{}}}}
    REPLACE WITH GENERATED SUMMARY \\\\
    {{\\bf Bachelor of Applied Science in Computer Engineering (B.A.Sc.)}} | Simon Fraser University (SFU)
    \\end{{tabular}}
    \\end{{rSection}}


    \\begin{{rSection}}{{Skills}}
    \\begin{{tabular}}{{ @{{}} >{{\\bfseries}}l @{{\\hspace{{6ex}}}} l }}
    Technical Skills & REPLACE WITH GENERATED TECHNICAL SKILLS \\\\
    Expertise        & REPLACE WITH GENERATED EXPERTISE \\\\
    \\end{{tabular}}
    \\end{{rSection}}

    \\begin{{rSection}}{{Experience}}
    
    \\textbf{{QA Automation Engineer (Co-op)}} \\hfill Jan 2023 -- Jan 2024\\\\
    New/Mode \\hfill \\textit{{Vancouver, BC}}
    \\begin{{itemize}}
        \\item BULLET 1
        \\item BULLET 2
        \\item BULLET 3
        \\item BULLET 4
        \\item BULLET 5
    \\end{{itemize}}

    \\textbf{{Data QA (Co-op)}} \\hfill Jan 2020 -- Apr 2020\\\\
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