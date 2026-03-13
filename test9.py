import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)



        first_input = browser.find_element(By.XPATH,
                                           "//div[@class='first_block']//div[@class='form-group first_class']//input")
        first_input.send_keys("Иван")
        second_input = browser.find_element(By.XPATH,
                                            "//div[@class='first_block']//div[@class='form-group second_class']//input")
        second_input.send_keys("Гогин")
        third_input = browser.find_element(By.XPATH,
                                           "//div[@class='first_block']//div[@class='form-group third_class']//input")
        third_input.send_keys("sobaka@gmail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Uncorrect message")

    def test_registration2(self):
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_input = browser.find_element(By.XPATH,
                                           "//div[@class='first_block']//div[@class='form-group first_class']//input")
        first_input.send_keys("Иван")
        second_input = browser.find_element(By.XPATH,
                                            "//div[@class='first_block']//div[@class='form-group second_class']//input")
        second_input.send_keys("Гогин")
        third_input = browser.find_element(By.XPATH,
                                           "//div[@class='first_block']//div[@class='form-group third_class']//input")
        third_input.send_keys("sobaka@gmail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Uncorrect message")


if __name__ == "__main__":
    unittest.main()
