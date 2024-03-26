

import time


class ExchangeRateFetcher:
    def simulate_api_call(self, base_currency, target_currency):
        # Simulating API call with specific exchange rates
        exchange_rates = {
            'USD': 0.75,
            'EUR': 0.68,
            'GBP': 0.59,
            'SGD': 1.02,
            'CNY': 5.15,
            'JPY': 82.50,
        }

        time.sleep(0.5)  # delay
        return exchange_rates.get(target_currency, 1.0)  # Default to 1.0 if currency not found
