from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import asyncio

PATH = r"C:\Users\Marina\Documents\Selenium Project\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(10)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id ("productPrice" + str(i)) for i in range(1,-1,-1)]

actions = ActionChains(driver)
actions.click(cookie)

async def click_cookies():
    while True:
        actions.perform()
        count = int(cookie_count.text.split(" ")[0])
        print(count)
        for item in items:
            value = int(item.text)
            if value <= count:
                upgrade_actions = ActionChains(driver)
                upgrade_actions.move_to_element(item)
                upgrade_actions.click()
                upgrade_actions.perform()
                await asyncio.sleep(2)

#async def main():
    task1 = asyncio.create_task(socket_test.element)
    task2 = asyncio.create_task(click_cookies)
    await task2
    await task1
#asyncio.run(main())
asyncio.run(click_cookies())