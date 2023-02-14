import tkinter as tk
from tkinter import ttk

# Conversion rates
usd_to_eur = 0.82
usd_to_gbp = 0.72
eur_to_usd = 1.22
eur_to_gbp = 0.87
gbp_to_usd = 1.39
gbp_to_eur = 1.15

class MoneyConverter:
    def __init__(self, master):
        self.master = master
        master.title("Money Converter")

        # Create labels and input fields
        self.amount_label = ttk.Label(master, text="Amount:")
        self.amount_label.grid(row=0, column=0, padx=5, pady=5)
        self.amount_entry = ttk.Entry(master, width=10)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)

        self.from_currency_label = ttk.Label(master, text="From:")
        self.from_currency_label.grid(row=1, column=0, padx=5, pady=5)
        self.from_currency = tk.StringVar()
        self.from_currency_combo = ttk.Combobox(master, textvariable=self.from_currency, values=["USD", "EUR", "GBP"])
        self.from_currency_combo.grid(row=1, column=1, padx=5, pady=5)

        self.to_currency_label = ttk.Label(master, text="To:")
        self.to_currency_label.grid(row=2, column=0, padx=5, pady=5)
        self.to_currency = tk.StringVar()
        self.to_currency_combo = ttk.Combobox(master, textvariable=self.to_currency, values=["EUR", "USD", "GBP"])
        self.to_currency_combo.grid(row=2, column=1, padx=5, pady=5)

        # Create the convert button and result label
        self.convert_button = ttk.Button(master, text="Convert", command=self.convert)
        self.convert_button.grid(row=3, column=0, padx=5, pady=5)

        self.result_label = ttk.Label(master, text="")
        self.result_label.grid(row=3, column=1, padx=5, pady=5)

    def convert(self):
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            self.result_label.configure(text="Please enter a valid amount")
            return

        from_currency = self.from_currency.get()
        to_currency = self.to_currency.get()

        if from_currency == "USD" and to_currency == "EUR":
            converted_amount = amount * usd_to_eur
        elif from_currency == "USD" and to_currency == "GBP":
            converted_amount = amount * usd_to_gbp
        elif from_currency == "EUR" and to_currency == "USD":
            converted_amount = amount * eur_to_usd
        elif from_currency == "EUR" and to_currency == "GBP":
            converted_amount = amount * eur_to_gbp
        elif from_currency == "GBP" and to_currency == "USD":
            converted_amount = amount * gbp_to_usd
        elif from_currency == "GBP" and to_currency == "EUR":
            converted_amount = amount * gbp_to_eur
        else:
            self.result_label.configure(text="Invalid conversion")

        self.result_label.configure(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")

root = tk.Tk()
money_converter = MoneyConverter(root)
root.mainloop()

root.mainloop()
