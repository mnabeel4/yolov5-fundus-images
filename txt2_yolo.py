import xml.etree.ElementTree as ET
from tqdm import tqdm
import os
from os import getcwd

sets=['train','val']

classes = [
'Blood vessels']


def convert(size,box):
    # dw = 1./(size[1])
    # dh = 1./(size[0])
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x=(box[0]+box[1])/2.0-1
    y=(box[2]+box[3])/2.0-1
    w=box[1]-box[0]
    h=box[3]-box[2]
    x=x*dw
    w=w*dw
    y=y*dh
    h=h*dh
    return x,y,w,h

def convert_annotation(image_set, image_id):
    #in_file=open('./Annotations/%s.xml'%(image_id),encoding='utf-8')
    #if not os.path.exists('./yolo_set/labels/%s/'%(image_set)):
    #    os.makedirs('./yolo_set/labels/%s/'%(image_set))
    #out_file=open('./yolo_set/labels/%s/%s.txt'%(image_set,image_id), 'w',encoding='utf-8')

    #Hand-Held Probe Lesion VOC Dataset root
    #xmlRoot = 'G:/2021-07-09Dat4Set 4 Hand-held Probe SSD/2021-07-09DataSet 4 Hand-held Probe SSD/Hand-held-Probe/Lesion Annots'
    xmlRoot = 'H:/workspace/Nabeel/yolov5/HR-xml'
    xmlpath = '%s/%s.xml' % (xmlRoot, image_id)
    print(xmlpath)

    in_file = open(xmlpath, encoding='utf-8')
    out_file = open('./HR-yoloset1/labels/%s/%s.txt' % (image_set, image_id), 'w', encoding='utf-8')

    tree=ET.parse(in_file)
    root=tree.getroot()
    size=root.find('size')
    h=int(size.find('height').text)
    w=int(size.find('width').text)
    for obj in root.iter('object'):
        #difficult=obj.find('difficult').text
        # cls=obj.find('name').text
        # if cls not in classes or int(difficult)==1:
        #     continue
        # cls_id=classes.index(cls)
        cls_id = 0
        xmlbox=obj.find('bndbox')
        b=(float(xmlbox.find('xmin').text),float(xmlbox.find('xmax').text),float(xmlbox.find('ymin').text),float(xmlbox.find('ymax').text))
        b1,b2,b3,b4=b
        if b2>w:
            b2=w
        if b4>h:
            b4=h
        b=(b1,b2,b3,b4)
        bb=convert((w,h),b)
        # print(str(cls_id)+" "+" ".join([str(a) for a in bb])+"\n")
        out_file.write(str(cls_id)+" "+" ".join([str(a) for a in bb])+"\n")

wd=getcwd()
for image_set in sets:
    if not os.path.exists('./HR-yoloset1/'):
        os.makedirs('./HR-yoloset1/')
    if not os.path.exists('./HR-yoloset1/labels/'):
        os.makedirs('./HR-yoloset1/labels/')
    if not os.path.exists('./HR-yoloset1/labels/%s/' % (image_set)):
        os.makedirs('./HR-yoloset1/labels/%s/' % (image_set))

    image_ids=open('./HR-VOC1/index/%s.txt'%(image_set))
    for image_id in tqdm(image_ids):
        image_id=image_id.replace('\n','')
        # image_id='Lesion_1.2.840.42157.3.152.235.2.12.131613391185074746'
        # convert VOC's type to yolo txt
        convert_annotation(image_set, image_id)
        print('Finish: %s' % (image_id))
        # break


