#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

PATH_TO_DRIVER = ChromeDriverManager().install()


def pytest_addoption(parser):
    """
    argparse-style options and ini-style config values, called once at the beginning of a test run.
    @param parser: to add command line options.
    """
    parser.addoption("--url", "-U", default="https://www.saucedemo.com/", help='input ip address')
    parser.addoption("--showbrowser", action="store_true", help="show browser")


@pytest.fixture
def params(request) -> dict:
    """
    :param request: request fixture is a special fixture providing information of the requesting test function
    :return: dictionary with data
    """
    params = {
              'url': request.config.getoption('--url'),
              'showbrowser': request.config.getoption('--showbrowser')
    }

    return params


@pytest.fixture
def browser(params: dict):
    """ Фикстура инициализации браузера """
    url = params["url"]

    service = Service(executable_path=PATH_TO_DRIVER)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--force-device-scale-factor=1")
    chrome_options.add_argument('--disable-dev-shm-usage')

    if not params['showbrowser']:
        chrome_options.add_argument('headless')

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)

    yield driver

    driver.close()
    driver.quit()