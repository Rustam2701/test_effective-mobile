from selene import browser, have
import allure


class ReviewsChapter:
    def open(self):
        with allure.step('Open site'):
            browser.open("https://effective-mobile.ru/#main")

    def click_reviews_button(self):
        with allure.step('"Reviews" button is clickable'):
            browser.element('.tn-elem__5730545321706704571141').click()

    def expected_text(self):
        with allure.step('User can read a few reviews about company'):
            browser.element('[class="t730__topsection"]').should(have.text(
                'ОТЗЫВЫ КЛИЕНТОВ'))


reviews_about_company = ReviewsChapter()
