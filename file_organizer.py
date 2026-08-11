import os
import shutil

# Ask the user for the folder path
folder_path = input("Enter the folder path: ")

# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".doc", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav"],
    "Excel": [".xlsx", ".xls", ".csv"],
    "Others": []
}

# Check if the folder exists
if not os.path.exists(folder_path):
    print("Folder does not exist!")
    exit()

# Go through all files in the folder
for file_name in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file_name)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get the file extension
    extension = os.path.splitext(file_name)[1].lower()

    category_found = False

    # Find the correct category
    for category, extensions in file_types.items():

        if extension in extensions:

            destination_folder = os.path.join(
                folder_path, category
            )

            # Create category folder
            os.makedirs(destination_folder, exist_ok=True)

            # Move the file
            shutil.move(
                file_path,
                os.path.join(destination_folder, file_name)
            )

            print(f"Moved: {file_name} → {category}")

            category_found = True
            break

    # Move unknown file types to Others
    if not category_found:

        destination_folder = os.path.join(
            folder_path, "Others"
        )

        os.makedirs(destination_folder, exist_ok=True)

        shutil.move(
            file_path,
            os.path.join(destination_folder, file_name)
        )

        print(f"Moved: {file_name} → Others")

print("\n✅ Files organized successfully!")