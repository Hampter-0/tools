import os
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Programs": [".exe", ".bat"]
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        return "Folder not found :("

    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for file in files:
        file_path = os.path.join(folder_path, file)
        moved = False
        for folder, extensions in FILE_TYPES.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                dest_folder = os.path.join(folder_path, folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, file))
                moved = True
                break
        if not moved:
            others_folder = os.path.join(folder_path, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, file))

    return "Files organized :)"
