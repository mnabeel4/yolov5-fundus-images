import os
import xml.etree.ElementTree as ET

# Directory containing your XML files
directory = 'H:/workspace/Nabeel/yolov5/hr-training-miss-xml'


# Function to replace object names with "blood vessel"
def replace_object_names(file_path):
    try:
        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Replace object names with "blood vessel"
        for obj in root.findall('object'):
            name_tag = obj.find('name')
            name_tag.text = 'blood vessel'

        # Write the modified XML back to the file
        tree.write(file_path)
        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")


# Iterate through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.xml'):
        file_path = os.path.join(directory, filename)
        replace_object_names(file_path)
