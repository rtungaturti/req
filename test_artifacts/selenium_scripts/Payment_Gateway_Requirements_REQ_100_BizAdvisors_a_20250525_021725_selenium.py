# Selenium Test Script for Requirement
# Requirement: Payment Gateway Requirements REQ-100 BizAdvisors and Corpseed specify that a copy of the Certificate of Incorporation (COI) from the Registrar of Companies (ROC) is required.
# Generated on: 2025-05-25 02:17:25

Here is a Python Selenium test script that covers the positive and negative test cases:
```
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Set up the web driver
def setup():
    global driver
    driver = webdriver.Chrome()  # Use Chrome driver
    driver.maximize_window()  # Maximize the window
def teardown():
    driver.quit()  # Close the browser

# Test Case 1: Valid COI from ROC
def test_valid_COI_from_ROC():
    driver.get("https://example.com/payment-gateway")  # replace with the actual URL
    upload_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "upload-button")))
    upload_button.send_keys(os.getcwd() + "/test_COI_from_ROC.pdf")
    time.sleep(2)  # wait for the upload to complete
    assert driver.find_element_by_css_selector(".payment-processing").is_displayed()

# Test Case 2: COI with All Required Details
def test_COI_with_required_details():
    driver.get("https://example.com/payment-gateway")  # replace with the actual URL
    upload_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "upload-button")))
    upload_button.send_keys(os.getcwd() + "/test_COI_with_required_details.pdf")
    time.sleep(2)  # wait for the upload to complete
    assert driver.find_element_by_css_selector(".payment-processing").is_displayed()

# Test Case 3: COI from ROC in Accepted File Format
def test_COI_in_accepted_file_format():
    driver.get("https://example.com/payment-gateway")  # replace with the actual URL
    upload_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "upload-button")))
    upload_button.send_keys(os.getcwd() + "/test_COI_in_accepted_file_format.pdf")
    time.sleep(2)  # wait for the upload to complete
    assert driver.find_element_by_css_selector(".payment-processing").is_displayed()

# Test Case 1: Invalid COI
def test_invalid_COI():
    driver.get("https://example.com/payment-gateway")  # replace with the actual URL
    upload_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "upload-button")))
    upload_button.send_keys(os.getcwd() + "/test_invalid_COI.pdf")
    time.sleep(2)  # wait for the upload to complete
    assert driver.find_element_by_css_selector(".error-message").is_displayed()

# Test Case 2: COI from Unauthorised Source
def test_COI_from_unauthorised_source():
    driver.get("https://example.com/payment-gateway")  # replace with the actual URL
    upload_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "upload-button")))
    upload_button.send_keys(os.getcwd() + "/test_COI_from_unauthorised_source.pdf")
    time.sleep(2)  # wait for the upload to complete
    assert driver.find_element_by_css_selector(".error-message").is_displayed()

# Test Case 3: COI in Unsupported File Format
def test_COI_in_unsupported_file_format():
    driver.get("https://example.com/payment-gateway")  # replace with the actual URL
    upload_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "upload-button")))
    upload_button.send_keys(os.getcwd() + "/test_COI_in_unsupported_file_format.doc")
    time.sleep(2)  # wait for the upload to complete
    assert driver.find_element_by_css_selector(".error-message").is_displayed()

# Run the test cases
setup()
test_valid_COI_from_ROC()
test_COI_with_required_details()
test_COI_in_accepted_file_format()
test_invalid_COI()
test_COI_from_unauthorised_source()
test_COI_in_unsupported_file_format()
teardown()
```
Note:

* Replace `https://example.com/payment-gateway` with the actual URL of the payment gateway.
* Place the test files (e.g. `test_COI_from_ROC.pdf`, `test_COI_with_required_details.pdf`, etc.) in the same directory as the script.
* Make sure the script has the necessary permissions to upload files.
* The script uses the `selenium` library to interact with the web driver (Chrome).
* The script uses `WebDriverWait` to wait for the upload to complete before asserting the expected output.

Also, please make sure to handle any exceptions that may occur during the test execution.
