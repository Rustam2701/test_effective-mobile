import allure
from selene import browser, have
from effective_mobile_project.pages.web.about_us import about_us

@allure.title('User see expected information about company')
def test_about_us():
    about_us.open()
    about_us.click_about_us()
    about_us.expected_text()

def test_services():
    browser.open('https://effective-mobile.ru/#main')
    browser.element('.tn-elem__5730545321680606406485').click()
    browser.element('[field="tn_text_1680510339492"]').should(have.text('Разработаем мобильное приложение с нуля от проектирования интерфейса до программирования, тестирования и оптимизации для различных платформ (iOS, Android, Flutter). Мобильное приложение поможет бизнесу повысить лояльность клиентов и расширить аудиторию.'))

def test_reviews():
    browser.open('https://effective-mobile.ru/#main')
    browser.element('.tn-elem__5730545321706704571141').click()
    browser.element('[class="t730__topsection"]').should(have.text('ОТЗЫВЫ КЛИЕНТОВ'))

def test_contacts():
    browser.open('https://effective-mobile.ru/#main')
    browser.element('.tn-elem__5730545321680606406492').click()
    browser.element('[field="tn_text_1680515874720"]').should(have.text('Остались вопросы?'))
