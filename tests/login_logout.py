from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.data import TestData
from tests.locators import TestLocators
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=1280,720')

class TestLoginLogout:
    def test_login_account(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_LOGIN_ACCOUNT).click()
        driver.find_element(*TestLocators.SEARCH_NAME).send_keys(TestData.EMAIL_LOGIN)
        driver.find_element(*TestLocators.SEARCH_PASS).send_keys(TestData.PASSWORD)
        driver.find_element(*TestLocators.SEARCH_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_CHECKOUT))
        assert driver.find_element(*TestLocators.SEARCH_CHECKOUT), "Тест не пройден"
        driver.quit()

    def test_login_account_profile(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_ACCOUNT_PROFILE).click()
        driver.find_element(*TestLocators.SEARCH_NAME).send_keys(TestData.EMAIL_LOGIN)
        driver.find_element(*TestLocators.SEARCH_PASS).send_keys(TestData.PASSWORD)
        driver.find_element(*TestLocators.SEARCH_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_CHECKOUT))
        assert driver.find_element(*TestLocators.SEARCH_CHECKOUT), "Тест не пройден"
        driver.quit()

    def test_login_form_registration(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_LOGIN_ACCOUNT).click()
        driver.find_element(*TestLocators.SEARCH_REGISTER).click()
        driver.find_element(*TestLocators.SEARCH_REGISTER_LOGIN).click()
        driver.find_element(*TestLocators.SEARCH_NAME).send_keys(TestData.EMAIL_LOGIN)
        driver.find_element(*TestLocators.SEARCH_PASS).send_keys(TestData.PASSWORD)
        driver.find_element(*TestLocators.SEARCH_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_CHECKOUT))
        assert driver.find_element(*TestLocators.SEARCH_CHECKOUT), "Тест не пройден"
        driver.quit()

    def test_login_form_restore(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_LOGIN_ACCOUNT).click()
        driver.find_element(*TestLocators.SEARCH_RESTORE).click()
        driver.find_element(*TestLocators.SEARCH_REGISTER_LOGIN).click()
        driver.find_element(*TestLocators.SEARCH_NAME).send_keys(TestData.EMAIL_LOGIN)
        driver.find_element(*TestLocators.SEARCH_PASS).send_keys(TestData.PASSWORD)
        driver.find_element(*TestLocators.SEARCH_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_CHECKOUT))
        assert driver.find_element(*TestLocators.SEARCH_CHECKOUT), "Тест не пройден"
        driver.quit()

    def test_logout_account(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*TestLocators.SEARCH_LOGIN_ACCOUNT).click()
        driver.find_element(*TestLocators.SEARCH_NAME).send_keys(TestData.EMAIL_LOGIN)
        driver.find_element(*TestLocators.SEARCH_PASS).send_keys(TestData.PASSWORD)
        driver.find_element(*TestLocators.SEARCH_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_ACCOUNT_PROFILE))
        driver.find_element(*TestLocators.SEARCH_ACCOUNT_PROFILE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_LOGOUT))
        driver.find_element(*TestLocators.SEARCH_LOGOUT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.SEARCH_LOGIN))
        assert driver.find_element(*TestLocators.SEARCH_LOGIN), "Тест не пройден"
        driver.quit()
