import logging
from django.core.management.base import BaseCommand
from binance.client import Client
from binance.exceptions import BinanceAPIException
from WithdrawalApp.Api.config import API_KEY, API_SECRET

# Set up logging
logging.basicConfig(
    filename='withdrawals.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Command(BaseCommand):
    help = "Withdraw assets from Binance with pre-defined details"

    def handle(self, *args, **kwargs):
        # Withdrawal details (Hard-coded)
        asset = 'BNB'  # The asset you want to withdraw
        address = 'your_destination_wallet_address'  # The recipient's wallet address
        amount = 0.5  # Amount to withdraw
        network = 'BSC'  # Binance Smart Chain (or any supported network)

        # Initialize Binance client
        client = Client(API_KEY, API_SECRET)

        # Sync the client time with Binance server time
        client.get_server_time()

        # Log the withdrawal attempt
        logging.info(f"Attempting to withdraw {amount} {asset} to {address} on network {network}")

        # Confirmation prompt
        confirm = input(f"Are you sure you want to withdraw {amount} {asset} to {address} on {network}? (yes/no): ").strip().lower()

        if confirm == 'yes':
            try:
                # Make the withdrawal request
                response = client.withdraw(
                    asset=asset,
                    address=address,
                    amount=amount,
                    network=network
                )
                self.stdout.write(self.style.SUCCESS(f"Withdrawal successful: {response}"))
                logging.info(f"Withdrawal successful: {response}")
            except BinanceAPIException as e:
                self.stdout.write(self.style.ERROR(f"Error during withdrawal: {e.message}"))
                logging.error(f"Error during withdrawal: {e.message}")
        else:
            self.stdout.write(self.style.WARNING("Withdrawal canceled by user."))
            logging.info("Withdrawal canceled by user.")
