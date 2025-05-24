# Test Cases for Requirement
## Requirement: REQ-103 Corpseed and PayU Payments highlight the requirement for a Goods and Services Tax (GST) registration certificate.

### Positive Test Cases:
**

1. **Valid GST Registration Certificate**
	* Preconditions: User has a valid GST registration certificate.
	* Steps: Corpseed and PayU Payments request GST registration certificate, user uploads a valid certificate.
	* Expected Result: The system accepts the certificate and allows the user to proceed.
2. **GST Registration Certificate with Correct Format**
	* Preconditions: User has a GST registration certificate in the correct format (e.g. PDF, JPEG).
	* Steps: Corpseed and PayU Payments request GST registration certificate, user uploads a certificate in the correct format.
	* Expected Result: The system accepts the certificate and allows the user to proceed.

**

### Negative Test Cases:
**

1. **Invalid GST Registration Certificate**
	* Preconditions: User has an invalid or expired GST registration certificate.
	* Steps: Corpseed and PayU Payments request GST registration certificate, user uploads an invalid certificate.
	* Expected Result: The system rejects the certificate and displays an error message.
2. **No GST Registration Certificate**
	* Preconditions: User does not have a GST registration certificate.
	* Steps: Corpseed and PayU Payments request GST registration certificate, user does not upload a certificate.
	* Expected Result: The system displays an error message and does not allow the user to further.
3. **GST Registration Certificate in Incorrect Format**
	* Preconditions: User has a GST registration certificate in an incorrect format (e.g. docx, txt).
	* Steps: Corpseed and PayU Payments request GST registration certificate, user uploads a certificate in an incorrect format.
	* Expected Result: The system rejects the certificate and displays an error message.

Let me know if you need any further clarification!

Generated on: 2025-05-25 05:19:24
