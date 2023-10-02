import tkinter as tk
from tkinter import ttk

# Create the main application window
app = tk.Tk()
app.title("Currency Converter with Alerts")

from_currency_label = tk.Label(app, text="From Currency:")
to_currencies_label = tk.Label(app, text="To Currencies:")
result_label = tk.Label(app, text="Exchange Rate:")
min_alert_threshold_label = tk.Label(app, text="Min Alert Threshold:")
max_alert_threshold_label = tk.Label(app, text="Max Alert Threshold:")

# Create a "Fetch Exchange Rates" button
fetch_rates_button = tk.Button(app, text="Fetch Exchange Rates", command=fetch_exchange_rates)

# Create a dropdown (combo box) for selecting the "From Currency"
from_currency_var = tk.StringVar()
from_currency_combo = ttk.Combobox(app, textvariable=from_currency_var)
from_currency_combo['values'] = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BZD", "CAD", "CDF", "CHF", "CLF", "CLP", "CNH", "CNY", "COP", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "ICP", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RUR", "RWF", "SAR", "SBD", "SCR", "SDG", "SDR", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VND", "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"]
from_currency_combo['state'] = 'readonly'
from_currency_combo.set("USD")  # Default selected currency

# Create a listbox for selecting multiple "To Currencies"
to_currency_listbox = tk.Listbox(app, selectmode=tk.MULTIPLE)
to_currencies = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL", "BSD", "BTN", "BWP", "BZD", "CAD", "CDF", "CHF", "CLF", "CLP", "CNH", "CNY", "COP", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "ICP", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRO", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RUR", "RWF", "SAR", "SBD", "SCR", "SDG", "SDR", "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VND", "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"]
for currency in to_currencies:
    to_currency_listbox.insert(tk.END, currency)
to_currency_listbox.select_set(0)  # Default selected currency

# Create entry fields for the alert thresholds
min_alert_threshold_var = tk.StringVar()
max_alert_threshold_var = tk.StringVar()
min_alert_threshold_entry = tk.Entry(app, textvariable=min_alert_threshold_var)
max_alert_threshold_entry = tk.Entry(app, textvariable=max_alert_threshold_var)
min_alert_threshold_var.set("0.0")  # Default minimum alert threshold
max_alert_threshold_var.set("2.0")  # Default maximum alert threshold

# Place widgets on the grid
from_currency_label.grid(row=0, column=0)
from_currency_combo.grid(row=0, column=1)
to_currencies_label.grid(row=1, column=0)
to_currency_listbox.grid(row=1, column=1)
min_alert_threshold_label.grid(row=2, column=0)
min_alert_threshold_entry.grid(row=2, column=1)
max_alert_threshold_label.grid(row=3, column=0)
max_alert_threshold_entry.grid(row=3, column=1)
fetch_rates_button.grid(row=4, column=0, columnspan=2)
result_label.grid(row=5, column=0, columnspan=2)

# Run the Tkinter main loop
app.mainloop()