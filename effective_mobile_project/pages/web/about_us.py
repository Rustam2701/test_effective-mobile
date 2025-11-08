from selene import browser, have
import allure


class AboutUsChapter:
    def open(self):
        with allure.step('Open site'):
            browser.open("https://effective-mobile.ru/#main")

    def click_about_us(self):
        with allure.step('About us button is clickable'):
            browser.element('.tn-elem__5730545321680606406481').click()

    def expected_text(self):
        with allure.step('Information about us'):
            browser.element('[field="tn_text_1680508197689"]').should(have.text(
                'Effective Mobile — это команда экспертов, которая поможет создать собственное мобильное приложение или оперативно внедрить на ваш проект лучших специалистов в сфере IT.'))


about_us = AboutUsChapter()