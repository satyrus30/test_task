#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BaseMethods:
    def __init__(self, driver, wait=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)

    def click(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def input(self, element, value):
        self.click(element)
        element.clear()
        element.send_keys(value)

    def open(self, url):
        self.driver.get(url)

    def element(self, locator: tuple):
        try:
            return self.wait.until(ec.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента {locator}")
