from pages.base_page import BasePage


class LoginPage(BasePage):
    scouts_panel_header_xpath = "//child::div/h5"
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    remind_password_hyperlink_xpath = "//child::div/a"
    MuiSelect_button_xpath = "//div[@role='button']"
    sign_in_button_xpath = "//child::div/button"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

