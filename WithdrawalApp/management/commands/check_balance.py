import logging
from django.core.management.base import BaseCommand
from binance.client import Client
from binance.exceptions import BinanceAPIException
from WithdrawalApp.Api.config import API_KEY, API_SECRET  # Import credentials from config.py
from colorama import Fore, Style  # To add color formatting to the output

# Set up logging
logging.basicConfig(
    filename='balances.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Command(BaseCommand):
    help = "Check the balance of assets on Binance"

    def handle(self, *args, **kwargs):
        # Initialize Binance client
        client = Client(API_KEY, API_SECRET)

        # Fetch account balance and print results
        self.get_account_balance(client)

    def get_account_balance(self, client):
        """
        Fetch and print the balance of assets from the Binance account.
        """
        try:
            balance = client.get_account()
            balances = balance['balances']

            # Print and log account balances
            self.stdout.write(Fore.CYAN + Style.BRIGHT + "Account Balances:")
            logging.info("Account Balances:")

            for asset in balances:
                if float(asset['free']) > 0:  # Only show assets that have a non-zero balance
                    free_balance = float(asset['free'])
                    locked_balance = float(asset['locked'])
                    total_balance = free_balance + locked_balance
                    
                    # Display balance in terminal and log to file
                    self.stdout.write(f"{Fore.YELLOW}{asset['asset']}: {Fore.GREEN}{free_balance} free, {Fore.RED}{locked_balance} locked")
                    logging.info(f"{asset['asset']}: Free = {free_balance}, Locked = {locked_balance}, Total = {total_balance}")
        
        except BinanceAPIException as e:
            # Handle errors
            self.stdout.write(self.style.ERROR(f"Error fetching balance: {e.message}"))
            logging.error(f"Error fetching balance: {e.message}")
