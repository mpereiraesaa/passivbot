import os
import re

NEW_LIVE_CONFIGS_DIR = "latest_live_configs"
OPTIMIZED_CONFIG_RESULTS_PATH = "results_particle_swarm_optimization_recursive_grid_v1"

def get_latest_long_config_filename(directory):
    config_files = [f for f in os.listdir(directory) if re.match(r'\d+_best_config_long\.json', f)]
    if not config_files:
        return None
    latest_file = max(config_files, key=lambda x: int(x.split('_')[0]))
    return latest_file

def get_symbols_with_latest_configs(base_path):
    symbols_with_configs = []
    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)
        if os.path.isdir(folder_path):
            symbol = folder_name.split('_')[-1]
            latest_config_filename = get_latest_long_config_filename(folder_path)
            if latest_config_filename:  # Asegurarse de que se encontró un archivo
                symbols_with_configs.append((symbol, folder_name, latest_config_filename))
    return symbols_with_configs
