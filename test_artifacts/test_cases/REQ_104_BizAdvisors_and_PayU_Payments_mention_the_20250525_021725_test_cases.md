# Test Cases for Requirement
## Requirement: REQ-104 BizAdvisors and PayU Payments mention the need for proof of the business's registered address.

### Positive Test Cases:
**

* **Test Case 1:** The system asks for proof of business registered address when signing up for PayU Payments and BizAdvisors services.
    * Preconditions: User has not provided proof of business registered address.
    * Steps: 1. User signs up for PayU Payments and BizAdvisors services. 2. System prompts user to provide proof of business registered address.
    * Expected Result: System requires proof of business registered address to complete the sign-up process.
* **Test Case 2:** The system accepts a valid proof of business address (e.g. utility bill, lease agreement) when signing up for PayU Payments and BizAdvisors services.
    * Preconditions: User has a valid proof of business registered address.
    * Steps: 1. User signs up for PayU Payments and BizAdvisors services. 2. User uploads a valid proof of business registered address.
    * Expected Result: System accepts the valid proof of business registered address and completes the sign-up process.

**

### Negative Test Cases:
**

* **Test Case 1:** The system allows sign-up for PayU Payments and BizAdvisors services without providing proof of business registered address.
    * Preconditions: User has not provided proof of business registered address.
    * Steps: 1. User signs up for PayU Payments and BizAdvisors services. 2. User does not provide proof of business registered address.
    * Expected Result: System should not allow sign-up to complete without proof of business registered address.
* **Test Case 2:** The system accepts an invalid proof of business registered address (e.g. photo of a pet) when signing up for PayU Payments and BizAdvisors services.
    * Preconditions: User has an invalid proof of business registered address.
    * Steps: 1. User signs up for PayU Payments and BizAdvisors services. 2. User uploads an invalid proof of business registered address.
    * Expected Result: System should not accept the invalid proof of business registered address and prevent sign-up completion.
* **Test Case 3:** The system does not prompt for proof of business registered address when signing up for PayU Payments and BizAdvisors services.
    * Preconditions: User has not provided proof of business registered address.
    * Steps: 1. User signs up for PayU Payments and BizAdvisors services.
    * Expected Result: System should prompt for proof of business registered address.

Generated on: 2025-05-25 02:17:25
