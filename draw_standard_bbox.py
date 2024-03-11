import os
import xml.etree.ElementTree  as ET
import cv2

#yolo_img_root = 'G:/Hand-held Probe SSD ValidationSet/Hand-held Probe SSD ValidationSet/Image'
yolo_img_root = 'H:/workspace/Nabeel/yolov5-master-new/yolo_set6/images/test'
xml_root = 'H:/workspace/Nabeel/yolov5-master-new/yolo_set6/images/test-xml'
dstRoot = 'H:/workspace/Nabeel/yolov5-master-new/yolo_set6/images/tested-images'



if not os.path.exists(dstRoot):
    os.mkdir(dstRoot)

for img in os.listdir(yolo_img_root):
    iname = img[:-4]
    for xml in os.listdir(xml_root):
        xname = xml[:-4]
        if iname == xname:
            xmlpath = os.path.join(xml_root, xml)
            xmlfile = open(xmlpath, encoding='utf-8')
            tree = ET.parse(xmlfile)
            root = tree.getroot()

            imgpath = os.path.join(yolo_img_root, img)
            mat = cv2.imread(imgpath)
            darwpath = os.path.join(dstRoot, img)

            saveflag = True

            size = root.find('size')
            w = int(size.find('width').text)
            h = int(size.find('height').text)
            for obj in root.iter('object'):
                # difficult = obj.find('difficult').text
                cls = obj.find('name').text

                if cls.find('_HP') > 0 or cls.find('ZS') > 0:
                    saveflag = False
                    break

                xmlbox = obj.find('bndbox')
                b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
                     float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
                x1, x2, y1, y2 = b

                # 标注越界修正
                if x2 > w:
                    x2 = w
                if y2 > h:
                    y2 = h
                b = (x1, x2, y1, y2)

                # print('%d, %d, %d, %d' % (x1, x2, y1, y2))

                pt1 = (int(x1), int(y1))
                pt2 = (int(x2), int(y2))
                color = (255, 0, 255)
                cv2.rectangle(mat, pt1, pt2, color, 4, 4)

            # cv2.imshow('show', mat)
            # cv2.waitKey(33)

            if saveflag:
                cv2.imwrite(darwpath, mat)