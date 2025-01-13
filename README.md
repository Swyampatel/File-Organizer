# File Organizer

## Overview
The **File Organizer** is a Python-based automation tool designed to efficiently manage and declutter directories by categorizing files into designated folders based on their types. It not only organizes existing files at startup but also monitors the directory in real-time, ensuring any newly added or modified files are sorted immediately. This project demonstrates practical programming skills and highlights the power of automation.

---

## Features
- Automatically organizes files into categories like Images, Videos, Documents, Audio, Archives, Scripts, and Others.
- Supports a wide range of file types (e.g., `.jpg`, `.png`, `.mp4`, `.pdf`, `.zip`, `.py`).
- Real-time directory monitoring using the `watchdog` library.
- Fully customizable categories and file extensions.
- Prevents overwriting files by checking for existing filenames in target folders.

---

## What I Learned
1. **Python Automation**: Leveraged Python's libraries to build a practical file management tool.
2. **File Handling**: Gained experience in working with file paths, extensions, and directory management.
3. **Real-Time Monitoring**: Used the `watchdog` library to detect file system changes dynamically.
4. **Error Handling**: Implemented robust error handling to ensure smooth execution.
5. **Project Structuring**: Designed a clean, reusable, and scalable codebase suitable for real-world applications.

---

## Dependencies
Before running the program, ensure you have the following installed:

- Python 3.6 or higher
- Required Python libraries:
  ```bash
  pip install watchdog
  ```

---

## How to Use
1. Clone or download the repository.
2. Open the Python file and update the `path` variable:
   ```python
   path = r"Insert your folder path here"
   ```
3. Run the script:
   ```bash
   python FileOrganizer.py
   ```
4. Watch as the program organizes your files into appropriate folders!

---

## File Categories
- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg`
- **Videos**: `.mp4`, `.mkv`, `.flv`, `.avi`, `.mov`, `.wmv`
- **Audio**: `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.m4a`
- **Documents**: `.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.txt`, `.csv`, `.ods`
- **Archives**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`
- **Scripts**: `.py`, `.js`, `.html`, `.css`, `.php`, `.java`, `.c`, `.cpp`
- **Others**: Files that don't fit into the above categories

---

## Customization
You can modify the file categories and extensions to suit your needs. Edit the `file_categories` dictionary in the script:

```python
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    # Add or modify categories here
}
```

---

## Why This Project Stands Out
- **Practical Application**: Demonstrates a real-world use case for Python automation.
- **Technical Skills**: Combines file handling, event monitoring, and error management.


---

## License
Feel free to use or modify this code for personal or professional projects. Attribution is appreciated!
