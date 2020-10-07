import pytest
import json
from selenium import webdriver
import os


@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def config():
    with open('C:\\Users\\Tony\\PycharmProjects\\vtb-country-property\\options\\data.json') as config_file:
        data = json.load(config_file)
    return data
