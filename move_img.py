import os
from tqdm import tqdm
import cv2
import shutil
sets=['train','val','test']



for image_set in sets:
    if not os.path.exists('./HR-yoloset1/images/%s'%(image_set)):
        os.makedirs('./HR-yoloset1/images/%s'%(image_set))

    path = './HR-yoloset1/labels/%s'%(image_set)
    if not os.path.exists(path) :
        continue

    image_ids = os.listdir(path)
    for image_id in tqdm(image_ids):
        # image_id=image_id.replace('\n','')
        #imgRoot = 'G:/2021-07-09DataSet 4 Hand-held Probe SSD/2021-07-09DataSet 4 Hand-held Probe SSD/Hand-held-Probe/Lesion Image'
        imgRoot = 'H:/workspace/Nabeel/yolov5/HR-images'
        img_path = os.path.join(imgRoot,image_id).replace('.txt','.jpg')
        if os.path.exists(img_path)  == False:
            continue
        shutil.copy(img_path,'./HR-yoloset1/images/%s'%(image_set))

        print(f"Checking for image: {img_path}")
        if os.path.exists(img_path):
            shutil.copy(img_path, f'./HR-yoloset1/images/{image_set}')
            print(f"Copied {img_path} to ./HR-yoloset1/images/{image_set}")
        else:
            print(f"Image {img_path} does not exist.")

