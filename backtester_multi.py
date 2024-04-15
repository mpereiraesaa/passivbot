import subprocess

start_dates = ["2022-03-21"]
end_date = "2024-03-30"
user = "binance_01"
exchange = "binance"

total_wallet_exposure_long_values = ["2.0"]
total_wallet_exposure_short_values = ["1.0"]

balance_value = "10000"

coins = ["FETUSDT", "AGIXUSDT", "XLMUSDT", # qty precision 1.0 list
    "RNDRUSDT", "APTUSDT", "ARBUSDT", "LDOUSDT", # low qty pct precision 0.1 list
    "INJUSDT", "1000SHIBUSDT", "DOGEUSDT", "1000PEPEUSDT", # top 100 small coin
]

def run_backtest_for_balance(command, start_date, twe_short, twe_long):
    full_command = command + [
        "-s", ",".join(coins),
        "-tl", twe_long,
        "-ts", twe_short,
        "-sb", balance_value,
        "--start_date", start_date,
        "--end_date", end_date
    ]
    subprocess.run(full_command)

# Command for the backtest
base_command = [
    "python3",
    "backtest_multi.py",
]

# Run the backtest for each starting date, symbol, short_leverage, and long_leverage value
for start_date in start_dates:
    for short_leverage_value in total_wallet_exposure_short_values:
        for long_leverage_value in total_wallet_exposure_long_values:
            run_backtest_for_balance(base_command, start_date, short_leverage_value, long_leverage_value)
