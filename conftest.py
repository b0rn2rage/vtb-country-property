import pytest
import json
from selenium import webdriver
import os


@pytest.fixture(scope='function')
def browser():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "C:\\qwe"}
    chrome_options.add_experimental_option("prefs", prefs)
    chromedriver = "C:\\chromedriver\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
    #driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def config():
    with open(os.getcwd()+'\\options\\data.json', encoding='utf-8') as config_file:
        data = json.load(config_file)
    return data


@pytest.fixture(scope='session')
def host():
    with open(os.getcwd()+'\\options\\hostname.json', encoding='utf-8') as host_file:
        host_names = json.load(host_file)
    return host_names
