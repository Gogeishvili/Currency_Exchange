import requests

class CurrencyAPIParse:
    def __init__(self):
        self.__api_url = 'https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/ka/json/?currencies=RUB&currencies=USD&currencies=EUR&date=2024-09-03'

    def load_currency_data(self):
        response = requests.get(self.__api_url)

        if response.status_code == 200:
            data = response.json()

            if isinstance(data, list):
                data = data[0]
                if 'currencies' in data:
                    currencies = data['currencies']

                    currency_dict = {}
                    for currency in currencies:
                        code = currency['code']
                        rate = currency['rate']

                        if code in ['USD', 'EUR']:
                            currency_dict[code] = rate

                    if 'GEL' not in currency_dict:
                        currency_dict['GEL'] = 1.00

            return currency_dict
        else:
            raise Exception("Failed to fetch data from API")

