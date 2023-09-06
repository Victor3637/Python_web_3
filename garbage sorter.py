import os
import shutil
from concurrent.futures import ThreadPoolExecutor

# Function to organize a file based on its extension
def organize_file(file_path, destination_folder):
    # Get the file extension
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()  # Convert the extension to lowercase

    # Create a folder for the extension if it doesn't exist
    extension_folder = os.path.join(destination_folder, file_extension[1:])
    os.makedirs(extension_folder, exist_ok=True)

    # Move the file to the corresponding folder
    shutil.move(file_path, os.path.join(extension_folder, os.path.basename(file_path)))

# Function to traverse a directory and organize files
def process_directory(root_folder, destination_folder):
    for root, _, files in os.walk(root_folder):
        for file in files:
            file_path = os.path.join(root, file)
            # Organize the file into the appropriate extension folder
            organize_file(file_path, destination_folder)

if __name__ == "__main__":
    source_folder = "Clutter"
    destination_folder = "Sorted_Files"

    # Create a folder for sorting
    os.makedirs(destination_folder, exist_ok=True)

    # Use ThreadPoolExecutor for parallel traversal and sorting
    with ThreadPoolExecutor(max_workers=4) as executor:
        for root, _, _ in os.walk(source_folder):
            # Traverse each folder in a separate thread
            executor.submit(process_directory, root, destination_folder)

    print("Sorting completed.")
