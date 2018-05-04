import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# get URL
driver = webdriver.Chrome()
baseURL = "https://www.glassdoor.com/index.htm"
driver.get(baseURL)
driver.implicitly_wait(3)

# Search job and location
keywordElement = driver.find_element_by_id("KeywordSearch")
locationElement = driver.find_element_by_id("LocationSearch")
keywordElement.clear()
keywordElement.send_keys("Data Analyst")
locationElement.clear()
locationElement.send_keys("New York, NY")
driver.find_element_by_class_name("gd-btn-mkt").click()

# get text

jobsList = []
jobsDscript = []

page_remaining = True
while page_remaining:
    jobs = driver.find_elements_by_class_name("jl")

    for job in jobs:
        try:
            # emailMeJob_pop = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.CLASS_NAME, "mfp-close")))
            # time.sleep(5)
            emailMeJob_pop = driver.find_element_by_class_name("mfp-close")
            emailMeJob_pop.click()
        except:
            pass

        try:
            jobsList.append(job.text)
            job.click()
            jobDscript = driver.find_element_by_id("JobDescriptionContainer")
            jobsDscript.append(jobDscript.text)
        except:
            jobsDscript.append("NA")

    next_page = driver.find_element_by_class_name("next")
    try:
        next_page.find_element_by_tag_name("a")
        next_page.click()

    except:
        page_remaining = False
        print("Finished")
for indx, value in enumerate(jobsDscript):
    if value != "NA":
        print(indx, "ok")
    else:
        print(indx, value)