### Currency Converter - Python Tkinter App

**Currency_Converter** is a Python-based graphical application built with `customtkinter` that enables users to convert currencies in real time using live exchange rates from [FreeCurrencyAPI](https://freecurrencyapi.com/). The app provides a simple, interactive interface and supports clean UI theming and error handling.

---

## What does the program do?

The application helps users:
- Convert any supported currency to another
- Access real-time exchange rates via API
- View clean, responsive GUI with dark theme
- Easily interact through dropdowns, input fields, and a convert button

---

## Main Window

- The top header contains a title and a green-themed banner with a modern UI style
- A numeric entry field allows the user to input the amount to convert
- Two dropdown menus let the user choose the **source** and **target** currencies
- A green "Convert" button triggers the currency conversion process
- The result is shown clearly in the bottom section (formatted nicely)

---

## Preview

![Screenshot 2025-06-12 213327](https://github.com/user-attachments/assets/e121b5ed-d16d-4fa8-9dff-9149547e6414)
 
---

## Functional Modules

### Currency Converter

- Ensures valid numeric input (int or float)
- Dropdowns are populated with currency codes and descriptions (e.g., USD - US Dollar $)
- Convert button sends a live request to FreeCurrencyAPI
- Conversion result is dynamically displayed in readable format:
100.0000 GBP
128.7400 USD

---

## Technical Stack

- `Python 3.10+`
- `customtkinter` for GUI
- `requests` for API communication
- `dotenv` for managing API key securely
- `Pillow` for image handling

---

## Real-Time Exchange Rate API 

We use [FreeCurrencyAPI](https://freecurrencyapi.com/) to fetch the latest rates. The base URL looks like:

"http
https://api.freecurrencyapi.com/v1/latest?apikey=YOUR_API_KEY&base_currency=USD"

---

## Features

-Real-time currency conversion
-Dark-themed, responsive GUI
-Secure API key management
-Modular code structure
-Input validation and error handling

---

 ## Possible Enhancements
-Add currency rate history chart using Matplotlib
-Support for offline fallback with cached last known rates
-Add theme switching (light/dark)
-Include a conversion history log in GUI

---

## Features video

https://github.com/user-attachments/assets/b8c9c009-d4a7-4c81-81c3-3088982f68b0


























