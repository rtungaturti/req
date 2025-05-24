# Selenium Test Script for Requirement
# Requirement: REQ-102 PayU Payments and Nimbbl state that a cancelled cheque or a bank statement is needed to verify the business's bank account.
# Generated on: 2025-05-25 02:29:05

Here is a Python Selenium test script that covers the test cases mentioned:
```python
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up the test environment
 chrome_options = webdriver.ChromeOptions()
 chrome_options.add_argument("--headless")
 chrome_options.add_argument("--disable-gpu")
 driver = webdriver.Chrome(options=chrome_options")

# Set up the test data
cancelled_cheque_path = os.path.join(os.getcwd(), "testdata", "cancelled_cheque_file_input = {"file": open(cancelled_cheque_path, "rb")}

bank_statement_path = os.path.join(os.getcwd(), "testdata", "bank_statement.pdf")
bank_statement_file_input = {"file": open(bank_statement_path, "rb")}

invalid_document_path = os.path.join(os.getcwd(), "testdata", "invalid_document.pdf")
invalid_document_file_input = {"file": open(invalid_document_path, "rb")}

# Test Case 1: Valid Document Provided
    def test_valid_document_provided():
        driver.get("https://example.com/business/bank-account-verification")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "document-upload-input")))
        driver.find_element_by_id("document-upload-input").send_keys(cancelled_cheque_file_input["file"].name)
        driver.find_element_by_id("verification-success-message")
        assert True

    # Test Case 2: Legible Document
    def test_legible_document():
        driver.get("https://example.com/business/bank-account-verification")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "document-upload-input")))
        driver.find_element_by_id("document-upload-input").send_keys(bank_statement_file_input["file"].name)
        driver.find_element_by_id("verification-success-message")
        assert True

    # Test Case 3: Matching Account Information
    def test_matching_account_info():
        driver.get("https://example.com/business/bank-account-verification")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "document-upload-input")))
        driver.find_element_by_id("document-upload-input").send_keys(cancelled_cheque_file_input["file"].name)
        driver.find_element_by_id("verification-success-message")
        assert True

    # Test Case 4: Invalid Document Provided
    def test_invalid_document_provided():
        driver.get("https://example.com/business/bank-account-verification")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "document-upload-input")))
        driver.find_element_by_id("document-upload-input").send_keys(invalid_document_file_input["file"].name)
        try:
            driver.find_element_by_id("verification-error-message")
        except TimeoutException:
            assert False, "Verification error message not displayed"

    # Test Case 5: Illegible Document
    def test_illegible_document():
        # Create an illegible document (e.g. a torn or worn out document)
        illegible_document_path = os.path.join(os.getcwd(), "testdata", "illegible_document.pdf")
        illegible_document_file_input = {"file": open(illegible_document_path, "rb")}
        driver.get("https://example.com/business/bank-account-verification")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "document-upload-input")))
        driver.find_element_by_id("document-upload-input").send_keys(illegible_document_file_input["file"].name)
        try:
            driver.find_element_by_id("verification-error-message")
        except TimeoutException:
            assert False, "Verification error message not displayed"

    # Test Case 6: Non-Matching Account Information
    def test_non_matching_account_info():
        # Create a document with non-matching account information
        non_matching_account_document_path = os.path.join(os.getcwd(), "testdata", "non_matching_account_document.pdf")
        non_matching_account_document_file_input = {"file": open(non_matching_account_document_path, "rb")}
        driver.get("https://example.com/business/bank-account-verification")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "document-upload-input")))
        driver.find_element_by_id("document-upload-input").send_keys(non_matching_account_document_file_input["file"].name)
        try:
            driver.find_element_by_id("verification-error-message")
        except TimeoutException:
            assert False, "Verification error message not displayed"

# Run the test cases
if __name__ == "__main__":
    test_valid_document_provided()
    test_legible_document()
    test_matching_account_info()
    test_invalid_document_provided()
    test_illegible_document()
    test_non_matching_account_info()

# Teardown
driver.quit()
```
Note:

* You'll need to replace the `https://example.com/business/bank-account-verification` URL with the actual URL of the application.
* You'll need to create the test data files (e.g. `cheque.pdf`, `bank_statement.pdf`, `invalid_document.pdf`, etc.) and place them in the `testdata` directory.
* You may need to adjust the test cases to fit the specific requirements of your application, such as different file types or different error messages.
* You may want to add more test cases or edge cases to ensure the application's functionality is thoroughly tested.
