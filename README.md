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

## Usage Guide
- Enter an amount
- Select "From" and "To" currencies
- Click Convert
- Get real-time results displayed instantly

---

Get real-time results displayed instantly
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

["https://api.freecurrencyapi.com/v1/latest?apikey=YOUR_API_KEY&base_currency=USD"](https://api.freecurrencyapi.com/v1/)

---

## Features

- Real-time currency conversion
- Dark-themed, responsive GUI
- Secure API key management
- Modular code structure
- Input validation and error handling

---

 ## Possible Enhancements
- Add currency rate history chart using Matplotlib
- Support for offline fallback with cached last known rates
- Add theme switching (light/dark)
- Include a conversion history log in GUI

---

## Features video

https://github.com/user-attachments/assets/b8c9c009-d4a7-4c81-81c3-3088982f68b0

---

### Screenshots

---
## Currency Converter tab

![image](https://github.com/user-attachments/assets/9fbdd93a-9f8a-4b58-812e-378b568994da)

---

## Conversion

![Screenshot 2025-06-12 214042](https://github.com/user-attachments/assets/b96b48a8-e976-46d8-8a52-4b78e9869528)

---

### Possible Input Errors & Validations

---

## Invalid Input: Non-numeric Characters
- Description: Displayed when the user enters alphabets or special characters instead of numbers.
- Example: Input = abc, @#%.

![Screenshot 2025-06-12 213612](https://github.com/user-attachments/assets/eefe4296-b229-4267-b20a-fad4aa0a43fc)

---

##  Invalid Input: Characters with Operators

- Description: Displayed when the user enters a mix of characters and operators.
- Example: 12+abc, --10.

![Screenshot 2025-06-12 213730](https://github.com/user-attachments/assets/14b6f4bf-67a3-4946-bf38-7d6490fd01cb)

---

## Invalid Input: Negative Amount

- Description: Negative values are not allowed for currency conversion.
- Example: Input = -100.

![Screenshot 2025-06-12 213833](https://github.com/user-attachments/assets/31b48add-31b2-41ca-9265-f3b4f4e1ea1e)

---

## Logical Error: Same 'From' and 'To' Currencies

- Description: Prevents conversion when the source and target currencies are identical.
- Example: From = USD, To = USD.

![Screenshot 2025-06-12 213937](https://github.com/user-attachments/assets/cb821d69-4dcd-4a06-940a-88f821e436e6)

---

## License
This project is licensed under the MIT License.

---

## Show Your Support

If you like this project, please Star it on GitHub! Contributions and feedback are welcome.

---
































