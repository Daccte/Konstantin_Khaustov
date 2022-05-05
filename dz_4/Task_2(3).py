import requests
from datetime import datetime

def currency_rates(currency_code):
    currency_code = currency_code.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    print(response.text)
    if response.ok:
        new_code = response.text.split(currency_code)
        value = new_code[1].split("</Value>")[0].split("<Value>")[1]
        value = float(value.replace(',', '.'))
        date = response.headers['Date']
        date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT").date()

        return date, currency_code, value
    else:
        return None


print(currency_rates('UsD'))
print(currency_rates('Eur'))