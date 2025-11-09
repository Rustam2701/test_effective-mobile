import allure
from effective_mobile_project.pages.web.reviews_page import reviews_about_company


@allure.title('User can see a few reviews about the company')
def test_reviews_of_company():
    reviews_about_company.open()
    reviews_about_company.click_reviews_button()
    reviews_about_company.expected_text()
