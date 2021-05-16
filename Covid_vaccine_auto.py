from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
path = "C:\\Users\\vishn\\PycharmProjects\\pythonProject\\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.cowin.gov.in/home")
search = driver.find_elements_by_id("mat-input-0")
search[0].send_keys("641045")
search[0].send_keys(Keys.ENTER)
dates = []
dt = []
d = {}

# sample=driver.find_element_by_id("status")
# print(sample.get_attribute("type"))
try:
    slot = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "slot-available-wrap")))
    hospt = driver.find_elements_by_class_name("main-slider-wrap")
    hospital = hospt[0].find_element_by_tag_name("h5").text
    addr = hospt[0].find_element_by_tag_name("p").text
    print(hospital)
    print(addr)
    slots = slot.find_elements_by_tag_name("li")
    dates = driver.find_elements_by_tag_name("slide")
    for i in dates:
        dt.append(i.find_element_by_tag_name("p").text)
    c = 0
    for i in slots:
        sam = i.find_elements_by_class_name("slots-box")
        print(sam)
        status, age, med = [], [], []
        for j in sam:
            status.append(j.find_element_by_tag_name("a").text)
            med.append(j.find_element_by_class_name("name").text)
            flag = j.find_elements_by_class_name("age-limit")
            age.append(flag[0].text if len(flag) >= 1 else "")
        d[dt[c]] = {"status": status, "med": med, "age": age}
        c += 1

except:
    driver.quit()
print(d)

driver.quit()
