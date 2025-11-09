import allure
from effective_mobile_project.pages.web.contacts_page import contact_us


@allure.title('User can see how to contact with the company')
def test_contacts():
    contact_us.open()
    contact_us.click_contact_us_button()
    contact_us.expected_text()