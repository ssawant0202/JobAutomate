import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from webdriver_manager.chrome import ChromeDriverManager

import time, os, sys
from bs4 import BeautifulSoup
import re
#google email: jobautomate@jobautomate.iam.gserviceaccount.com
# Path to ChromeDriver (Update as needed)
def generate_description_files():
    chrome_driver_path = ChromeDriverManager().install()#"/opt/homebrew/bin/chromedriver"  # Update this if necessary
    service = Service(chrome_driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in the background
    options.add_argument("--disable-gpu")  # Prevents GPU issues
    options.add_argument("--no-sandbox")  # Helps prevent permission issues (especially in Linux)
    options.add_argument("--disable-dev-shm-usage")  # Reduces memory issues


    # Initialize WebDriver for Chrome
    driver = webdriver.Chrome(service=service, options=options)

    # -------------------- 1️⃣ Google Sheets Setup --------------------
    sheet_id = '1T6xyQlTDDglARwiYaPaSKmZnfrqS1rcJTcmsgusWsMs'
    # Define scope and authorize credentials.json
    #scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

    scope = ['https://www.googleapis.com/auth/spreadsheets']
    credentials = Credentials.from_service_account_file('credentials.json', scopes = scope)
    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()
    if sys.platform == "darwin":
        parent_dir = "/Users/siddheshsawant/Documents/JobApplications/AutomatedPDFs"  # Change to your desired path
    elif sys.platform == "win32":
        parent_dir = r"E:\Applications 2024\AutomatedPDFs"  # Change to your desired path
    else:
        raise RuntimeError("Unsupported OS")

    # List of folders to create
    # folders = ["Project1", "Project2"]
    sheet_read = sheet.values().get(spreadsheetId = sheet_id, range = 'A2:B4').execute()
    values = sheet_read.get('values', [])
    folders = [row[0] for row in values if row]  # Avoids empty rows

    if not values or len(values[0]) < 2:
        print("❌ Error: Not enough data in Google Sheets. Ensure A2:A8 has folder names and B2:B8 has job URLs.")
        exit()

    for index, link in enumerate(values):
        # Specify the LinkedIn job URL (Replace this with your job link)
        # job_url = "https://www.linkedin.com/jobs/search/?currentJobId=4158058797&distance=100&f_TPR=r604800&geoId=103366113&keywords=software%20developer&origin=JOB_SEARCH_PAGE_QUERY_EXPANSION"  # Replace with a real job link
        # print(link[0])
        # break
        retry_attempts = 3  # Set the number of retries
        for attempt in range(retry_attempts): 
            try:
                # ✅ Start a new WebDriver instance for each job
                folder_path = os.path.join(parent_dir, folders[index])
                os.makedirs(folder_path, exist_ok=True)  # Avoids errors if folder exists
                # ✅ Define the correct file path inside the folder
                filename = os.path.join(folder_path, "jobDescription.txt")
                if os.path.exists(filename):
                    print(f"⚠️ Skipping {folders[index]} - Description already exists.")
                    break
                service = Service(chrome_driver_path)
                options = webdriver.ChromeOptions()
                options.add_argument("--headless")  # Run Chrome in the background
                options.add_argument("--disable-gpu")  # Prevents GPU issues
                options.add_argument("--no-sandbox")  # Helps prevent permission issues (especially in Linux)
                options.add_argument("--disable-dev-shm-usage")  # Reduces memory issues

                # Initialize WebDriver for Chrome
                driver = webdriver.Chrome(service=service, options=options)

                # ✅ Add a small delay to reduce rate-limiting
                time.sleep(3 + random.uniform(0, 2))

                driver.get(link[1])
                # Wait for job description to load
                wait = WebDriverWait(driver, 10)
                wait.until(EC.presence_of_element_located((By.CLASS_NAME, "show-more-less-html__markup")))

                # Extract Job Description
                soup = BeautifulSoup(driver.page_source, "html.parser")
                job_description_section = soup.find("div", {"class": "show-more-less-html__markup"})

                if job_description_section:
                    job_description = job_description_section.get_text(separator=" ", strip=True)
                    job_description = re.sub(r"\n", " ", job_description)  # Clean up text
                

                    # Ensure the directory exists
                    os.makedirs(parent_dir, exist_ok=True)

                    # Create folders

                    
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(job_description)

                    # Save to file
                    print(f"✅ Success: Job description saved for {link[0]}.")
                    break
                else:
                    print(f"⚠️ Warning: Job description not found for {link[1]}.")
            except Exception as e:
                print(f"❌ Error processing {folders[index]}: {e}")
            finally:
                driver.quit()
    print("-----✅All descriptions Generated!-----")
    


