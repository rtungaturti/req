# Test Cases for Requirement
## Requirement: Payment Gateway Requirements REQ-100 BizAdvisors and Corpseed specify that a copy of the Certificate of Incorporation (COI) from the Registrar of Companies (ROC) is required.

### Positive Test Cases:
**
Validate that a valid COI from the ROC is accepted.

1. Test Case: Valid COI with correct details
   - Upload a COI with the correct company name, ROC number, and date of incorporation.
   - Expected Result: The system accepts the COI and mark it as verified.

2. Test Case: COI with minor formatting issues
   - Upload a COI with minor formatting issues, such as extra spaces or different font sizes.
   - Expected Result: The system accepts the COI and marks it as verified, ignoring minor formatting issues.

3. Test Case: COI with different file formats
   - Upload a COI in different file formats, such as PDF, JPEG, or PNG.
   - Expected Result: The system accepts the COI in different file formats and marks it as verified.

**

### Negative Test Cases:
**
Validate that an invalid COI from the ROC is not accepted.

1. Test Case: COI with invalid company name
   - Upload a COI with an incorrect company name.
   - Expected Result: The system rejects the COI and displays an error message.

2. Test Case: COI with expired date
   - Upload a COI with an expired date of incorporation.
   - Expected Result: The system rejects the COI and displays an error message.

3. Test Case: COI from an unauthorized source
   - Upload a COI from a source other than the ROC.
   - Expected Result: The system rejects the COI and displays an error message.

These test cases cover different scenarios to ensure that the system behaves correctly when validating a COI from the ROC.

Generated on: 2025-05-25 02:03:19
