# Kodbud_Tasks
# Kodbud Python Mini-Projects

A collection of foundational Python scripts demonstrating core programming concepts, command-line interfaces (CLI), and API integrations. 

## 🚀 Projects Included

### 1. Password Strength Checker
A script that validates user passwords against standard security criteria using regular expressions (`re`).
* **Criteria Checked:** Minimum 8 characters, at least one uppercase letter, one number, and one special character.
* **Key Concepts:** Regular expressions, string evaluation, conditional feedback loop.

### 2. Simple Calculator (CLI)
A command-line calculator that handles basic arithmetic operations with built-in error handling.
* **Operations:** Addition (`+`), Subtraction (`-`), Multiplication (`*`), and Division (`/`).
* **Key Concepts:** Functions, user input casting, division-by-zero validation.

### 3. Simple Chatbot (CLI)
An interactive terminal chatbot that parses user inputs and responds to specific commands.
* **Features:** Built-in string normalization to handle mixed casing and an explicit exit condition (`bye`).
* **Key Concepts:** Infinite loop handling (`while True`), control flow, text matching.

### 4. Weather App (Console)
A practical script that connects to the OpenWeatherMap API to fetch real-time weather data for any city.
* **Features:** Displays temperature (°C), humidity (%), and weather descriptions. Includes status code handling for unauthorized keys (`401`) and unknown cities (`404`).
* **Key Concepts:** `requests` library, JSON parsing, API error handling, `try-except` blocks.

---

## 🛠️ Prerequisites

The **Weather App** requires the third-party `requests` library. You can install it using pip:

```bash
pip install requests
