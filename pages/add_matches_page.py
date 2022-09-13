from pages.base_page import BasePage
from pages.dashboard import Dashboard
from utils.settings import DEFAULT_LOCATOR_TYPE
import requests


class AddMatches(BasePage):
    matches_button_xpath = "(//div[@role='button'])[4]"
    expected_title = "Adding match player Max Minston"
    title_of_page_xpath = "(//span[@class='MuiTypography-root MuiCardHeader-title MuiTypography-h5 MuiTypography-displayBlock'])[1]"
    add_match_button_xpath = "(//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text jss34'])[1]"
    my_team_field_xpath = "//input[@name='myTeam']"
    enemy_team_field_xpath = "//input[@name='enemyTeam']"
    my_team_score_field_xpath = "//input[@name='myTeamScore']"
    enemy_team_score_field_xpath = "//input[@name='enemyTeamScore']"
    date_xpath = "//input[@name='date']"
    match_at_home_radio_xpath = "//input[@value='true']"
    match_out_home_radio_xpath = "//input[@value='false']"
    submit_button_xpath = "//button[@type='submit']"
    search_field_xpath = "//input[@placeholder='Search…']"
    card_of_player_xpath = '//*[@id="MUIDataTableBodyRow-02677958699365781-0"]/td[2]'

    def type_in_my_team_field(self, my_team):
        self.field_send_keys(self.my_team_field_xpath, my_team)

    def type_in_enemy_team_field(self, enemy_team):
        self.field_send_keys(self.enemy_team_field_xpath, enemy_team)

    def type_in_my_team_score_field(self, my_team_score):
        self.field_send_keys(self.my_team_score_field_xpath, my_team_score)

    def type_in_enemy_team_score_field(self, enemy_team_score):
        self.field_send_keys(self.enemy_team_score_field_xpath, enemy_team_score)

    def type_in_date(self, date):
        self.field_send_keys(self.date_xpath, date)

    def click_on_the_match_out_home_radio(self, match_out_home):
        self.click_on_the_element(self.match_out_home_radio_xpath)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def check_the_text_of_the_page(self):
        self.assert_element_text(self.driver, self.title_of_page_xpath, self.expected_title)

    def click_on_the_add_match_button(self):
        self.click_on_the_element(self.add_match_button_xpath)

    def type_in_search_field(self, search):
        self.field_send_keys(self.search_field_xpath, search)

    def click_on_the_card_of_player(self):
        self.click_on_the_element(self.card_of_player_xpath)

    def click_on_matches_button(self):
        self.click_on_the_element(self.matches_button_xpath)
