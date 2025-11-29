import os
import shutil

def split_pdfs_into_folders(src_folder, batch_size=20):
    # Get all PDF files in the folder
    files = [f for f in os.listdir(src_folder) if f.lower().endswith(".pdf")]
    files.sort()  # sort for consistency

    # Make batches
    for i in range(0, len(files), batch_size):
        batch = files[i:i+batch_size]
        folder_num = (i // batch_size) + 1
        dest_folder = os.path.join(src_folder, str(folder_num))

        os.makedirs(dest_folder, exist_ok=True)

        for f in batch:
            shutil.move(os.path.join(src_folder, f),
                        os.path.join(dest_folder, f))

    print("Done! Split into folders.")

# Usage
src_folder = r"./reports/REPORTS/"  # change this to your folder path
split_pdfs_into_folders(src_folder, batch_size=20)
