# Selenium Test Script for Requirement
# Requirement: FR-05: "I'm Feeling Lucky" button redirects to: https://www.google.com/search?q=<user_query>&btnI=I
# Generated on: 2025-05-25 02:55:49

Here is a Python Selenium test script that covers the specified test cases:
```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestImFeelingLucky(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Replace with your desired browser
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_valid_user_query(self):
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element_by_name("q")
        search_box.send_keys("java tutorials")
        lucky_button = self.driver.find_element_by_name("btnI")
        lucky_button.click()
        self.assertEqual(self.driver.current_url, "https://www.google.com/search?q=java+tutorials&btnI=I")

    def test_empty_query(self):
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element_by_name("q")
        search_box.clear()
        lucky_button = self.driver.find_element_by_name("btnI")
        lucky_button.click()
        self.assertEqual(self.driver.current_url, "https://www.google.com/search?q=&btnI=I")

    def test_special_characters(self):
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element_by_name("q")
        search_box.send_keys("java! tutorials")
        lucky_button = self.driver.find_element_by_name("btnI")
        lucky_button.click()
        self.assertEqual(self.driver.current_url, "https://www.google.com/search?q=java%21+tutorials&btnI=I")

    def test_invalid_url(self):
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element_by_name("q")
        search_box.send_keys("java tutorials")
        lucky_button = self.driver.find_element_by_name("btnI")
        lucky_button.click()
        try:
            self.driver.get("https://www.example.com/search?q=<user_query>&btnI=I"):
                self.fail("Expected an error page or 404 Not Found")
        except Exception as e:
            self.assertIn("Error", str(e))

    def test_malformed_query(self):
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element_by_name("q")
        search_box.send_keys("//java tutorials")
        lucky_button = self.driver.find_element_by_name("btnI")
        lucky_button.click()
        try:
            WebDriverWait(self.driver, 5).until(EC.title_contains("400 Bad Request"))
        except Exception:
            self.fail("Expected a 400 Bad Request error page")

    def test_button_disabled(self):
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element_by_name("q")
        search_box.send_keys("java tutorials")
        lucky_button = self.driver.find_element_by_name("btnI")
        self.driver.execute_script("arguments[0].disabled = true;", lucky_button)
        try:
            lucky_button.click()
        except Exception:
            pass
        else:
            self.fail("Expected the button to be not clickable")

if __name__ == "__main__":
    unittest.main()
```
Note:

* I've assumed that the "I'm Feeling Lucky" button is named "btnI". You might need to adjust this.
* In the `test_invalid_url` and `test_malformed_query` tests, I've used try-except blocks to catch the expected errors. You can modify this to suit your needs.
* The `test_button_disabled` test uses JavaScript to disable the button. This might not be the most realistic scenario, but it should give you an idea of how to test this case.

Remember to install the required packages (`selenium`, `unittest`) and ensure you have the correct chromedriver executable in your system's PATH.
