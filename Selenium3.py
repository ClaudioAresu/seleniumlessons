from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = r"C:\Users\Marina\Documents\Selenium Project\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://techwithtim.net")

link = driver.find_element_by_link_text("Python Programming")
link.click()



try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

except:
    driver.quit()


#para voltar ou avançar página só usar os comandos .back e .forward no driver, e para usar novo clique, usar .clear para limpara a memória dos comandos anteriores