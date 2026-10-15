# Static Code Analysis - Issues and Fixes

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe eval() usage | Security - Medium | 48 | eval() can execute arbitrary Python code. | Replaced eval() with restricted arithmetic expression evaluation. |
| Unsafe pickle deserialization | Security - Medium | 64 | Loading untrusted pickle data can execute malicious code. | Replaced pickle storage with JSON. |
| Hardcoded password | Security - Low | 11 | A password was stored directly in the source code. | Read the password from an environment variable. |
| Shell command execution | Security - High | 68 | os.system() with input can cause command injection. | Replaced shell execution with print(). |
| Weak MD5 hashing | Security - High | 51 | MD5 is unsuitable for secure hashing. | Replaced MD5 with SHA-256. |
| Mutable default argument | Bug | 13 | audit=[] can share state across function calls. | Changed the default to None and initialized a list when needed. |
| Bare exception handler | Bug / Security | 27 | A bare except hides errors. | Removed the broad exception handler and added explicit checks. |
| Weak random number generation | Security - Low | 54 | random.randint() is not intended for security-sensitive values. | Used the secrets module. |
| Missing docstrings | Code quality | Multiple | Functions and the module lacked documentation. | Added module and function docstrings. |
| Naming and formatting violations | Style | Multiple | Function names and line formatting violated conventions. | Used snake_case names and corrected formatting. |

