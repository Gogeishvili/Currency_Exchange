from CurrencyConverter import CurrencyConverter
from CurrencyExchangeApp import CurrencyExchangeApp

def main():
    converter = CurrencyConverter()
    app = CurrencyExchangeApp(converter,400,400)
    app.run()

if __name__ == "__main__":
    main()

