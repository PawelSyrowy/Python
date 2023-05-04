import requests

# API URL to fetch latest exchange rates
api_url = "https://api.exchangerate-api.com/v4/latest/"


def convert_currency(amount, from_currency, to_currency):
    # Fetch the latest exchange rates from the API
    response = requests.get(api_url + from_currency)
    data = response.json()

    # Extract the exchange rate for the target currency
    exchange_rate = data["rates"][to_currency]

    # Calculate the converted amount
    converted_amount = amount * exchange_rate

    # Return the converted amount rounded to 2 decimal places
    return round(converted_amount, 2)


# Example usage
amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the source currency code (e.g. USD): ")
to_currency = input("Enter the target currency code (e.g. EUR): ")

converted_amount = convert_currency(amount, from_currency, to_currency)

print(f"{amount} {from_currency} is equivalent to {converted_amount} {to_currency}")
