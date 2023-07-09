from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.locators import TestLocators
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1280,720')

class TestToFromAccount:
    def test_to_account(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_ACCOUNT_PROFILE).click()
        assert '/login' in driver.current_url
        driver.quit()

    def test_from_account_to_constructor(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_ACCOUNT_PROFILE).click()
        driver.find_element(*TestLocators.SEARCH_NAME).send_keys("svetlanazolotova11123@yandex.ru")
        driver.find_element(*TestLocators.SEARCH_PASS).send_keys("12345678")
        driver.find_element(*TestLocators.SEARCH_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ACCOUNT_PROFILE))
        driver.find_element(*TestLocators.SEARCH_ACCOUNT_PROFILE).click()
        driver.find_element(*TestLocators.SEARCH_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/button[text() = "Оформить заказ"]')))
        assert driver.find_element(By.XPATH, './/button[text() = "Оформить заказ"]'), "Тест не пройден"
        driver.quit()

    def test_from_account_to_logo(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_ACCOUNT_PROFILE).click()
        driver.find_element(*TestLocators.SEARCH_NAME).send_keys("svetlanazolotova11123@yandex.ru")
        driver.find_element(*TestLocators.SEARCH_PASS).send_keys("12345678")
        driver.find_element(*TestLocators.SEARCH_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ACCOUNT_PROFILE))
        driver.find_element(*TestLocators.SEARCH_ACCOUNT_PROFILE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_LOGO))
        driver.find_element(*TestLocators.SEARCH_LOGO).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, './/button[text() = "Оформить заказ"]')))
        assert driver.find_element(By.XPATH, './/button[text() = "Оформить заказ"]'), "Тест не пройден"
        driver.quit()
