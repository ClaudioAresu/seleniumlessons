from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#selecionar Browser. Selecionado Chrome
PATH = r"C:\Users\Marina\Documents\Selenium Project\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#Acessar site
driver.get("http://techwithtim.net")
print(driver.title)

#Elementos de busca, através do nome/buscar texto em keys/Enter para retornar valores
search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
try:
    articles = main.find_elements_by_tag_name("article")
    for article in articles:
        header = article.find_elements_by_class_name("entry-title")
        

finally:
    driver.quit()



#print(driver.page_source)

#Tempo até fechar
time.sleep(10)
#Fechar automaticamente
driver.quit()