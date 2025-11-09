import allure
from effective_mobile_project.pages.web.leave_request_page import leave_request_for_call


@allure.title('User can send a request for a call')
def test_leave_request():
    leave_request_for_call.open()
    leave_request_for_call.click_contact_us_button()
    leave_request_for_call.type_name()
    leave_request_for_call.type_phone_number()
    leave_request_for_call.type_nick_telegram()
    leave_request_for_call.type_additional_info()
    leave_request_for_call.send_request()
    leave_request_for_call.modal_window_of_success()
