# 🔐 Password Strength Checker & Security Analyzer

A beginner-friendly **Cyber Security project** developed using Python and Streamlit to analyze password strength, identify common password weaknesses, and provide security recommendations.

## 📌 Project Overview

The Password Strength Checker evaluates passwords based on their length, character combinations, repeated characters, common patterns, and sequential characters.

It classifies passwords as **Weak, Medium, or Strong** and provides recommendations to improve password security.

This project was developed as part of the **NexOrbiX Technologies Cyber Security Internship**.

## 🎯 Objectives

- Understand basic password security concepts.
- Understand why strong passwords are important.
- Identify weak password characteristics.
- Analyze password complexity.
- Practice Python programming.
- Implement input validation.
- Identify common password weaknesses.
- Provide useful security recommendations.
- Understand basic password storage concepts.
- Develop a user-friendly security application.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Framework:** Streamlit
- **Libraries:** string, Streamlit
- **IDE:** Visual Studio Code
- **Platform:** Windows

## ✨ Features

- 🔐 Password input with hidden characters
- 📏 Password length checking
- 🔠 Uppercase and lowercase character detection
- 🔢 Number detection
- 🔣 Special character detection
- 🔁 Repeated character detection
- ⚠️ Common password pattern detection
- 🔍 Sequential character detection
- 📊 Password strength classification
- 📈 Visual strength meter
- 💡 Explanation of the strength result
- 🛡️ Security recommendations
- ✅ Password requirements checklist
- 🛡️ Basic password security tips
- 🗑️ Clear password option
- 🖥️ Interactive Streamlit interface
- ❌ Empty-input validation and error handling

## 📊 Password Strength Classification

The application classifies passwords into three categories based on its rule-based scoring system:

| Strength | Description |
|---|---|
| 🔴 Weak | Password has several basic security weaknesses. |
| 🟡 Medium | Password meets some of the basic security checks. |
| 🟢 Strong | Password meets the application's stronger criteria. |

The classification is a basic assessment and does not guarantee that a password is secure.

## 🔍 Strength Checks

The application checks the following password characteristics:

- Password length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Repeated characters
- Common password patterns
- Sequential characters

## 💡 Why This Result?

After analyzing a password, the application explains why it received its strength classification.

It displays:

- Checks that passed
- Checks that failed
- Areas that need improvement
- The overall strength assessment

This helps users understand how different password characteristics affect the result.

## 🛡️ Security Recommendations

The application provides recommendations based on detected weaknesses.

Examples include:

- Use at least 12 characters.
- Add an uppercase letter.
- Add a lowercase letter.
- Add a number.
- Add a special character.
- Avoid repeated characters.
- Avoid common password patterns.
- Avoid sequential characters.

## 🔒 Password Storage Security

Passwords should never be stored as plain text.

Plain-text password storage means saving the actual password directly in a database or file. If that storage is compromised, the original passwords may be exposed.

For this project, the application does not intentionally save passwords to files or databases. The password is analyzed for security characteristics and is not stored as part of the application.

In real-world applications where passwords need to be stored, an appropriate password-hashing mechanism should be used instead of storing the original password.

### Basic Password Security Practices

- Use long and unique passwords.
- Avoid common words and predictable patterns.
- Avoid reusing passwords across different accounts.
- Do not share passwords with others.
- Do not store passwords as plain text.
- Use appropriate password-hashing methods when passwords must be stored by an application.


## ⚙️ Installation and Setup

### 1. Install Python

Download and install Python from:

https://www.python.org/downloads/

### 2. Clone the repository

```bash
git clone https://github.com/SupriyaMathpati/Password-Strength-Checker.git
```

### 3. Navigate to the project folder

```bash
cd Password-Strength-Checker
```

### 4. Install Streamlit

```bash
python -m pip install streamlit
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser, usually at:

http://localhost:8501

## 📂 Project Structure

```text
Password-Strength-Checker/
│
├── app.py
├── password_checker.py
├── README.md
│
└── screenshots/
    ├── weak.png
    ├── medium.png
    └── strong.png
```

   
File Description
* app.py – Streamlit-based graphical user interface and password analysis logic.
* password_checker.py – Console-based password strength checker.
* README.md – Project documentation.
* screenshots/ – Screenshots demonstrating the application results.

🧪 Testing

The application was tested using dummy passwords with different characteristics.

| Test Case             | Expected Behaviour                         |
| --------------------- | ------------------------------------------ |
| Weak password         | Displays Weak or applicable classification |
| Medium password       | Displays Medium when criteria are met      |
| Strong password       | Displays Strong when criteria are met      |
| Empty input           | Displays a warning                         |
| Repeated characters   | Provides a security recommendation         |
| Common patterns       | Provides a security recommendation         |
| Sequential characters | Provides a security recommendation         |

🔒 Security Considerations

* Passwords are entered locally for analysis.
* The application does not intentionally save passwords to files or databases.
* Password input is hidden in the interface.
* Dummy passwords should be used for testing.
* The application provides basic rule-based analysis and is not a substitute for a dedicated password security assessment.

📸 Screenshots

🔴 Weak Password

🟡 Medium Password

🟢 Strong Password

🎓 Learning Outcomes

* Python programming and conditional statements
* String handling and input validation
* Basic cyber security and password security concepts
* Password characteristic analysis
* Understanding common password weaknesses
* Streamlit application development
* Testing a security-focused application
* Understanding why passwords should not be stored as plain text
* GitHub project management
* Technical project documentation

👩‍💻 Author

Supriya Mathpati
Electronics and Computer Engineering @ VTU CPGS KALABURAGI
Cyber Security Intern – NexOrbiX Technologies

📜 Disclaimer

This project is intended for educational purposes as part of a beginner-level cyber security internship. It is a basic password strength checker and does not guarantee protection against password attacks.

Developed as part of the NexOrbiX Technologies Cyber Security Internship – 2026.