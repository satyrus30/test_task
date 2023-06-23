#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
import allure

from page_objects.login_page import LoginPage
from selenium.common.exceptions import TimeoutException


@pytest.mark.open_login_page
def test_open_login_page(browser, params):
    login_page = LoginPage(browser)
    login_page.open(params["url"])

    actual_url = browser.current_url
    expected_url = login_page.LOGIN_PAGE_URL
    assert actual_url == expected_url, f'unexpected result: loaded page does not match the url {expected_url}'

    with allure.step("Найти поле для ввода - Username"):
        try:
            login_page.element(login_page.USERNAME_INPUT)
        except TimeoutException:
            raise AssertionError('unexpected result: the element search led to an error')

    with allure.step("Найти поле для ввода - Password"):
        try:
            login_page.element(login_page.PASSWORD_INPUT)
        except TimeoutException:
            raise AssertionError('unexpected result: the element search led to an error')

    with allure.step("Найти кнопку - Login"):
        try:
            login_page.element(login_page.LOGIN_BUTTON)
        except TimeoutException:
            raise AssertionError('unexpected result: the element search led to an error')
