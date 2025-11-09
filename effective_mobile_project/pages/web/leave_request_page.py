from selene import browser, have
import allure


class LeaveRequestForCall:
    def open(self):
        with allure.step('Open site'):
            browser.open("https://effective-mobile.ru/#main")

    def click_contact_us_button(self):
        with allure.step('"Contacts" button is clickable'):
            browser.element('.tn-elem__5730545321680606406492').click()

    def type_name(self):
        with allure.step('User can type the name'):
            browser.element('[id="nm-1531306243545"]').type('Сергей')

    def type_phone_number(self):
        with allure.step('User can type the phone number'):
            browser.element('[id="input_1531306540094"]').type('9099990990')

    def type_nick_telegram(self):
        with allure.step('User can type the nickname of telegram'):
            browser.element('[id="in-1680516575724"]').type('@Sergey333')

    def type_additional_info(self):
        with allure.step('User can type the additional information about his/her company'):
            browser.element('[name = "Дополнительная информация"]').type('Частная компания, нужен прайс-лист')

    def send_request(self):
        with allure.step('User can type the phone number'):
            browser.element('[class="t-submit"]').click()


    def modal_window_of_success(self):
        with allure.step('Successfull sended rquest'):
            browser.element('[class="t-form-success-popup__text t-descr t-descr_sm"]').should(have.text(
                'Спасибо! Данные успешно отправлены.'))


leave_request_for_call = LeaveRequestForCall()
