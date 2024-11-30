import os
import shutil

# Define file type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".sh"],
    "Executables": [".exe", ".msi", ".bat"],
    "Others": []  # Files that don't match any category
}

# Function to organize files
def organize_files(directory):
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Create folders for file types
    for folder in FILE_TYPES.keys():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Move files to their respective folders
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        file_moved = False
        for folder, extensions in FILE_TYPES.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                try:
                    shutil.move(file_path, os.path.join(directory, folder, file))
                    file_moved = True
                    break
                except (shutil.Error, PermissionError) as e:
                    print(f"Error moving file {file}: {e}")

        # If no category matched, move to "Others"
        if not file_moved:
            try:
                shutil.move(file_path, os.path.join(directory, "Others", file))
            except (shutil.Error, PermissionError) as e:
                print(f"Error moving file {file}: {e}")

    print(f"Files in {directory} have been organized.")

if __name__ == "__main__":
    target_directory = input("Enter the path of the directory to organize: ").strip()
    organize_files(target_directory)