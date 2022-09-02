from pages.base_page import BasePage


class RemindPassword(BasePage):
    title_of_box_xpath = "(//h5[normalize-space()='Remind password'])[1]"
    header_of_box_xpath = 'Remind password'
    email_field_xpath = "//input[@name='email']"
    send_button_xpath = "//button[@type='submit']"

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def click_on_the_send_button(self):
        self.click_on_the_element(self.send_button_xpath)
