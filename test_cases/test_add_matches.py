import time
from pages.base_page import BasePage
import os
import unittest
from turtle import speed

from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

from pages.add_matches_page import AddMatches
import pyautogui

class TestAddMatchesPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/players/630e0a9862fd50f9620fdc24/matches')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_match(self):
        user_login = LoginPage(self.driver)
        # user_login.check_the_text_of_the_box()
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()

        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_the_players_button()

        add_match = AddMatches(self.driver)
        add_match.type_in_search_field('Minston')
        pyautogui.press("Enter")

        add_match.click_on_the_card_of_player()
        add_match.click_on_matches_button()
        add_match.click_on_the_add_match_button()
        add_match.type_in_my_team_field('Lions')
        add_match.type_in_enemy_team_field('Tigers')
        add_match.type_in_my_team_score_field('97')
        add_match.type_in_enemy_team_score_field('95')
        add_match.type_in_date('28.08.2022')
        add_match.click_on_the_submit_button()

        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()
