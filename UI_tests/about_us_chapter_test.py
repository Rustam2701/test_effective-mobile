import allure
from effective_mobile_project.pages.web.about_us_page import about_us

@allure.title('User see expected information about company')
def test_about_us_chapter():
    about_us.open()
    about_us.click_button_about_us()
    about_us.expected_text()


