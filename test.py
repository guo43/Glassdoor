from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.glassdoor.com/index.htm")
input_area = driver.find_element_by_name("sc.keyword")
input_area.send_keys("data analyst")
input_area.send_keys(Keys.RETURN)




#driver.close()
