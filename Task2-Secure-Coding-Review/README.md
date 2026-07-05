#### **#Secure Coding Review–Python Login System**





###### **Project Overview:**

This project demonstrates a security audit of a Python-based Login System. The application was reviewed using manual code inspection and static analysis techniques to identify security vulnerabilities and recommend secure coding practices.





###### **Objectives:**

* Perform a secure coding review of a Python application.
* Identify security vulnerabilities in the source code.
* Analyze risks associated with insecure coding practices.
* Recommend remediation measures to improve security.





###### **Application Details:**

* Programming Language: Python
* Application Type: Login System





###### **Vulnerabilities Identified:**

* Hardcoded Password
* Plain Text Password Input
* No Input Validation
* Unlimited Login Attempts





###### **Security Analysis Tool:**

* Bandit (Python Static Code Security Analyzer)





###### **Findings:**

Bandit analysis detected the presence of a hardcoded password in the source code, highlighting a potential security risk that could expose sensitive credentials.





###### **Remediation Recommendations:**

* Use password hashing for credential storage.
* Implement secure password input methods.
* Validate and sanitize all user inputs.
* Restrict failed login attempts to prevent brute-force attacks.
* Follow secure coding best practices.





###### **Project Files:**

* vulnerable\_login.py
* secure\_login.py
* Secure\_Coding\_Review\_Report.docx
* bandit\_scan\_result.png
* login\_output.png





###### **Conclusion:**

The review identified multiple security weaknesses within the application. Implementing the recommended security controls can significantly improve the overall security posture of the login system and reduce the risk of unauthorized access.

