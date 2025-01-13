import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Path to the directory you want to monitor
path = r"Insert your folder path here"

# Define file categories and their extensions
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv", ".ods"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".bat", ".sh"],
    "Scripts": [".py", ".js", ".html", ".css", ".php", ".java", ".c", ".cpp"],
    "Others": []
}

# Create folders for each category
for category in file_categories:
    folder_path = os.path.join(path, category)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


# Function to organize files
def organize_files():
    print("Organizing existing files...")
    file_names = os.listdir(path)
    for file in file_names:
        file_path = os.path.join(path, file)

        # Skip directories and only process files
        if not os.path.isfile(file_path):
            continue

        # Try matching the file to a category
        moved = False
        for category, extensions in file_categories.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                dest_folder = os.path.join(path, category)
                dest_path = os.path.join(dest_folder, file)

                # Move file to the appropriate folder
                try:
                    shutil.move(file_path, dest_path)
                    print(f"Moved file: {file} -> {category}")
                    moved = True
                except Exception as e:
                    print(f"Error moving file: {file} -> {e}")
                break

        # If no category matched, move the file to "Others"
        if not moved:
            others_folder = os.path.join(path, "Others")
            dest_path = os.path.join(others_folder, file)
            try:
                shutil.move(file_path, dest_path)
                print(f"Moved file: {file} -> Others")
            except Exception as e:
                print(f"Error moving file to Others: {file} -> {e}")


# Event handler class for live monitoring
class FileOrganizerHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Triggered when a new file is created
        print(f"New file detected: {event.src_path}")
        organize_files()

    def on_modified(self, event):
        # Triggered when a file is modified
        print(f"File modified: {event.src_path}")
        organize_files()


# Organize existing files before starting live monitoring
organize_files()

# Set up the observer for live monitoring
event_handler = FileOrganizerHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=False)

try:
    print("Monitoring folder for changes...")
    observer.start()
    while True:
        pass  # Keep the script running
except KeyboardInterrupt:
    observer.stop()
observer.join()
