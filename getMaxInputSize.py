from PIL import Image
import os

# get the parent folder
path = "Food101N/Food-101N_release/images/"
widths = []
heights = []

# for all folders, loop through all images and append their widths and heights
for folderName in os.listdir(path):
  print("Computing for folder " + folderName)
  for fileName in os.listdir(path + folderName):
    im = Image.open(path + folderName + str("/") + fileName)
    w, h = im.size
    widths.append(w)
    heights.append(h)

# write the max width and height to a file
f = open("maxSizes.txt", "a")
f.write("max width: " + str(max(widths)) + "\n")
f.write("max height: " + str(max(heights)))
f.close()