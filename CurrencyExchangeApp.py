import tkinter as tk
from tkinter import ttk


class CurrencyExchangeApp:
    def __init__(self, converter, currency_data,height, width):
        self.__converter = converter
        self.__curreny_data=currency_data

        self.__root = tk.Tk()
        self.__currency_1 = tk.StringVar(value="GEL")
        self.__currency_2 = tk.StringVar(value="USD")
        self.__entry_amount = tk.Entry(self.__root)
        self.__converted_amount = tk.StringVar()

        self.create_root(height, width)
        self.create_widgets()

    def create_root(self, height, width):
        self.__root.title("Currency Exchange")

        window_height = height
        window_width = width

        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()

        x_offset = (screen_width // 2) - (window_width // 2)
        y_offset = (screen_height // 3) - (window_height // 2)

        self.__root.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")

    def create_widgets(self):

        label_currency1 = tk.Label(self.__root, text="From:")
        label_currency1.grid(row=0, column=0, padx=10, pady=10)
        dropdown_currency_1 = tk.ttk.Combobox(self.__root, textvariable=self.__currency_1,
                                              values=list(self.__curreny_data.keys()))
        dropdown_currency_1.grid(row=0, column=1, padx=10, pady=10)

        label_currency2 = tk.Label(self.__root, text="To:")
        label_currency2.grid(row=1, column=0, padx=10, pady=10)
        dropdown_currency2 = tk.ttk.Combobox(self.__root, textvariable=self.__currency_2,
                                             values=list(self.__curreny_data.keys()))
        dropdown_currency2.grid(row=1, column=1, padx=10, pady=10)

        label_amount = tk.Label(self.__root, text="Amount:")
        label_amount.grid(row=2, column=0, padx=10, pady=10)
        self.__entry_amount.grid(row=2, column=1, padx=10, pady=10)

        label_converted = tk.Label(self.__root, text="Converted Amount:")
        label_converted.grid(row=3, column=0, padx=10, pady=10)
        label_result = tk.Label(self.__root, textvariable=self.__converted_amount)
        label_result.grid(row=3, column=1, padx=10, pady=10)

        button_convert = tk.Button(self.__root, text="Convert", command=self.convert_currency)
        button_convert.grid(row=4, column=0, padx=10, pady=20)

        button_reset = tk.Button(self.__root, text="Reset", command=self.reset_fields)
        button_reset.grid(row=4, column=1, padx=10, pady=20)

    def convert_currency(self):
        try:
            amount = float(self.__entry_amount.get())
            result = self.__converter.convert(self.__currency_1.get(), self.__currency_2.get(), amount)
            self.__converted_amount.set(f"{result:.2f}")
        except BaseException:
            self.__converted_amount.set("Invalid input")

    def reset_fields(self):
        self.__entry_amount.delete(0, tk.END)
        self.__converted_amount.set("")
        self.__currency_1.set("GEL")
        self.__currency_2.set("USD")

    def run(self):
        self.__root.mainloop()
