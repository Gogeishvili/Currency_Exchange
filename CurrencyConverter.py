
class CurrencyConverter:
    def __init__(self,api):
        self.__currency_rates = api.load_currency_data()
        print(self.__currency_rates)

    @property
    def currency_rates(self):
        return self.__currency_rates

    def convert(self, from_currency, to_currency, amount):
        if from_currency not in self.__currency_rates or to_currency not in self.__currency_rates:
            return None
        rate = self.__currency_rates[to_currency] / self.__currency_rates[from_currency]
        return amount * rate

    def load_currency_data(self):
        #დრო არ მეყო თორე აქ ეიპიაის გაპარსვას ვაპირებდი 😂
        return {
            "GEL": 1.00,
            "USD": 0.32,
            "EUR": 0.27
        }
