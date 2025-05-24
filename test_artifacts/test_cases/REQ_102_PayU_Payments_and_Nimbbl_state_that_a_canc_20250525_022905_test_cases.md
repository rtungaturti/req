# Test Cases for Requirement
## Requirement: REQ-102 PayU Payments and Nimbbl state that a cancelled cheque or a bank statement is needed to verify the business's bank account.

### Positive Test Cases:
**

1. **Valid Document Provided**
PayU Payments and Nimbbl receive a cancelled cheque or a bank statement from the business, which matches the business's bank account information. The system verifies the document successfully, and the business's bank account is confirmed.

2. **Legible Document**
PayU Payments and Nimbbl receive a clear and legible cancelled cheque or bank statement from the business. The system is able to read and verify the document successfully, and the business's bank account is confirmed.

3. **Matching Account Information**
PayU Payments and Nimbbl receive a cancelled cheque or bank statement with account information that matches the business's registered account information. The system verifies the document successfully, and the business's bank account is confirmed.

**

### Negative Test Cases:
**

1. **Invalid Document Provided**
PayU Payments and Nimbbl receive a document that is not a cancelled cheque or bank statement from the business. The verification fails, and an error message is displayed.

2. **Illegible Document**
PayU Payments and Nimbbl receive a cancelled cheque or bank statement that is torn, worn out, or otherwise illegible. The system is unable to read the document, and an error message is displayed.

3. **Non-Matching Account Information**
PayU Payments and Nimbbl receive a cancelled cheque or bank statement with account information that does not match the business's registered account information. The system verification fails, and an error message is displayed.

Note: These test cases can be further enhanced by adding specific scenarios, data, or edge cases to cover more possibilities.

Generated on: 2025-05-25 02:29:05
