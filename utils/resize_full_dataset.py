from PIL import Image
import os

datasetPath = "Food101N/Food-101N_release/images/"
proceesedPath = "Food101N_resized_224/"

for folderName in os.listdir(datasetPath):
  print("Computing for folder " + folderName)

  if not os.path.exists(proceesedPath + folderName):
    os.makedirs(proceesedPath + folderName)

  for fileName in os.listdir(datasetPath + folderName):
    im = Image.open(datasetPath + folderName + str("/") + fileName)
    im = im.resize((224, 224))
    im.save(proceesedPath + folderName + str("/") + fileName)