from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class AccountPage(Page):
    ERROR_MSG = (By.CSS_SELECTOR, "div.message-container")
    INPUT_ID = (By.CSS_SELECTOR, "input#username")
    INPUT_PW = (By.CSS_SELECTOR, "input#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[name='login']")

    BLANK_ID_MSG = "Error: Username is required."
    BLANK_PW_MSG = "Error: The password field is empty."
    INVALID_ID_MSG = "Unknown email address. Check again or try your username."

    # error_type: 0 -> invalid credential, 1 -> blank_id, 2 -> blank_pw
    error_type = 0

    def open_my_account(self):
        self.open_page("https://gettop.us/my-account/")

    def login_try(self, email, pw):
        id_input = self.find_element(*self.INPUT_ID)
        pw_input = self.find_element(*self.INPUT_PW)

        self.error_type = 0
        if email == "blank email":
            self.error_type = 1
            email = ""
            id_input.clear()
        if pw == "blank password":
            pw = ""
            pw_input.clear()
            if email != "":
                self.error_type = 2

        id_input.send_keys(email)
        pw_input.send_keys(pw)

        self.click(*self.LOGIN_BUTTON)

    def verify_login_failed(self):
        login_button = self.find_elements(*self.LOGIN_BUTTON)
        # if login button exists, it means login failed
        assert len(login_button), "Logged in successfully"

    def verify_error_msg(self):
        if self.error_type == 1:
            correct_err_msg = self.BLANK_ID_MSG
        elif self.error_type == 2:
            correct_err_msg = self.BLANK_PW_MSG
        else:
            correct_err_msg = self.INVALID_ID_MSG

        self.verify_text(correct_err_msg, *self.ERROR_MSG)