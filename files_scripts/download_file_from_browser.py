import os.path
import time

from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

current_directory = os.path.dirname(os.path.abspath(__file__))

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": os.path.join(current_directory, '../tmp'),
    "download.prompt_for_download": False
}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.config.driver = driver

browser.open('https://demoqa.com/upload-download')
browser.element('#downloadButton').click()
time.sleep(3)

assert os.path.getsize('sampleFile.jpeg') == 4096


