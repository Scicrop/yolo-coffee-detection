import os
import sys
sys.path.append('yolov7')
from yolov7.simple_detect import detect


def is_valid_folder(folder):
    return os.path.exists(folder) and os.path.isdir(folder)


def find_file(diretorio_base, nome_arquivo):
    for root, dirs, files in os.walk(diretorio_base):
        if nome_arquivo in files:
            return os.path.join(root, nome_arquivo)
    return None

runs_folder = 'yolov7/runs/'
if is_valid_folder(runs_folder):
    weights = find_file(runs_folder+'/train', 'best.pt')
    base_folder_test_images = "test_images/"
    files = os.listdir(base_folder_test_images)
    for file in files:
        print("Detecting rust in file: " + file)
        detect(base_folder_test_images+file, weights)
else:
    print(runs_folder, 'is not a valid folder')