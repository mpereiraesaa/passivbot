import os
import shutil
from new_utils import get_symbols_with_latest_configs, OPTIMIZED_CONFIG_RESULTS_PATH, NEW_LIVE_CONFIGS_DIR

def copy_configs_to_live(symbols_with_configs, src_base_path, dest_base_path):
    for symbol, folder, config_name in symbols_with_configs:
        src_path = os.path.join(src_base_path, folder, config_name)
        dest_path = os.path.join(dest_base_path, f"{symbol}.json")
        try:
            shutil.copy(src_path, dest_path)
            print(f"Copied {src_path} to {dest_path}")
        except Exception as e:
            print(f"Error copying {src_path} to {dest_path}: {e}")

# Obtener la lista de símbolos con sus configuraciones más recientes
symbols_with_latest_configs = get_symbols_with_latest_configs(OPTIMIZED_CONFIG_RESULTS_PATH)

# Copiar las configuraciones más recientes al directorio de configuraciones en vivo
copy_configs_to_live(symbols_with_latest_configs, OPTIMIZED_CONFIG_RESULTS_PATH, NEW_LIVE_CONFIGS_DIR)
