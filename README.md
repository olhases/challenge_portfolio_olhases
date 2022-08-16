# Task 1. Software configuration

## Subtask1. Why did I choose to participate in the challenge portfolio?

Hello, my name is Olha 👋

I'm taking part in this portfolio_challenge because I'm interested in trying new things. In the direction of automatic testing, I looked for a long time, but I thought that it was very difficult. Seeing the opportunity to learn this, I thought "why not?".  At the same time, I was very interested in the possibility of an internship, so I ended up here.

Thank you for this opportunity, I will be glad to spend the next 6 weeks with you and learn new things from you.

## TASK 2: selectors
### Subtask 1: Searching for selectors on the login pageList all the elements that are on the login page.

#### scouts_panel_h5_xpath
* //*[@id="__next"]/form/div/div[1]/a
* (//h5[normalize-space()='Scouts Panel'])[1]
* //child::div/h5

#### login_field_xpath
* //*[@id="login"]
* //input[@id="login"]
* (//input[@id='login'])[1]
* //*[text()="Login"]

#### password_field_xpath
* //*[@id="password"]
* //input[@id='password']
* //*[text()="Password"]
* (//label[normalize-space()='Password'])[1]

#### remind_password_hyperlink_xpath
* //*[@id="__next"]/form/div/div[1]/a
* //*[text()="Remind password"]
* //child::div/a

#### english_multiselect_xpath
* //*[@id="__next"]/form/div/div[2]/div/div
* //div[@role='button']
* //*[text () ="English"]

#### polish_multiselect_xpath
* //*[@id="__next"]/form/div/div[2]/div/div
* //div[@role='button']
* //*[text () ="Polski"]

#### sing_in_button_xpath
* //*[@id="__next"]/form/div/div[2]
* //*[@class="MuiButton-label"]
* //*[@class="MuiTouchRipple-root"]
* //span[@class='MuiButton-label']
* //child::div/button
