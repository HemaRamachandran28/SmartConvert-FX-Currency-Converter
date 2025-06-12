# --- Import the required libraries / modules:
from customtkinter import *
from PIL import ImageTk
from tkinter import messagebox

from modules.env.env_vars import load_env_vars
from modules.currency.currency_list import currencies
from modules.currency.convert import convert_currency, check_value_is_numeric
from modules.image_check.image_check import check_image_present

import os


def main() -> None:
    """Main function for the Currency Converter app."""

    load_env_vars()
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))

    # Check for images
    icon_check = check_image_present(
        image_path=f"{BASE_DIR}/images/icon.png",
        error_message="Check that the icon file exists as icon.png."
    )
    header_check = check_image_present(
        image_path=f"{BASE_DIR}/images/header.png",
        error_message="Check that the header file exists as header.png."
    )

    app_name = "Currency Converter"
    default_font_size = 18

    # Setup the window
    app = CTk()
    app.title(app_name)
    app.geometry("380x650")
    app.resizable(False, False)

    icon = ImageTk.PhotoImage(icon_check)
    app.wm_iconphoto(True, icon)
    app.wm_iconbitmap()

    from_currency = StringVar()
    to_currency = StringVar()

    # --- Header Image ---
    header_image = CTkImage(light_image=header_check, dark_image=header_check, size=(350, 100))
    header_label = CTkLabel(app, width=350, height=100, text=app_name, font=("", 28), image=header_image, text_color="white")
    header_label.grid(row=0, column=0, padx=10, pady=(10, 5))

    # --- Value Entry Frame ---
    value_frame = CTkFrame(app, width=350)
    value_frame.grid(row=1, column=0, padx=15, pady=(5, 10))

    CTkLabel(value_frame, text="Convert:", font=("", default_font_size), anchor="w").pack(anchor="w", pady=(10, 2), padx=10)
    value_entry = CTkEntry(value_frame, width=320, placeholder_text="Enter a number to convert", font=("", default_font_size), justify=CENTER)
    value_entry.pack(padx=10, pady=(0, 10))

    # --- From Currency Frame ---
    from_frame = CTkFrame(app, width=350)
    from_frame.grid(row=2, column=0, padx=15, pady=(0, 10))

    CTkLabel(from_frame, text="From:", font=("", default_font_size), anchor="w").pack(anchor="w", pady=(10, 2), padx=10)
    from_currency_code = CTkComboBox(from_frame, width=320, values=currencies, font=("", default_font_size), variable=from_currency, state="readonly")
    from_currency_code.pack(padx=10, pady=(0, 10))
    from_currency_code.set(currencies[0])

    # --- To Currency Frame ---
    to_frame = CTkFrame(app, width=350)
    to_frame.grid(row=3, column=0, padx=15, pady=(0, 10))

    CTkLabel(to_frame, text="To:", font=("", default_font_size), anchor="w").pack(anchor="w", pady=(10, 2), padx=10)
    to_currency_code = CTkComboBox(to_frame, width=320, values=currencies, font=("", default_font_size), variable=to_currency, state="readonly")
    to_currency_code.pack(padx=10, pady=(0, 10))
    to_currency_code.set(currencies[1])

    # --- Output Label ---
    to_currency_value = CTkLabel(app, width=320, text="The converted amount\nwill be shown here.", font=("", default_font_size), justify=CENTER)
    to_currency_value.grid(row=4, column=0, padx=10, pady=(10, 15))

    # --- Convert Function ---
    def convert_currency_button_command():
        if from_currency.get() == to_currency.get():
            messagebox.showinfo("Info", "From and To currencies are the same.")
            return

        convert_from_value = check_value_is_numeric(value_entry.get())
        if convert_from_value is False:
            messagebox.showerror("Error", "Please enter a valid number greater than 0.")
            return

        converted_value = convert_currency(from_currency.get(), to_currency.get(), convert_from_value)
        to_currency_value.configure(
            text=f'{convert_from_value:.4f} {from_currency.get().split(" ")[0]}\n=\n{converted_value:.4f} {to_currency.get().split(" ")[0]}'
        )

    # --- Convert Button ---
    convert_button = CTkButton(app, text="Convert", font=("", default_font_size), fg_color="green", hover_color="#38B215", height=40, width=200, command=convert_currency_button_command)
    convert_button.grid(row=5, column=0, pady=(10, 20))

    app.mainloop()


if __name__ == "__main__":
    main()
