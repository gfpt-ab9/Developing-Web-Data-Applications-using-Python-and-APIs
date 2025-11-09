
import requests

# Your Forex API key (replace with your actual one from https://www.forexrateapi.com)
api_key = "f81f4717327b01201daa77f00b7daf5c"

# Ask user for details
base = input("Enter base currency: ").upper()
target = input("Enter target currency: ").upper()
amount = float(input("Enter amount to convert: "))

# API endpoint (Forex API)
url = f"https://api.forexrateapi.com/v1/latest?api_key={api_key}&base={base}"

# Send request to API
response = requests.get(url)
data = response.json()

# Debugging tip (optional): print(data)

# Check if API returned rates
if "rates" in data and target in data["rates"]:
    rate = data["rates"][target]
    converted = amount * rate
    print(f"\n{amount} {base} = {converted:.2f} {target}")
else:
    print("\nError: Could not fetch exchange rate. Please check currency codes or API key.")
