#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import allure

from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage, LeftSideBar
from selenium.common.exceptions import TimeoutException


@pytest.mark.authorization_negative
@pytest.mark.parametrize('login, password', [('qwerty', 'secret_sauce'),
                                             ('qwerty', 'qwerty'),
                                             ('standard_user', 'qwerty')])
def test_invalid_authorization(login, password, browser):
    with allure.step("Авторизация"):
        user = LoginPage(browser)
        user.login(username=login, password=password)

    error_message_locator = user.ERROR_MESSAGE
    element = user.element(error_message_locator)

    with allure.step("Найти сообщение о ошибке"):
        try:
            element
        except TimeoutException:
            raise AssertionError(f"unexpected result: no error message was found - {element.text}")


@pytest.mark.authorization_positive
def test_valid_authorization(browser, params):
    with allure.step("Авторизация"):
        user = LoginPage(browser)
        user.login(username=params["login"], password=params["password"])

    main_page = MainPage(browser)
    actual_url = browser.current_url
    expected_url = main_page.MAIN_PAGE_URL
    with allure.step("Сравнить ожидаемый и фактическй url"):
        assert actual_url == expected_url, f'unexpected result: loaded page does not match the url {expected_url}'


@pytest.mark.logout
def test_logout(browser, params):
    with allure.step("Авторизация"):
        user = LoginPage(browser)
        user.login(username=params["login"], password=params["password"])

    left_side_bar = LeftSideBar(browser)
    with allure.step("Нажать на кнопку - Open_burger_menu"):
        left_side_bar.click(left_side_bar.OPEN_BURGER_MENU)

    with allure.step("Нажать на кнопку - Logout"):
        left_side_bar.click(left_side_bar.LOGOUT_BUTTON)

    actual_url = browser.current_url
    expected_url = user.LOGIN_PAGE_URL
    with allure.step("Сравнить ожидаемый и фактическй url"):
        assert actual_url == expected_url, f'unexpected result: loaded page does not match the url {expected_url}'
