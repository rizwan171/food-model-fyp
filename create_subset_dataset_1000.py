import os
import shutil

# define both the location of the orginal dataset and the new subset that will be created
originalDatasetPath = "Food101N/Food-101N_release/images/"
subsetPath = "Food101N_subset_1000/"

# for all folders, loop through all images and copy the first 500 in each directory
for folderName in os.listdir(originalDatasetPath):
  print("Copying in folder " + folderName)

  # create the new folder in the subset directory
  if not os.path.exists(subsetPath + folderName):
    os.makedirs(subsetPath + folderName)

  fileCounter = 0
  for fileName in os.listdir(originalDatasetPath + folderName):
    if fileCounter == 1000:
      break

    shutil.copy(originalDatasetPath + folderName + "/" + fileName, subsetPath + folderName)
    fileCounter += 1