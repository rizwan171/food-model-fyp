import numpy as np
import os
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import pathlib

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
print("Num CPUs Available: ", len(tf.config.list_physical_devices('CPU')))

datasetPath = "Food101N_pst_100/"
data_dir = pathlib.Path(datasetPath)
image_count = len(list(data_dir.glob('*/*.jpg')))
print(str(image_count) + " images")


with tf.device('/CPU'):

  # parameters
  batch_size = 64
  img_width = 64
  img_height = 64

  # training data
  training_dataset = []
  training_labels = []
  classes = []

  # load all images and labels
  for folderName in os.listdir(datasetPath):
    print("Computing for folder " + folderName)
    classes.append(folderName)
    for fileName in os.listdir(datasetPath + folderName):
      image = tf.keras.preprocessing.image.load_img(datasetPath + folderName + "/" + fileName)
      image_arr = tf.keras.preprocessing.image.img_to_array(image)
      image_arr = np.array(image_arr)  # Convert single image to a batch.

      training_dataset.append(image_arr)
      training_labels.append(folderName)

  # get total number of classes
  num_classes = len(classes)

  # one hot encode labels
  encodedLabels = []
  for label in training_labels:
    encodedLabels.append(classes.index(label))


  # load training data
  x_train = np.array(training_dataset[:int(float(len(training_dataset)) * 0.9)])
  y_train = np.array(encodedLabels[:int(float(len(training_dataset)) * 0.9)])
  y_train = tf.keras.utils.to_categorical(y_train, num_classes)
  print("Loaded training data")

  # split and load validation data
  x_valid = np.array(training_dataset[int(float(len(training_dataset)) * 0.9):])
  y_valid = np.array(encodedLabels[int(float(len(training_dataset)) * 0.9):])
  y_valid = tf.keras.utils.to_categorical(y_valid, num_classes)
  print("Loaded validation data")


  # # define the model
  model = Sequential([
    layers.experimental.preprocessing.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
    layers.Conv2D(32, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes, activation='softmax')
  ])
  
  # define the optimisation and loss functions
  model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
  
  training_dataset = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  label_mode="categorical",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

  validation_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    data_dir,
    validation_split=0.2,
    subset="validation",
    label_mode="categorical",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size)

with tf.device('/GPU'):

  # train the model
  epochs=20
  train = model.fit(
    x=training_dataset,
    batch_size=batch_size,
    validation_data=validation_dataset,
    epochs=epochs,
    shuffle=True
  )

  # train = model.fit(
  #   x=x_train,
  #   y=y_train,
  #   batch_size=batch_size,
  #   validation_data=(x_valid, y_valid),
  #   epochs=epochs,
  #   shuffle=True
  # )

  # save the model
  model.save('model.h5')
