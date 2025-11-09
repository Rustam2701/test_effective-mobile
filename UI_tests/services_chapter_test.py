import allure
from effective_mobile_project.pages.web.services_page import services_of_company


@allure.title('Information about services in the company')
def test_services():
    services_of_company.open()
    services_of_company.click_services_button()
    services_of_company.expected_text_services()
