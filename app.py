import os
import sys

sys.path.append('yolov7')
import cv2
from yolov7.simple_detect import detect


def is_valid_folder(folder):
    return os.path.exists(folder) and os.path.isdir(folder)


def find_file(diretorio_base, nome_arquivo):
    for root, dirs, files in os.walk(diretorio_base):
        if nome_arquivo in files:
            return os.path.join(root, nome_arquivo)
    return None


def returnCameraIndexes():
    # checks the first 10 indexes.
    index = 0
    arr = []
    i = 10
    while i > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i -= 1
    return arr


def main(args):
   if args[1] == 'detect':
        detect(args[2], args[3])

   elif args[1] == 'check_webcams':
        cam_array = returnCameraIndexes()
        print("Available cameras: ", cam_array)


if __name__ == "__main__":
    main(sys.argv)
