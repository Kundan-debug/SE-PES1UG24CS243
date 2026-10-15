# Reflection - Static Code Analysis

## 1. What did you learn from static code analysis?

I learned that static code analysis tools can identify code quality, formatting, and security problems without requiring the program to be executed. Pylint checks code quality, Flake8 checks style and formatting, and Bandit identifies common security risks.

## 2. Which tool was most useful, and why?

Bandit was especially useful because it identified security risks such as unsafe eval() usage, insecure hashing, hardcoded credentials, and shell command execution. Pylint and Flake8 also helped improve code readability and maintainability.

## 3. What challenges did you face while fixing the issues?

The main challenge was fixing security vulnerabilities without changing the intended functionality of the program. For example, I replaced eval() with a restricted arithmetic evaluator, pickle with JSON, and MD5 with SHA-256. I also corrected formatting and improved function documentation.

## 4. How do you know the code improved after the fixes?

After making the changes, I reran all three tools. Pylint achieved a score of 10.00/10, Flake8 reported no issues, and Bandit reported no security issues. I also compiled and executed the program to verify that it ran successfully.
