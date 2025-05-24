# Selenium Test Script for Requirement
# Requirement: REQ-102 PayU Payments and Nimbbl state that a cancelled cheque or a bank statement is needed to verify the business's bank account.
# Generated on: 2025-05-25 02:03:19

Here is a sample Python Selenium test script for the given requirement:
```python
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up the web driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

class TestPayUVerification(unittest.TestCase):
    def setUp(self):
        self.driver = driver
        self.driver.get("https://example.com/payu-verification")  # Replace with the actual URL

    def tearDown(self):
        self.driver.quit()

    def test_valid_bank_statement(self):
        # Upload bank statement document
        bank_statement_file = os.path.join(os.path.dirname(__file__), "bank_statement.pdf")
        self.driver.find_element_by_id("bank-statement-upload").send_keys(bank_statement_file)
        
        # Submit the form
        self.driver.find_element_by_id("submit-button").click()
        
        # Verify the account is verified successfully
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "verification-success"))
            )
        except TimeoutException:
            self.fail("Bank account verification failed")

    def test_cancelled_cheque_with_correct_details(self):
        # Upload cancelled cheque document
        cancelled_cheque_file = os.path.join(os.path.dirname(__file__), "cancelled_cheque.pdf")
        self.driver.find_element_by_id("cancelled-cheque-upload").send_keys(cancelled_cheque_file)
        
        # Submit the form
        self.driver.find_element_by_id("submit-button").click()
        
        # Verify the account is verified successfully
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "verification-success"))
            )
        except TimeoutException:
            self.fail("Bank account verification failed")

    def test_invalid_document_type(self):
        # Upload an invalid document type
        invalid_document_file = os.path.join(os.path.dirname(__file__), "invalid_document.jpg")
        self.driver.find_element_by_id("bank-statement-upload").send_keys(invalid_document_file)
        
        # Submit the form
        self.driver.find_element_by_id("submit-button").click()
        
        # Verify an error message is displayed
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "error-message"))
            )
        except TimeoutException:
            self.fail("Error message not displayed")

    def test_cancelled_cheque_with_incorrect_details(self):
        # Upload cancelled cheque document with incorrect details
        incorrect_cancelled_cheque_file = os.path.join(os.path.dirname(__file__), "incorrect_cancelled_cheque.pdf")
        self.driver.find_element_by_id("cancelled-cheque-upload").send_keys(incorrect_cancelled_cheque_file)
        
        # Submit the form
        self.driver.find_element_by_id("submit-button").click()
        
        # Verify an error message is displayed
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "error-message"))
            )
        except TimeoutException:
            self.fail("Error message not displayed")

    def test_no_document_uploaded(self):
        # Try to complete the verification process without uploading a document
        self.driver.find_element_by_id("submit-button").click()
        
        # Verify an error message is displayed
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "error-message"))
            )
        except TimeoutException:
            self.fail("Error message not displayed")

if __name__ == "__main__":
    unittest.main()
```
This script assumes that the web application has the following elements:

* A file input element with an ID of "bank-statement-upload" for uploading a bank statement document.
* A file input element with an ID of "cancelled-cheque-upload" for uploading a cancelled cheque document.
* A submit button with an ID of "submit-button".
* An error message element with an ID of "error-message" that is displayed when an invalid document is uploaded or no document is uploaded.
* A success message element with an ID of "verification-success" that is displayed when the bank account verification is successful.

Replace the `https://example.com/payu-verification` URL with the actual URL of the web application. Also, make sure to update the file paths and IDs to match the actual web application.

Note that this script uses the `headless` mode to run the Chrome browser in the background. If you want to run the script in a visible mode, remove the `chrome_options.add_argument("--headless")` line.
