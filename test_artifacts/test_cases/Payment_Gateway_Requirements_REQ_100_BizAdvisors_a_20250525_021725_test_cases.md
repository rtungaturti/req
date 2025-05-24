# Test Cases for Requirement
## Requirement: Payment Gateway Requirements REQ-100 BizAdvisors and Corpseed specify that a copy of the Certificate of Incorporation (COI) from the Registrar of Companies (ROC) is required.

### Positive Test Cases:
**

**Test Case 1: Valid COI from ROC**

* Input: A scanned copy of the Certificate of Incorporation (COI) from the Registrar of Companies (ROC) in PDF format.
* Expected Output: The payment gateway accepts the uploaded COI and proceeds with the payment process.

**Test Case 2: COI with All Required Details**

* Input: A COI document that contains all the required details such as company name, registration number, date of incorporation, and registered office address.
* Expected Output: The payment gateway verifies the details and accepts the uploaded COI, allowing the payment process to continue.**

**Test Case 3: COI from ROC in Accepted File Format**

* Input: A COI document in a format accepted by the payment gateway (e.g. PDF, JPEG, or PNG).
* Expected Output: The payment gateway accepts the uploaded COI and allows the payment process to proceed.

**

### Negative Test Cases:
**

**Test Case 1: Invalid COI**

* Input: A fake or tampered COI document that is not issued by the Registrar of Companies (ROC).
* Expected Output: The payment gateway rejects the uploaded COI and displays an error message indicating that the document is invalid.

**Test Case 2: COI from Unauthorised Source**

* Input: A COI document obtained from an unauthorised source, such as a self-attested copy or a document from an unrecognised authority.
* Expected Output: The payment gateway rejects the uploaded COI and displays an error message indicating that the document is not from a valid source.

**Test Case 3: COI in Unsupported File Format**

* Input: A COI document in a file format not supported by the payment gateway (e.g. DOC, TXT, or BMP).
* Expected Output: The payment gateway rejects the uploaded COI and displays an error message indicating that the file format is not supported.

Generated on: 2025-05-25 02:17:25
