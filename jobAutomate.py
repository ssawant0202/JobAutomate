import descriptionscrapper
import openAItest
import os, time ,sys
def get_latex_code():
    # Define the parent directory
    if sys.platform == "darwin":
        parent_dir = "/Users/siddheshsawant/Documents/JobApplications/AutomatedPDFs"
        resume_dir = "/Users/siddheshsawant/Documents/JobApplications"
    elif sys.platform == "win32":
        parent_dir = r"\\192.168.5.3\JobApplications\AutomatedPDFs"  # Change to your desired path
        resume_dir = r"\\192.168.5.3\JobApplications"
    else:
        raise RuntimeError("Unsupported OS")
    
    #Get Resume
    if os.path.isdir(resume_dir):  # Ensure it's a directory
            job_resume_path = os.path.join(resume_dir, "my_resume.txt")  # Path to job description
    if os.path.exists(job_resume_path):  # Ensure job_description.txt exists
                with open(job_resume_path, "r", encoding="utf-8") as file:
                    my_resume = file.read()  # Read content
    # Loop through all subdirectories in AutomatedPDFs
    for folder in os.listdir(parent_dir):
        if folder == ".DS_Store":  # Ignore .DS_Store
            continue
        folder_path = os.path.join(parent_dir, folder)  # Full path to subfolder
        
        if os.path.isdir(folder_path):  # Ensure it's a directory
            job_des_path = os.path.join(folder_path, "jobDescription.txt")  # Path to job description
            if os.path.exists(job_des_path):  # Ensure job_description.txt exists
                with open(job_des_path, "r", encoding="utf-8") as file:
                    job_description = file.read()  # Read content

        latex_file_path = os.path.join(folder_path, "latex_code.txt")
        # Check if the file already exists
        if not os.path.exists(latex_file_path):
            latex_code = openAItest.generate_latex_code(job_description, my_resume)
            if latex_code:
                print(f"✅ Got Latex Code for: {folder}")
            latex_file_path = os.path.join(folder_path, "latex_code.txt")
            with open(latex_file_path, "w", encoding="utf-8") as file:
                file.write(latex_code)

        else:
            print(f"⚠️ Skipping {folder} - LaTeX file already exists.")
    print("-----✅ All Resumes Code Generated!-----")
    




if __name__ == "__main__":
    #Get the job description from linkedin and generate text file contaning the job description
    # descriptionscrapper.generate_description_files()
    get_latex_code()


