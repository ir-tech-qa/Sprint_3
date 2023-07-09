from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import TestLocators
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1280,720')

class TestToConstructor:
    def test_to_constructor_fillings(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_FILLINGS).click()
        assert driver.find_element(By.XPATH, './/h2[text() = "Начинки"]').text =='Начинки'
        driver.quit()

    def test_to_constructor_sauces(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_SAUCES).click()
        assert driver.find_element(By.XPATH, './/h2[text() = "Соусы"]').text =='Соусы'
        driver.quit()

    def test_to_constructor_rolls(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_SAUCES).click()
        driver.find_element(*TestLocators.SEARCH_ROLLS).click()
        assert driver.find_element(By.XPATH, './/h2[text() = "Булки"]').text == 'Булки'
        driver.quit()