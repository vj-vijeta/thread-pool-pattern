
import threading

from exchange_rate_fetcher import ExchangeRateFetcher
from currency_converter import fetch_exchange_rate_and_convert

def main():
    base_currency = 'INR'
    target_currencies = ['USD', 'EUR', 'GBP', 'SGD', 'CNY', 'JPY']
    amount_inr = float(input("Enter the amount in INR: "))

    exchange_rate_fetcher = ExchangeRateFetcher()
    threads = []

    for currency in target_currencies:
        thread = threading.Thread(
            target=fetch_exchange_rate_and_convert,
            args=(exchange_rate_fetcher, base_currency, amount_inr, currency,)
        )
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
