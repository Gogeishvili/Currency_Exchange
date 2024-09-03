
class CurrencyConverter:
    def __init__(self,api):
        self.__currency_rates = api
        print(self.__currency_rates)

    # @property
    # def currency_rates(self):
    #     return self.__currency_rates

    def convert(self, from_currency, to_currency, amount):
        normalized_rates = self.normalize_rates(self.__currency_rates)
        if from_currency not in self.__currency_rates or to_currency not in self.__currency_rates:
            return None
        rate = self.__currency_rates[to_currency] / self.__currency_rates[from_currency]
        return amount * rate

    def normalize_rates(self, rates):
        base_rate = rates.get('GEL', 1.00)
        normalized_rates = {code: base_rate / rate for code, rate in rates.items()}
        return normalized_rates

    def load_currency_data(self):
        #დრო არ მეყო თორე აქ ეიპიაის გაპარსვას ვაპირებდი 😂
        return {
            "GEL": 1.00,
            "USD": 0.32,
            "EUR": 0.27
        }
