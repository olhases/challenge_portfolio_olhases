from pages.base_page import BasePage
from pages.dashboard import Dashboard
from utils.settings import DEFAULT_LOCATOR_TYPE


class AddPlayer(BasePage):
    name_field_xpath = "//div[@class='Toastify']"
    surname_field_xpath = "//input[@name='surname']"
    age_xpath = "//input[@name='age']"
    main_position_field_xpath = "//input[@name='mainPosition']"
    submit_button_xpath = "//button[@type='submit']"
    title_of_page_xpath = "//span[@class='MuiTypography-root MuiCardHeader-title MuiTypography-h5 MuiTypography-displayBlock']"
    expected_title = "Add player"

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_xpath, age)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def check_the_text_of_the_page(self):
        self.assert_element_text(self.driver, self.title_of_page_xpath, self.expected_title)
