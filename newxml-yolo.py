
import os

# Path to your dataset
dataset_root = 'H:/data/new-fundus-dataset/new-fundus-dataset/fundus-data-seg'

# Directory containing images and labels for the 'train' set
train_image_dir = os.path.join(dataset_root, 'H:/workspace/Nabeel/yolov5/yolo_set10/images/', 'train')
train_label_dir = os.path.join(dataset_root, 'H:/workspace/Nabeel/yolov5/yolo_set10/labels/', 'train')

# Path to save train.txt file
train_txt_path = os.path.join(dataset_root, 'H:/workspace/Nabeel/yolov5/yolo_set10/val.txt')

# Open train.txt in write mode
with open(train_txt_path, 'w') as train_txt:
    # Iterate through images in the train set
    for image_name in os.listdir(train_image_dir):
        # Check if the file is an image file
        if image_name.endswith('.jpg'):
            image_path = os.path.join(train_image_dir, image_name)
            label_path = os.path.join(train_label_dir, image_name.replace('.jpg', '.txt'))

            # Check if the corresponding label file exists
            if os.path.exists(label_path):
                # Write the image path and label path to train.txt
                train_txt.write(f"{image_path} {label_path}\n")