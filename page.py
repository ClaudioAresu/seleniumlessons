from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):

    locator = "q"

class GoButtonElement(BasePageElement):
    locator = "go"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    #Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""

        return "Python" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MaingPageLocators.GO_BUTTON)
        element.click()

class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source