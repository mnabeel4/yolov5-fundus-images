
import os

# Directory containing your image files
directory = 'H:/workspace/Nabeel/yolov5/HR-test/images'

# Starting sequence number
sequence_number = 1


# Function to rename image files
def rename_image_files(directory):
    global sequence_number
    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.png') or filename.lower().endswith('.tif'):
            old_path = os.path.join(directory, filename)
            new_filename = f"Test-data_{sequence_number}.png"
            new_path = os.path.join(directory, new_filename)

            os.rename(old_path, new_path)
            print(f"Renamed {filename} to {new_filename}")

            sequence_number += 1


# Rename image files
rename_image_files(directory)

