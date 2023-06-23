#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import allure
from selenium.webdriver.common.by import By
from page_objects.base_methods import BaseMethods


class LoginPage(BaseMethods):
    LOGIN_PAGE_URL = 'https://www.saucedemo.com/'
    USERNAME_INPUT = (By.XPATH, '//*[@placeholder="Username"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@placeholder="Password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login-button"]')
    ERROR_MESSAGE = (By.XPATH,
                     '//*[text()="Epic sadface: Username and password do not match any user in this service"]')

    def login(self, username, password):
        with allure.step("Ввести логин в поле Username"):
            self.input(self.element(self.USERNAME_INPUT), username)
        with allure.step("Ввести пароль в поле Password"):
            self.input(self.element(self.PASSWORD_INPUT), password)
        with allure.step("Нажать кнопку Login"):
            self.click(self.element(self.LOGIN_BUTTON))
        return self
