import os
import shutil

def is_folder_not_empty(folder_path):
    return bool(os.listdir(folder_path))

def copy_files(source_folder, destination_folder):
    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)
        if os.path.isfile(source_file):
            shutil.copy(source_file, destination_file)

def delete_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

# Example usage
# source_folder = 'path/to/source_folder'
# destination_folder = 'path/to/destination_folder'

# if is_folder_not_empty(source_folder):
#     copy_files(source_folder, destination_folder)
#     delete_files(source_folder)
#     print("Files copied and deleted successfully.")
# else:
#     print("The source folder is empty.")
