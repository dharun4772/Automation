from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver,600)
target="Dad"
message="Hi"
x_arg = '//span[contains(@title,' + target + ')]'
grp_title=wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
grp_title.click()
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box=wait.until(EC.presence_of_element_located((By.XPATH,inp_xpath)))
for i in range(5):
    input_box.send_keys(message+Keys.ENTER)
    time.sleep(1)
driver.close()

