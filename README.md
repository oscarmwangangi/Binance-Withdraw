# Binance Withdrawal and Balance Check 🚀💰

This project includes two Django management commands:

1. **Withdraw Assets**: A command that withdraws a specified amount of cryptocurrency from your Binance account to a specified address. 💸
2. **Check Account Balance**: A command that retrieves and prints the available balance for a specified asset (e.g., BNB, BTC) in your Binance account. 📊

## Prerequisites 🛠️

Before running the commands, ensure you have the following set up:

- A Binance account and API key with appropriate permissions for withdrawals and balance checks.
- Install the required libraries:
  - `python-binance`: Binance API client for Python
  - `Django`: Web framework for managing the project

### Clone
```bash
git clone https://github.com/oscarmwangangi/Binance-Withdraw.git
```
### install all dependancy
```bash
pip install -r requirements.txt
```

## Usage
### 1. Withdraw Assets 💸
To withdraw assets, run the following command in your terminal:
```bash
python manage.py withdraw
```
### 2. Check Account Balance 💰
To check the balance of a specific asset in your Binance account, run the following command in your terminal:
``` bash
python manage.py check_balance
```

## Troubleshooting 🛠️

### Common Errors ❌

#### "Timestamp for this request was 1000ms ahead of the server's time":

This error occurs due to a time synchronization issue between your server and the Binance API.

**Solution**: Ensure that your server time is synchronized with the Binance server's time. You can call `client.get_server_time()` to synchronize it programmatically.

**Solution 2**: Go to setting in your computer click time scroll to sync and  click

#### "You are not authorized to execute this request":

This error means that your API key does not have the necessary permissions to perform the action (withdrawal).

**Solution**: Ensure that your API key has withdrawal permissions enabled in the Binance API Management page and check if IP whitelisting is required.

### Log Files 📄

- **withdrawals.log**: Logs all withdrawal attempts (both successful and unsuccessful).
- **balances.log**: Logs the results of balance check attempts.

