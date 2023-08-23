from pages.auth_page import AuthPage
from pages.locators import AuthtorizationLocators, RegistrationLocators, PasswordRecoveryLocators, AgrLocators, \
    SocialLocators
import pytest
from tests import valid_data, messages, invalid_data


#ART-1

def test_load_reg_page_positive(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.link_registration)
    assert 'registration' in page.get_current_url()
    assert page.get_text_from_element(RegistrationLocators.reg_title) == 'Регистрация'


#ART-2

def test_load_auth_page_positive(browser):
    page = AuthPage(browser)
    page.go_to_site()
    assert 'https://b2c.passport.rt.ru/' in page.get_current_url()
    assert page.get_text_from_element(AuthtorizationLocators.auth_title) == 'Авторизация'


#ART-3

def test_load_forgot_pass_page_positive(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.link_forgot_pass)
    assert 'login-actions/reset-credentials' in page.get_current_url()
    assert page.get_text_from_element(PasswordRecoveryLocators.pass_title) == 'Восстановление пароля'


#ART-4
def test_reg_user_without_data_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.link_registration)
    reg_url = page.get_current_url()
    page.click_reg_btn()
    assert reg_url == page.get_current_url()


#ART-5

@pytest.mark.parametrize('email', invalid_data.incorrect_emails)
def test_reg_invalid_email_negative(browser, email):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.link_registration)
    page.enter_data(RegistrationLocators.reg_login, email)
    page.click_reg_btn()
    assert page.get_text_from_element(RegistrationLocators.reg_error) == messages.wrong_login_message


#ART-6

@pytest.mark.parametrize('password', invalid_data.incorrect_passwords)
def test_reg_invalid_password_negative(browser, password):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.link_registration)
    page.enter_data(RegistrationLocators.reg_password, password)
    page.click_reg_btn()
    assert page.get_text_from_element(RegistrationLocators.reg_error) == messages.wrong_password_message


#ART-7

@pytest.mark.parametrize('phone', invalid_data.incorrect_phones)
def test_reg_invalid_phone_negative(browser, phone):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.link_registration)
    page.enter_data(RegistrationLocators.reg_login, phone)
    page.click_reg_btn()
    assert page.get_text_from_element(RegistrationLocators.reg_error) == messages.wrong_login_message


#ART-8

@pytest.mark.parametrize('name', invalid_data.incorrect_names)
def test_reg_invalid_name_negative(browser, name):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.link_registration)
    page.enter_data(RegistrationLocators.name, name)
    page.click_reg_btn()
    assert page.get_text_from_element(RegistrationLocators.reg_error) == messages.wrong_name_message


#ART-9

@pytest.mark.parametrize('surname', invalid_data.incorrect_surnames)
def test_reg_invalid_surname_negative(browser, surname):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.link_registration)
    page.enter_data(RegistrationLocators.surname, surname)
    page.click_reg_btn()
    assert page.get_text_from_element(RegistrationLocators.reg_error) == messages.wrong_surname_message


#ART-10

@pytest.mark.parametrize('login', valid_data.correct_logins)
def test_auth_user_with_valid_email_positive(browser, login):
    page = AuthPage(browser)
    page.go_to_site()
    page.enter_data(AuthtorizationLocators.auth_login, login)
    page.enter_data(AuthtorizationLocators.auth_pass, valid_data.correct_pass)
    page.click_enter_btn()


#ART-11

def test_auth_user_with_invalid_mail_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.enter_data(AuthtorizationLocators.auth_login, invalid_data.incorrect_email)
    page.enter_data(AuthtorizationLocators.auth_pass, valid_data.correct_pass)
    page.click_enter_btn()
    assert page.get_text_from_element(
        AuthtorizationLocators.auth_error) == messages.wrong_login_or_pass_message or messages.wrong_capcha_message


#ART-12

def test_auth_user_with_invalid_phone_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.enter_data(AuthtorizationLocators.auth_login, invalid_data.incorrect_phone)
    page.enter_data(AuthtorizationLocators.auth_pass, valid_data.correct_pass)
    page.click_enter_btn()
    assert page.get_text_from_element(
        AuthtorizationLocators.auth_error) == messages.wrong_login_or_pass_message or messages.wrong_capcha_message


#ART-13

@pytest.mark.parametrize('login', valid_data.correct_logins)
def test_auth_user_with_invalid_pass_negative(browser, login):
    page = AuthPage(browser)
    page.go_to_site()
    page.enter_data(AuthtorizationLocators.auth_login, login)
    page.enter_data(AuthtorizationLocators.auth_pass, invalid_data.incorrect_pass)
    page.click_enter_btn()
    assert page.get_text_from_element(
        AuthtorizationLocators.auth_error) == messages.wrong_login_or_pass_message or messages.wrong_capcha_message


#ART-14

def test_auth_with_yandex_profile_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.icon_yandex)
    page.enter_data(SocialLocators.yandex_login, invalid_data.incorrect_login_yandex)
    page.click_link(SocialLocators.yandex_submit_btn)
    assert page.get_text_from_element(SocialLocators.yandex_error_message) == messages.yandex_wrong_message
    assert 'passport.yandex.ru' in page.get_current_url()

#ART-15

def test_auth_with_google_profile_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.icon_google)
    page.enter_data(SocialLocators.google_login, invalid_data.incorrect_email)
    page.click_link(SocialLocators.google_submit_btn)
    assert page.get_text_from_element(SocialLocators.google_error_message) == messages.google_wrong_message
    assert 'accounts.google.com' in page.get_current_url()

#ART-16

def test_auth_with_mail_profile_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.icon_male)
    page.enter_data(SocialLocators.mail_login, invalid_data.incorrect_email)
    page.enter_data(SocialLocators.mail_pass, invalid_data.incorrect_pass)
    page.click_link(SocialLocators.mail_submit_btn)
    assert page.get_text_from_element(SocialLocators.mail_error_message) == messages.mail_wrong_message
    assert 'connect.mail.ru' in page.get_current_url()

#ART-17

def test_auth_with_ok_profile_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.icon_ok)
    page.enter_data(SocialLocators.ok_login, invalid_data.incorrect_email)
    page.enter_data(SocialLocators.ok_pass, invalid_data.incorrect_pass)
    page.click_link(SocialLocators.ok_submit_btn)
    assert page.get_text_from_element(SocialLocators.ok_error_message) == messages.ok_wrong_message
    assert 'connect.ok.ru' in page.get_current_url()

#ART-18

def test_auth_with_vk_profile_negative(browser):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(AuthtorizationLocators.icon_vk)
    page.enter_data(SocialLocators.vk_login, invalid_data.incorrect_email)
    page.enter_data(SocialLocators.vk_pass, invalid_data.incorrect_pass)
    page.click_link(SocialLocators.vk_submit_btn)
    assert page.get_text_from_element(SocialLocators.vk_error_message) == messages.vk_wrong_message
    assert 'oauth.vk.com' in page.get_current_url()


#ART-19

def test_agreement_link_positive(browser):
    page = AuthPage(browser)
    page.get(valid_data.agreement_url)
    assert page.get_text_from_element(AgrLocators.agr_title) == valid_data.agreement_title


#ART-20

@pytest.mark.parametrize('locator, expected',
                         [(AuthtorizationLocators.tab_mail, 'Электронная почта'),
                          (AuthtorizationLocators.tab_login, 'Логин'),
                          (AuthtorizationLocators.tab_pers_account, 'Лицевой счёт'),
                          (AuthtorizationLocators.tab_phone, 'Мобильный телефон')])
def test_change_tabs_auth_page_positive(browser, locator, expected):
    page = AuthPage(browser)
    page.go_to_site()
    page.click_link(locator)
    assert page.get_text_from_element(AuthtorizationLocators.login_placeholder) == expected
