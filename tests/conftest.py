import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/")

@pytest.fixture(autouse=True)
def browser():
    driver = webdriver.Chrome()

    yield driver
    driver.quit()