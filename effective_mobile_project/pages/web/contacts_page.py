from selene import browser, have
import allure

class ContactsChapter:
    def open(self):
        with allure.step('Open site'):
            browser.open("https://effective-mobile.ru/#main")

    def click_contact_us_button(self):
        with allure.step('"Contacts" button is clickable'):
            browser.element('.tn-elem__5730545321680606406492').click()

    def expected_text(self):
        with allure.step('How to contact with us text is displayed'):
            browser.element('[field="tn_text_1680515874720"]').should(have.text(
                'Остались вопросы?'))


contact_us = ContactsChapter()