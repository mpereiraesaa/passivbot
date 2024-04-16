import os
import shutil
import sys

best_configs_extracted_path = "configs/extracted/"

def copy_json_files_from_harmony_folders(dest_dir):
    """
    Copies all JSON files that end with 'USDT.json' from each subdirectory starting with 'harmony_search_recursive_grid_'
    in the source root directory to the specified destination directory.
    
    Parameters:
        source_root (str): Root directory containing subdirectories prefixed with 'harmony_search_recursive_grid_'.
        dest_dir (str): Destination directory where files should be copied.
    """
    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Created directory: {dest_dir}")

    # Loop through each directory in the source root
    for folder in os.listdir(best_configs_extracted_path):
        full_folder_path = os.path.join(best_configs_extracted_path, folder)
        if os.path.isdir(full_folder_path):
            # Loop through each file within the folder
            for filename in os.listdir(full_folder_path):
                if filename.endswith("USDT.json"):  # Check if the file matches the pattern
                    src_path = os.path.join(full_folder_path, filename)
                    dest_path = os.path.join(dest_dir, filename)
                    shutil.copy(src_path, dest_path)  # Copy file
                    print(f"Copied {filename} from {full_folder_path} to {dest_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <destination_directory>")
        sys.exit(1)

    destination_directory = sys.argv[1]

    copy_json_files_from_harmony_folders(destination_directory)
