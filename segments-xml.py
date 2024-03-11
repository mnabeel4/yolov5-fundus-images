import os
import cv2
import numpy as np
import xml.etree.ElementTree as ET

def create_voc_xml(xml_filename, image_filename, width, height, objects):
    root = ET.Element("annotation")

    folder = ET.SubElement(root, "folder")
    folder.text = "images"

    filename_elem = ET.SubElement(root, "filename")
    filename_elem.text = image_filename

    size = ET.SubElement(root, "size")
    width_elem = ET.SubElement(size, "width")
    width_elem.text = str(width)
    height_elem = ET.SubElement(size, "height")
    height_elem.text = str(height)

    for obj in objects:
        obj_elem = ET.SubElement(root, "object")
        name_elem = ET.SubElement(obj_elem, "name")
        name_elem.text = obj["name"]

        bbox_elem = ET.SubElement(obj_elem, "bndbox")
        xmin_elem = ET.SubElement(bbox_elem, "xmin")
        xmin_elem.text = str(obj["xmin"])
        ymin_elem = ET.SubElement(bbox_elem, "ymin")
        ymin_elem.text = str(obj["ymin"])
        xmax_elem = ET.SubElement(bbox_elem, "xmax")
        xmax_elem.text = str(obj["xmax"])
        ymax_elem = ET.SubElement(bbox_elem, "ymax")
        ymax_elem.text = str(obj["ymax"])

    tree = ET.ElementTree(root)
    tree.write(xml_filename)

def binary_mask_to_voc(binary_mask_filename, output_xml_filename):
    mask = cv2.imread(binary_mask_filename, cv2.IMREAD_GRAYSCALE)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    objects = []

    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)
        obj_info = {
            "name": f"object_{i+1}",
            "xmin": x,
            "ymin": y,
            "xmax": x + w,
            "ymax": y + h
        }
        objects.append(obj_info)

    height, width = mask.shape
    create_voc_xml(output_xml_filename, os.path.basename(binary_mask_filename), width, height, objects)

# Example usage
input_folder = "H:/workspace/Nabeel/yolov5/hr-training-miss-label"
output_folder = "H:/workspace/Nabeel/yolov5/hr-training-miss-xml"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for mask_filename in os.listdir(input_folder):
    if mask_filename.endswith(".jpg"):
        mask_path = os.path.join(input_folder, mask_filename)
        xml_filename = os.path.join(output_folder, os.path.splitext(mask_filename)[0] + ".xml")

        binary_mask_to_voc(mask_path, xml_filename)