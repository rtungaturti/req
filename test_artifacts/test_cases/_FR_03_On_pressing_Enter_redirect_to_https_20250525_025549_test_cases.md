# Test Cases for Requirement
## Requirement: - FR-03: On pressing "Enter", redirect to: https://www.google.com/search?q=<user_query>

### Positive Test Cases:
**

These test cases verify that the system redirects to the correct URL when the "Enter" key is pressed.

1. **Valid Search Query**
	* Input: Enter "Hello World" in the search input field and press "Enter".
	* Expected Result: The system redirects to "https://www.google.com/search?q=Hello+World".
2. **Single Word Search Query**
	* Input: Enter "Java" in the search input field and press "Enter".
	* Expected Result: The system redirects to "https://www.google.com/search?q=Java".
3. **Search Query with Special Characters**
	* Input: Enter "C++ programming" in the search input field and press "Enter".
	* Expected Result: The system redirects to "https://www.google.com/search?q=C%2B%2B+programming".

**

### Negative Test Cases:
**

These test cases verify that the system does not redirect to an incorrect URL or behaves unexpectedly when the "Enter" key is pressed.

1. **Empty Search Query**
	* Input: Enter an empty string in the search input field and press "Enter".
	* Expected Result: The system does not redirect to any URL or displays an error message.
2. **Invalid URL Redirect**
	* Input: Enter "Hello World" in the search input field and press "Enter".
	* Expected Result: The system does not redirect to "https://www.bing.com/search?q=Hello+World" (instead of Google).
3. **Non-URL Characters in Search Query**
	* Input: Enter "!@#$%" in the search input and press "Enter".
	* Expected Result: The system does not redirect to an invalid URL or displays an error message.

Note: These test cases are just examples and may need to be modified or extended based on the specific requirements of the system being tested.

Generated on: 2025-05-25 02:55:49
