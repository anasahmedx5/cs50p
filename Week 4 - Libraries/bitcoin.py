import requests
import sys

try:
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    data = response.json()
    price = float(data["data"]["priceUsd"])

except requests.RequestException:
    sys.exit


try:
    number = float(sys.argv[1])

except IndexError:
    sys.exit("Missing command-line argument")

except ValueError:
    sys.exit("Command-line argument is not a number")

amount = number * price
print(f"${amount:,.4f}")
