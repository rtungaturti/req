# Test Cases for Requirement
## Requirement: FR-05: "I'm Feeling Lucky" button redirects to: https://www.google.com/search?q=<user_query>&btnI=I

### Positive Test Cases:
**

1. **Valid User Query**
	* Input: User enters a valid search query (e.g. "java tutorials") and clicks the "I'm Feeling Lucky" button.
	* Result: The browser redirects to "https://www.google.com?q=java+tutorials&btnI=I" and displays the search result.
2. **Empty Query**
	* Input: User enters an empty search query and clicks the "I'm Feeling Lucky" button.
	* Result: The browser redirects to "https://www.google.com/search?q=&btnI=I" and displays the Google homepage.
3. **Special Characters**
	* Input: User enters a search query with special characters (e.g. "java! tutorials") and clicks the "I'm Feeling Lucky" button.
	* Result: The browser redirects to "https://www.google.com/search?q=java%21+tutorials&btnI=I" and displays the search result.

**

### Negative Test Cases:
**

1. **Invalid URL**
	* Input: User clicks the "I'm Feeling Lucky" button, but the URL is hardcoded to an invalid URL (e.g. "https://www.example.com/search?q=<user_query>&btnI=I").
	* Result: The browser displays an error page or a "404 Not Found" error.
2. **Malformed Query**
	* Input: User enters a malformed search query (e.g. "//java tutorials") and clicks the "I'm Feeling Lucky" button.
	* Result: The browser displays an error page or a "400 Bad Request" error.
3. **Button Disabled**
	* Input: The "I'm Feeling Lucky" button is disabled (e.g. due to a JavaScript error).
	* Result: The button is not clickable, and no redirect occurs when clicked.

Generated on: 2025-05-25 02:55:49
