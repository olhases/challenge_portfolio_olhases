from pages.base_page import BasePage


class Dashboard(BasePage):
    Scouts_Panel_h_6_xpath = "//child::div/h6"
    Main_page_button_xpath = "(//div[@role='button'])[1]"
    Players_button_xpath = "(//div[@role='button'])[2]"
    Language_button_xpath = "(//div[@role='button'])[3]"
    Sing_out_button_xpath = "(//div[@role='button'])[4]"
    Players_count_xpath = "(//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-md-3'])[1]"
    Matches_count_xpath = "(//div[@class='MuiPaper-root MuiPaper-elevation1 MuiPaper-rounded'])[2]"
    Report_count_xpath = "(//div[@class='MuiPaper-root MuiPaper-elevation1 MuiPaper-rounded'])[3]"
    Events_count_xpath = "(//div[@class='MuiPaper-root MuiPaper-elevation1 MuiPaper-rounded'])[4]"
    Logo_Scouts_Panel = "//div[@title='Logo Scouts Panel']"
    Scouts_Panel_h_2_xpath = "//h2[normalize-space()='Shortcuts'](//h2[normalize-space()='Scouts Panel'])[1]"
    text_xpath = "//child::div/p"
    dev_team_contact_hyperlink_xpath = "//span[normalize-space()='Dev team contact']"
    Shortcuts_h_2_xpath = "(//h2[normalize-space()='Shortcuts'])[1]"
    add_player_hyperlink_xpath = "//span[normalize-space()='Add player']"
    Activity_h_2_xpath = "//h2[normalize-space()='Activity']"
    pass
