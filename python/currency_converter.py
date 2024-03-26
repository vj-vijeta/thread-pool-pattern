


from exchange_rate_fetcher import ExchangeRateFetcher

def convert_currency(amount_inr, exchange_rate, currency):
    converted_amount = amount_inr * exchange_rate
    print(f"{amount_inr} INR = {converted_amount:.2f} {currency}")

def fetch_exchange_rate_and_convert(exchange_rate_fetcher, base_currency, amount_inr, currency):
    print(f"Thread for {currency} started.")
    exchange_rate = exchange_rate_fetcher.simulate_api_call(base_currency, currency)
    convert_currency(amount_inr, exchange_rate, currency)
    print(f"Thread for {currency} finished.")
