from os import system
import os
from time import sleep
from new_utils import OPTIMIZED_CONFIG_RESULTS_PATH, get_latest_long_config_filename

user = "binance_01"
symbols_with_folders = []

session_name = f"{user}_session"
system(f"tmux has-session -t {session_name} 2>/dev/null || tmux new-session -d -s {session_name}")

for folder_name in os.listdir(OPTIMIZED_CONFIG_RESULTS_PATH):
    if os.path.isdir(os.path.join(OPTIMIZED_CONFIG_RESULTS_PATH, folder_name)):
        symbol = folder_name.split('_')[-1]
        symbols_with_folders.append((symbol, folder_name))

extended_symbols_with_folders = []
for symbol, folder_name in symbols_with_folders:
    directory_path = os.path.join(OPTIMIZED_CONFIG_RESULTS_PATH, folder_name)
    latest_config_filename = get_latest_long_config_filename(directory_path)
    extended_symbols_with_folders.append((symbol, folder_name, latest_config_filename))

for symbol, folder, config_name in extended_symbols_with_folders:
    # Construct the command and run it using tmux command
    command = f"python3 passivbot.py {user} {symbol} --test_mode {OPTIMIZED_CONFIG_RESULTS_PATH}/{folder}/{config_name}"
    window_name = symbol
    tmux_command = f"tmux new-window -t {session_name} -n {window_name} '{command}'"    
    system(tmux_command)
    print(f"{tmux_command} with config {folder}/{config_name} started...")
    sleep(1)

print('All Bots are running :)')
