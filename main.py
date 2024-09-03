from CurrencyConverter import CurrencyConverter
from CurrencyExchangeApp import CurrencyExchangeApp
from CurrencyAPIParse import CurrencyAPIParse

def main():

    curenccyAPiParse = CurrencyAPIParse()
    converter = CurrencyConverter(curenccyAPiParse)
    app = CurrencyExchangeApp(converter,400,400)
    app.run()



if __name__ == "__main__":
    main()

