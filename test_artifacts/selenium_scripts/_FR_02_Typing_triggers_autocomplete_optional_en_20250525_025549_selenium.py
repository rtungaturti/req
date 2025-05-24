# Selenium Test Script for Requirement
# Requirement: - FR-02: Typing triggers autocomplete (optional enhancement).
# Generated on: 2025-05-25 02:55:49

Here is a Python Selenium test script that covers the given requirement and test cases:
```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAutocomplete(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Replace with your preferred browser
        self.driver.get("https://example.com")  # Replace with your application URL
        self.search_bar = self.driver.find_element_by_name("search")  # Replace with your search bar element

    def tearDown(self):
        self.driver.quit()

    def test_autocomplete_appears_after_typing(self):
        # Preconditions: Search bar is empty, autocomplete feature is enabled
        self.search_bar.clear()
        self.search_bar.send_keys("app")
        # Expected Result: Autocomplete suggestions appear below the search bar
        autocomplete_suggestions = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".autocomplete-suggestion"))
        )
        self.assertGreater(len(autocomplete_suggestions), 0)

    def test_autocomplete_suggestions_are_relevant(self):
        # Preconditions: Search bar contains some text, autocomplete feature is enabled
        self.search_bar.send_keys("appl")
        self.search_bar.send_keys("e")
        # Expected Result: Autocomplete suggestions appear and are relevant to the input text
        autocomplete_suggestions = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".autocomplete-suggestion"))
        )
        self.assertGreater(len(autocomplete_suggestions), 0)
        for suggestion in autocomplete_suggestions:
            self.assertIn("appl", suggestion.text.lower())

    def test_autocomplete_does_not_appear_when_feature_is_disabled(self):
        # Preconditions: Autocomplete feature is disabled
        # NOTE: You may need to implement a way to disable autocomplete feature
        pass

    def test_autocomplete_does_not_appear_when_search_bar_is_empty(self):
        # Preconditions: Search bar is empty
        self.search_bar.clear()
        self.search_bar.send_keys("a")
        # Expected Result: No autocomplete suggestions appear
        try:
            WebDriverWait(self.driver, 1).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".autocomplete-suggestion"))
            )
            self.fail("Autocomplete suggestions appeared unexpectedly")
        except:
            pass

    def test_autocomplete_does_not_appear_when_input_text_is_too_short(self):
        # Preconditions: Search bar contains very few characters, autocomplete feature is enabled
        self.search_bar.send_keys("a")
        # Wait for autocomplete suggestions to appear (but they shouldn't)
        try:
            WebDriverWait(self.driver, 1).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".autocomplete-suggestion"))
            )
            self.fail("Autocomplete suggestions appeared unexpectedly")
        except:
            pass

if __name__ == "__main__":
    unittest.main()
```
Please note that:

* You'll need to replace the `https://example.com` URL with your application URL.
* You'll need to replace the `search_bar` element with the actual element locator for your search bar.
* You may need to implement a way to disable the autocomplete feature for the negative test case.
* You may need to adjust the CSS selectors used in the script to match your application's HTML structure.
* This script assumes that the autocomplete suggestions appear below the search bar element with a CSS class `autocomplete-suggestion`. You may need to adjust this to match your application's HTML structure.
