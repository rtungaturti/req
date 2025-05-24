# Test Cases for Requirement
## Requirement: REQ-102 PayU Payments and Nimbbl state that a cancelled cheque or a bank statement is needed to verify the business's bank account.

### Positive Test Cases:
**

1. **Valid Bank Statement**
	* Input: Scanned copy of a bank statement with the business's name and account number matching the details provided during registration.
	* Expected Result: The system accepts the document and verifies the business's bank account.
2. **Valid Cancelled Cheque**
	* Input: Scanned copy of a cancelled cheque bearing the business's name, account number, and a visible cancellation stamp.
	* Expected Result: The system accepts the document and verifies the business's bank account.
3. **Both Documents Provided**
	* Input: Copies of both a cancelled cheque and a bank statement, with matching business details.
	* Expected Result: The system accepts both documents and verifies the business's bank account.

**

### Negative Test Cases:
**

1. **Invalid Document Type**
	* Input: Scanned copy of a utility bill or any other document not specified in the requirement.
	* Expected Result: The system rejects the document and displays an error message indicating that a cancelled cheque or bank statement is required.
2. **Incomplete Document**
	* Input: Scanned copy of a cancelled cheque with the account number or business name partially obscured or illegible.
	* Expected Result: The system rejects the document and displays an error message indicating that the document is incomplete or illegible.
3. **Mismatched Business Details**
	* Input: Scanned copy of a cancelled cheque with a business name or account number that does not match the details provided during registration.
	* Expected Result: The system rejects the document and displays an error message indicating that the document does not match the registered business details.

Generated on: 2025-05-25 05:09:27
