from CurrencyConverter import CurrencyConverter
from CurrencyExchangeApp import CurrencyExchangeApp
from CurrencyAPIParse import CurrencyAPIParse


def main():
    currencyAPiParse = CurrencyAPIParse()
    currency_data = currencyAPiParse.load_currency_data()
    print(currency_data)
    converter = CurrencyConverter(currency_data)
    app = CurrencyExchangeApp(converter, currency_data, 400, 400)
    app.run()


if __name__ == "__main__":
    main()
