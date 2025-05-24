# Selenium Test Script for Requirement
# Requirement: REQ-102 PayU Payments and Nimbbl state that a cancelled cheque or a bank statement is needed to verify the business's bank account.
# Generated on: 2025-05-25 05:09:27

Here is a Python Selenium test script for the given requirement:
```python
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the test environment
def setup():
    global driver
    driver = webdriver.Chrome()  # Use Chrome as the web driver

# Teardown
def teardown():
    driver.quit()

# Positive Test Cases
def test_valid_bank_statement():
    # Input: Scanned copy of a bank statement with the business's name and account number matching the details provided during registration.
    driver.get("https://example.com/upload_document")  # Replace with the actual URL
    bank_statement_file = os.path.join(os.getcwd(), "bank_statement.pdf")
    driver.find_element_by_name("document").send_keys(bank_statement_file)
    driver.find_element_by_xpath("//button[text()='Upload']").click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='success']"), "Bank account verified"))

def test_valid_cancelled_cheque():
    # Input: Scanned copy of a cancelled cheque bearing the business's name, account number, and a visible cancellation stamp.
    driver.get("https://example.com/upload_document")  # Replace with the actual URL
    cancelled_cheque_file = os.path.join(os.getcwd(), "cancelled_cheque.pdf")
    driver.find_element_by_name("document").send_keys(cancelled_cheque_file)
    driver.find_element_by_xpath("//button[text()='Upload']").click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='success']"), "Bank account verified"))

def test_both_documents_provided():
    # Input: Copies of both a cancelled cheque and a bank statement, with matching business details.
    driver.get("https://example.com/upload_document")  # Replace with the actual URL
    bank_statement_file = os.path.join(os.getcwd(), "bank_statement.pdf")
    cancelled_cheque_file = os.path.join(os.getcwd(), "cancelled_cheque.pdf")
    driver.find_element_by_name("document").send_keys(bank_statement_file)
    driver.find_element_by_name("document").send_keys(cancelled_cheque_file)
    driver.find_element_by_xpath("//button[text()='Upload']").click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='success']"), "Bank account verified"))

# Negative Test Cases
def test_invalid_document_type():
    # Input: Scanned copy of a utility bill or any other document not specified in the requirement.
    driver.get("https://example.com/upload_document")  # Replace with the actual URL
    utility_bill_file = os.path.join(os.getcwd(), "utility_bill.pdf")
    driver.find_element_by_name("document").send_keys(utility_bill_file)
    driver.find_element_by_xpath("//button[text()='Upload']").click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='error']"), "Invalid document type. Please upload a cancelled cheque or bank statement"))

def test_incomplete_document():
    # Input: Scanned copy of a cancelled cheque with the account number or business name partially obscured or illegible.
    driver.get("https://example.com/upload_document")  # Replace with the actual URL
    incomplete_cheque_file = os.path.join(os.getcwd(), "incomplete_cheque.pdf")
    driver.find_element_by_name("document").send_keys(incomplete_cheque_file)
    driver.find_element_by_xpath("//button[text()='Upload']").click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='error']"), "Document is incomplete or illegible. Please upload a clear and complete document"))

def test_mismatched_business_details():
    # Input: Scanned copy of a cancelled cheque with a business name or account number that does not match the details provided during registration.
    driver.get("https://example.com/upload_document")  # Replace with the actual URL
    mismatched_cheque_file = os.path.join(os.getcwd(), "mismatched_cheque.pdf")
    driver.find_element_by_name("document").send_keys(mismatched_cheque_file)
    driver.find_element_by_xpath("//button[text()='Upload']").click()
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='error']"), "Document does not match registered business details"))

# Run the test cases
if __name__ == "__main__":
    setup()
    test_valid_bank_statement()
    test_valid_cancelled_cheque()
    test_both_documents_provided()
    test_invalid_document_type()
    test_incomplete_document()
    test_mismatched_business_details()
    teardown()
```
Note that you'll need to replace the `https://example.com/upload_document` URL with the actual URL of the web application, and update the file paths and element locators to match your specific test environment. Additionally, you may need to add additional test cases or modify the existing ones to cover specific edge cases or requirements.
