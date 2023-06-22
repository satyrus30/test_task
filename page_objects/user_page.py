#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class UserPage(BasePage):
    EMAIL_INPUT = (By, "")
    PASSWORD_INPUT = (By, "")
    LOGIN_BUTTON = (By, "")

    def login(self, username, password):
        self._input(self.element(self.EMAIL_INPUT), username)
        self._input(self.element(self.PASSWORD_INPUT), password)
        self.click(self.element(self.LOGIN_BUTTON))
        return self