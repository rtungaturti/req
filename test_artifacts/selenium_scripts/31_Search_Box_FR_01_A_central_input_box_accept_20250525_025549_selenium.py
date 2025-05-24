# Selenium Test Script for Requirement
# Requirement: 3.1 Search Box - FR-01: A central input box accepts text.
# Generated on: 2025-05-25 02:55:49

Here is a Python Selenium test script that covers the requirement and test cases:
```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSearchBox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Replace with your preferred web driver
        self.driver.get("https://your-web-app-url.com")  # Replace with your web app URL
        self.search_box = self.driver.find_element_by_css_selector("#search-box")  # Replace with the actual search box selector

    def tearDown(self):
        self.driver.quit()

    def test_valid_input(self):
        self.search_box.send_keys("Hello World")
        self.assertEqual(self.search_box.get_attribute("value"), "Hello World")

    def test_empty_input(self):
        self.search_box.send_keys("")
        self.assertEqual(self.search_box.get_attribute("value"), "")

    def test_special_characters(self):
        self.search_box.send_keys("!@#$%^&*()_-+")
        self.assertEqual(self.search_box.get_attribute("value"), "!@#$%^&*()_-+")

    def test_invalid_character(self):
        self.search_box.send_keys("÷")
        error_message = self.driver.find_element_by_css_selector("#search-box-error")
        self.assertIsNotNone(error_message)

    def test_excessive_length(self):
        long_text = "a"  # Replace with an extremely long text
        self.search_box.send_keys(long_text)
        error_message = self.driver.find_element_by_css_selector("#search-box-error")
        self.assertIsNotNone(error_message)

    def test_non_text_input(self):
        # This test case is tricky to implement as Selenium can only send text inputs. 
        # You may need to use a different approach, such as using a file input element.
        pass

if __name__ == "__main__":
    unittest.main()
```
Note:

* Replace the `https://your-web-app-url.com` with your actual web application URL.
* Replace the `#search-box` selector with the actual selector for your search box element.
* In the `test_invalid_character` method, you may need to adjust the error message selector `#search-box-error` to match your application's error message element.
* In the `test_excessive_length` method, you may need to adjust the error message selector `#search-box-error` to match your application's error message element.
* The `test_non_text_input` method is currently not implemented, as it's challenging to test non-text inputs using Selenium. You may need to explore alternative approaches.

Run the script using `python -m unittest test_script.py` (replace `test_script.py` with your script file name).
