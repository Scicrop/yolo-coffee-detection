import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

i = 0
limit = 10000 # max images to print
for imageName in glob.glob('runs/detect/exp2/*.jpg'): #assuming JPG
    if i < limit:
        img = mpimg.imread(imageName)
        plt.imshow(img)
        plt.axis('off') # Ocultar os eixos
        plt.show()
        print("\n")
    i = i + 1
