#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from selenium.webdriver.common.by import By
from page_objects.base_methods import BaseMethods


class MainPage(BaseMethods):
    MAIN_PAGE_URL = 'https://www.saucedemo.com/inventory.html'


class LeftSideBar(BaseMethods):
    OPEN_BURGER_MENU = (By.XPATH, '//*[@id="react-burger-menu-btn"]')
    LEFT_SIDE_BAR = (By.XPATH, '//*[@class="bm-menu"]')
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="logout_sidebar_link"]')
