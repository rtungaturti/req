**Login Page Automation Script**
================================

### Purpose

This script automates the login functionality on the Practice Test Automation website.

### Requirements

* Python 3.8+
* Selenium 4.0+
* WebDriver (e.g., ChromeDriver, GeckoDriver)
* Unittest

### Script

```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestLoginPage(unittest.TestCase):
    def setUp(self):
        # Set up WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Optional
        self.driver = webdriver.Chrome(options=options)
        self.base_url = "https://practicetestautomation.com/"

    def tearDown(self):
        # Close WebDriver
        self.driver.quit()

    def test_positive_login(self):
        # Test case 1: Positive LogIn test
        self.driver.get(self.base_url + "login/")
        self._enter_credentials("student", "Password123")
        self._submit_form()
        self._verify_login_success()

    def test_negative_username(self):
        # Test case 2: Negative username test
        self.driver.get(self.base_url + "login/")
        self._enter_credentials("incorrectUser", "Password123")
        self._submit_form()
        self._verify_error_message("Your username is invalid!")

    def test_negative_password(self):
        # Test case 3: Negative password test
        self.driver.get(self.base_url + "login/")
        self._enter_credentials("student", "incorrectPassword")
        self._submit_form()
        # Note: The expected error message for incorrect password is not provided
        #       in the problem description. Assuming it's "Your password is invalid!"
        self._verify_error_message("Your password is invalid!")

    def _enter_credentials(self, username, password):
        # Enter username and password
        try:
            username_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_input.send_keys(username)
            password_input = self.driver.find_element(By.ID, "password")
            password_input.send_keys(password)
        except TimeoutException:
            self.fail("Timed out waiting for username and password fields")

    def _submit_form(self):
        # Submit the form
        try:
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "submit"))
            )
            submit_button.click()
        except TimeoutException:
            self.fail("Timed out waiting for submit button")

    def _verify_login_success(self):
        # Verify login success
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("logged-in-successfully/")
            )
            self.assertIn("Congratulations", self.driver.page_source)
            self.assertIn("Log out", self.driver.page_source)
        except TimeoutException:
            self.fail("Timed out waiting for login success")

    def _verify_error_message(self, expected_message):
        # Verify error message
        try:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "error"))
            )
            self.assertEqual(expected_message, error_message.text)
        except TimeoutException:
            self.fail("Timed out waiting for error message")

if __name__ == "__main__":
    unittest.main()
```

### Usage

1. Save the script as `login_page_test.py`.
2. Install required packages: `pip install selenium unittest`.
3. Download and configure WebDriver (e.g., ChromeDriver).
4. Run the script: `python login_page_test.py`.

### Notes

* This script uses ChromeDriver, but you can easily switch to another WebDriver (e.g., GeckoDriver).
* The script assumes the base URL is `https://practicetestautomation.com/`.
* You may need to adjust the locators and expected messages based on the actual website implementation.
* This script uses explicit waits to ensure dynamic elements are loaded before interacting with them.
* The script uses Unittest for assertions and test organization.