import time
import os
import unittest
from selenium import webdriver
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.remind_password_page import RemindPassword
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestRemindPasswordPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def test_remind_password(self):
        user_login = LoginPage(self.driver)
        # user_login.check_the_text_of_the_box()
        user_login.title_of_page()
        user_login.click_on_the_remind_password_hyperlink()
        remind_password = RemindPassword(self.driver)
        remind_password.type_in_email('user01@getnada.com')
        remind_password.click_on_the_send_button()
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()