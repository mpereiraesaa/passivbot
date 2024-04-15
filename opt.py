# python3 opt.py #(will start signle optimize process)

import subprocess

def run_optimize(symbol, backtest_config, optimize_config, start_date, end_date):
    command = [
        "python3",
        "optimize.py",
        "-s", symbol,
        "-b", backtest_config,
        "-oc", optimize_config,
        "--start_date", start_date,
        "--end_date", end_date
    ]
    subprocess.run(command, check=True)

def main():
    coins = ["FETUSDT", "AGIXUSDT", "XLMUSDT", "MATICUSDT",
        "RNDRUSDT", "ATOMUSDT", "ARBUSDT", "LDOUSDT",
        "INJUSDT", "1000SHIBUSDT", "DOGEUSDT", "RLCUSDT",
        "OPUSDT", "WLDUSDT", "BLURUSDT", "AVAXUSDT",
        "XRPUSDT", "ORDIUSDT", "TONUSDT", "TIAUSDT",
        "BTCUSDT", "ETHUSDT", "SOLUSDT", "LTCUSDT"
    ]

    backtest_config = "configs/backtest/default.hjson"
    optimize_config = "configs/optimize/default.hjson"
    start_date = "2021-03-01"
    end_date = "2024-03-25"

    for symbol in coins:
        run_optimize(symbol, backtest_config, optimize_config, start_date, end_date)

if __name__ == "__main__":
    main()
