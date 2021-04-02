from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    # find_elements function added
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def open_page(self, url):
        self.driver.get(url)

    # Receive **kwargs to see if it needs to hit the enter key
    # Syntax: Page.input_text(str, *locator, enter=bool)
    # enter=bool is optional
    # The default value is enter=False
    def input_text(self, text: str, *locator, **kwargs):
        e = self.driver.find_element(*locator)
        e.clear()

        # if kwargs doesn't have an "enter" key or kwargs["enter"] is not a boolean value
        # set kwargs["enter"] to the default value
        if "enter" not in kwargs.keys() or type(kwargs["enter"]) is not bool:
            kwargs["enter"] = False

        e.send_keys(text, Keys.ENTER) if kwargs["enter"] else e.send_keys(text)

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def verify_text(self, expected_text: str, *locator):
        """
        Search for a web element, get its text, compare with expected_text
        :param expected_text: Text to be in web element
        :param locator: Search strategy and locator of web element (ex. (By.ID, 'id') )
        """
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f"Expected {expected_text} does not match actual {actual_text}"

    def hover_over_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()
