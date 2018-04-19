from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.glassdoor.com/index.htm")
assert "Glassdoor" in driver.title

# type job and location
input_job = driver.find_element_by_name("sc.keyword")
input_job.clear()
input_job.send_keys("data analyst")

input_location = driver.find_element_by_id("LocationSearch")
input_location.clear()
input_location.send_keys("New York")
input_location.submit()
assert "No results found." not in driver.page_source

#search for individual description listed by companies
all_companies = driver.find_elements_by_class_name("jl")

company_list = []
job_description = []
for company in all_companies:
    company_list.append(company.text)
    company.click()
    driver.implicitly_wait(10)
    try:
        descrip = driver.find_element_by_class_name("jobDescriptionContent")
        job_description.append(descrip.text)
    except:
        job_description.append("N/A")











#driver.close()
