import numpy as np
import requests
from PIL import Image
from pycocotools.coco import COCO
# https://leimao.github.io/blog/Inspecting-COCO-Dataset-Using-COCO-API/
coco_annotation_file_path = "data/v-coco/data/instances_vcoco_all_2014.json"

coco_annotation = COCO(annotation_file=coco_annotation_file_path)

# with open('data/v-coco/data/splits/vcoco_train.ids') as f:
#     lines = f.read().splitlines()
# lines = list(map(int, lines))
# print(lines)
# coco_annotation.download(tarDir='data/v-coco/Images/train2014',imgIds=lines)

def download(train_test_val):
  with open(f'data/v-coco/data/splits/vcoco_{train_test_val}.ids') as f:
    lines = f.read().splitlines()
  lines = list(map(int, lines))
  print(lines)
  coco_annotation.download(tarDir=f'data/v-coco/Images/{train_test_val}2014',imgIds=lines)

# download('val')
# download('test')

def download(train_test_val, lines):
  
  # with open(f'data/v-coco/data/splits/vcoco_{train_test_val}.ids') as f:
  #   lines = f.read().splitlines()
  # lines = list(map(int, lines))
  print(lines)
  coco_annotation.download(tarDir=f'data/v-coco/Images/{train_test_val}2014',imgIds=lines)

download(train_test_val='train', lines=[292213])