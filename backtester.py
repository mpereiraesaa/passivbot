import os
import subprocess
from new_utils import OPTIMIZED_CONFIG_RESULTS_PATH, get_latest_long_config_filename

start_dates = ["2024-04-03"]
end_date = "2024-04-09"
user = "binance_01"

long_leverage_values = ["0.2"] # ["0.1", "0.15", "0.20", "1.0"]
short_leverage_values = ["0.1"]

balance_values = ["15000"]  # ["250", "500", "1000"]

symbols_with_folders = []

for folder_name in os.listdir(OPTIMIZED_CONFIG_RESULTS_PATH):
    if os.path.isdir(os.path.join(OPTIMIZED_CONFIG_RESULTS_PATH, folder_name)):
        symbol = folder_name.split('_')[-1]
        symbols_with_folders.append((symbol, folder_name))

extended_symbols_with_folders = []
for symbol, folder_name in symbols_with_folders:
    directory_path = os.path.join(OPTIMIZED_CONFIG_RESULTS_PATH, folder_name)
    latest_config_filename = get_latest_long_config_filename(directory_path)
    extended_symbols_with_folders.append((symbol, folder_name, latest_config_filename))

print(extended_symbols_with_folders)

def run_backtest_for_balance(command, start_date, short_leverage, long_leverage):
    for symbol, folder, config_name in extended_symbols_with_folders:
        for balance in balance_values:
            full_command = command + [
                "-u", user,
                "-s", symbol,
                # "-sw", short_leverage,
                "-lw", long_leverage,
                "-m", "futures",
                "-sb", balance,
                f"{OPTIMIZED_CONFIG_RESULTS_PATH}/{folder}/{config_name}",
                "--start_date", start_date,
                "--end_date", end_date
            ]
            subprocess.run(full_command)

# Command for the backtest
base_command = [
    "python3",
    "backtest.py",
]

# Run the backtest for each starting date, symbol, short_leverage, and long_leverage value
for start_date in start_dates:
    for short_leverage_value in short_leverage_values:
        for long_leverage_value in long_leverage_values:
            run_backtest_for_balance(base_command, start_date, short_leverage_value, long_leverage_value)
