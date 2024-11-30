# File Organizer Script

Welcome to the **File Organizer** script! This Python script automatically organizes files in a specified directory based on their types. It categorizes files into folders such as Images, Documents, Videos, Music, Archives, Scripts, Executables, and Others. It ensures that your files are neatly sorted, making it easier to find what you need.

## Table of Contents
1. [Introduction](#introduction)
2. [How it Works](#how-it-works)
3. [File Categories](#file-categories)
4. [Setup Instructions](#setup-instructions)
5. [Usage](#usage)
6. [Error Handling](#error-handling)
7. [Conclusion](#conclusion)

## Introduction

This script helps you automatically organize your files in a directory into different categories based on their file types. It works by scanning the files in the specified directory and then sorting them into predefined categories.

## How it Works

1. The script first checks whether the directory exists.
2. It then creates subfolders for each file category (e.g., Images, Documents, etc.).
3. It scans all the files in the target directory, matching their extensions with the predefined categories.
4. If a file matches a category, it is moved into the corresponding folder.
5. Files that do not match any predefined category are moved into the "Others" folder.

## File Categories

The script organizes the files into the following categories:

- **Images**: .jpg, .jpeg, .png, .gif, .bmp, .svg, .webp
- **Documents**: .pdf, .doc, .docx, .txt, .ppt, .pptx, .xls, .xlsx
- **Videos**: .mp4, .mkv, .avi, .mov, .wmv
- **Music**: .mp3, .wav, .aac, .flac
- **Archives**: .zip, .rar, .7z, .tar, .gz
- **Scripts**: .py, .js, .html, .css, .sh
- **Executables**: .exe, .msi, .bat
- **Others**: Any file that doesn't match the above categories

## Setup Instructions

To use this script, you need Python installed on your system. You don't need any additional libraries, as it only uses the built-in `os` and `shutil` libraries.

### Prerequisites

- Python 3.x installed.
- Basic understanding of using Python scripts.

### How to Set Up:

1. **Install Python** (if not already installed):
    - Download and install Python from [python.org](https://www.python.org/downloads/).
    - During installation, ensure that you check the option to add Python to the system PATH.

2. **Download the Script**:
    - Copy the code into a file named `file_manager.py`.

## Usage

To use the file organizer script, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the folder where the `file_manager.py` script is located.
3. Run the script using the following command:

   ```bash
   python file_organizer.py
   ```

4. The script will prompt you to enter the path of the directory you wish to organize. Enter the path and press Enter.

5. The script will process the files in the specified directory and organize them into folders according to their type.

### Example

```bash
Enter the path of the directory to organize: C:\Users\YourName\Downloads
```

The files in the specified directory will be moved into appropriate folders such as `Images`, `Documents`, `Videos`, and so on.

## Error Handling

- If the directory does not exist, the script will notify you and terminate the operation.
- If a file cannot be moved due to permission issues or other errors, the script will print an error message.

### Common Errors:
- **File Permission Issues**: If the script is unable to move a file due to insufficient permissions, ensure that you have the required permissions for the files and the target directory.
- **Missing Directory**: If the target directory does not exist, the script will display an error message and stop.

## Conclusion

This **File Organizer** script helps keep your files in order by categorizing them into folders. It saves you time and effort when organizing files manually, making it easier to maintain a clean and efficient file structure.

Feel free to customize the categories and extensions based on your needs. Happy organizing!
