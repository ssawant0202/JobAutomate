def load_tex_file(tex_path):
    with open(tex_path, "r", encoding="utf-8") as file:
        tex_content = file.read()
    
    escaped_latex = tex_content.replace("\\", "\\\\")
    # Wrap LaTeX in verbatim for correct formatting
    #formatted_tex = f"\\begin{{verbatim}}\n{tex_content}\n\\end{{verbatim}}"
    return escaped_latex

# Load LaTeX resume
latex_resume = load_tex_file("resumebk.txt")
with open("formatted_resume.txt", "w", encoding="utf-8") as file:
    file.write(latex_resume)

