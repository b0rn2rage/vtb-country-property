import pytest
import json
import os
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "C:\\autotests_download_files"}
    options.add_experimental_option("prefs", prefs)
    chromedriver = "C:\\chromedriver\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chromedriver, options=options)
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
