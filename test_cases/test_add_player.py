import time

import os
import unittest

from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.add_player_page import AddPlayer
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayerPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en/players/add')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player_page(self):
        user_login = LoginPage(self.driver)
        user_login.check_the_text_of_the_box()
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()

        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_add_player_button()

        new_player = AddPlayer(self.driver)
        new_player.type_in_name('Max')
        new_player.type_in_surname('Minston')
        new_player.type_in_age('01.09.1996')
        new_player.type_in_main_position('goalkeeper')
        new_player.click_on_the_submit_button()

        time.sleep(7)

    @classmethod
    def tearDown(self):
        self.driver.quit()