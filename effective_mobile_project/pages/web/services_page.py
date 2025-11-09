from selene import browser, have
import allure


class ServicesChapter:
    def open(self):
        with allure.step('Open site'):
            browser.open("https://effective-mobile.ru/#main")

    def click_services_button(self):
        with allure.step('"Services" button is clickable'):
            browser.element('.tn-elem__5730545321680606406485').click()

    def expected_text_services(self):
        with allure.step('Information about services in the company displayed to the user'):
            browser.element('[field="tn_text_1680510339492"]').should(have.text(
                'Разработаем мобильное приложение с нуля от проектирования интерфейса до программирования, тестирования и оптимизации для различных платформ (iOS, Android, Flutter). Мобильное приложение поможет бизнесу повысить лояльность клиентов и расширить аудиторию.'))


services_of_company = ServicesChapter()