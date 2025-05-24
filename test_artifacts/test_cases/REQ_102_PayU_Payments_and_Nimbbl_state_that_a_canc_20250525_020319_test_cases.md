# Test Cases for Requirement
## Requirement: REQ-102 PayU Payments and Nimbbl state that a cancelled cheque or a bank statement is needed to verify the business's bank account.

### Positive Test Cases:
**

1. **Valid Bank Statement**
	* Pre-condition: User has a valid bank statement document.
	* Steps: Upload bank statement document.
	* Expected Result: Bank account is verified successfully.
3. **Cancelled Cheque with Correct Details**
	* Pre-condition: User has a cancelled cheque with correct bank account details (e.g. account number, IFSC code, etc.).
	* Steps: Upload cancelled cheque document.
	* Expected Result: Bank account is verified successfully.

**

### Negative Test Cases:
**

1. **Invalid Document Type**
	* Pre-condition: User tries to upload an invalid document type (e.g. photo, driver's license, etc.).
	* Steps: Upload invalid document.
	* Expected Result: Error message is displayed, indicating that the document type is not accepted.
2. **Cancelled Cheque with Incorrect Details**
	* Pre-condition: User has a cancelled cheque with incorrect or incomplete bank account details.
	* Steps: Upload cancelled cheque document with incorrect details.
	* Expected Result: Error message is displayed, indicating that the document details are incorrect.
3. **No Document Uploaded**
	* Pre-condition: User doesn't upload any supporting the bank account verification.
	* Steps: Try to complete the verification process without uploading a document.
	* Expected Result: Error message is displayed, indicating that a document is required for verification.

Generated on: 2025-05-25 02:03:19
