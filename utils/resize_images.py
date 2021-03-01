from PIL import Image
import os

datasetPath = "Food101N_subset_100/"
proceesedPath = "Food101N_ps_100/"

for folderName in os.listdir(datasetPath):
  print("Computing for folder " + folderName)

  if not os.path.exists(proceesedPath + folderName):
    os.makedirs(proceesedPath + folderName)

  for fileName in os.listdir(datasetPath + folderName):
    im = Image.open(datasetPath + folderName + str("/") + fileName)
    im = im.resize((64, 64))
    im.save(proceesedPath + folderName + str("/") + fileName)