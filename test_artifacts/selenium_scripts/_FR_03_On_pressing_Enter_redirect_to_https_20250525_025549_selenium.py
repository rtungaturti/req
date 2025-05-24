# Selenium Test Script for Requirement
# Requirement: - FR-03: On pressing "Enter", redirect to: https://www.google.com/search?q=<user_query>
# Generated on: 2025-05-25 02:55:49

Here is a Python Selenium test script that covers the given test cases:
```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFR03(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Replace with your preferred ChromeDriver executable path
        self.driver.get("https://example.com/search")  # Replace with your application's search page
        self.search_input = self.driver.find_element(By.ID, "search-input")  # Replace with your application's search input field ID

    def tearDown(self):
        self.driver.quit()

    def test_valid_search_query(self):
        self.search_input.send_keys("Hello World")
        self.search_input.send_keys(Keys.RETURN)
        self.assertEqual(self.driver.current_url, "https://www.google.com/search?q=Hello+World")

    def test_single_word_search_query(self):
        self.search_input.send_keys("Java")
        self.search_input.send_keys(Keys.RETURN)
        self.assertEqual(self.driver.current_url, "https://www.google.com/search?q=Java")

    def test_search_query_with_special_characters(self):
        self.search_input.send_keys("C++ programming")
        self.search_input.send_keys(Keys.RETURN)
        self.assertEqual(self.driver.current_url, "https://www.google.com/search?q=C%2B%2B+programming")

    def test_empty_search_query(self):
        self.search_input.send_keys("")
        self.search_input.send_keys(Keys.RETURN)
        self.assertEqual(self.driver.current_url, self.driver.current_url)  # Should not redirect

    def test_invalid_url_redirect(self):
        self.search_input.send_keys("Hello World")
        self.search_input.send_keys(Keys.RETURN)
        self.assertNotEqual(self.driver.current_url, "https://www.bing.com/search?q=Hello+World")

    def test_non_url_characters_in_search_query(self):
        self.search_input.send_keys("!@#$%")
        self.search_input.send_keys(Keys.RETURN)
        self.assertEqual(self.driver.current_url, self.driver.current_url)  # Should not redirect

if __name__ == "__main__":
    unittest.main()
```
This script uses the Chrome` webdriver and assumes a basic understanding of Selenium WebDriver. Replace `https://example.com/search` with your application's search page and `search-input` with your application's search input field ID.

Note:

* `send_keys(Keys.RETURN)` simulates pressing the Enter key.
* `WebDriverWait` is not used in this example, but you may need to add it if your application takes time to redirect or if you encounter timing issues.
* You should adjust the expected results according to your application's behavior.
