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
  num_classes = 10

  # define the model
  # model = Sequential([
  #   layers.experimental.preprocessing.Rescaling(1./255, input_shape=(img_height, img_width, 3)),
  #   layers.Conv2D(32, 3, padding='same', activation='relu', input_shape=(img_height, img_width, 3)),
  #   layers.MaxPooling2D(),
  #   layers.Conv2D(64, 3, padding='same', activation='relu'),
  #   layers.MaxPooling2D(),
  #   layers.Conv2D(64, 3, padding='same', activation='relu'),
  #   layers.MaxPooling2D(),
  #   layers.Flatten(),
  #   layers.Dense(128, activation='relu'),
  #   layers.Dense(num_classes, activation='softmax')
  # ])

  
  #first creating the model
  model = Sequential()
  in_size=(img_height,img_width,3)
  model.add(layers.Conv2D(32,(3,3),activation='relu',input_shape=(in_size)))
  model.add(layers.MaxPooling2D(pool_size=(2,2)))
  model.add(layers.Conv2D(64, 3, padding='same', activation='relu'))
  model.add(layers.MaxPooling2D())
  model.add(layers.Conv2D(64, 3, padding='same', activation='relu'))
  model.add(layers.MaxPooling2D())
  model.add(layers.Flatten())
  model.add(layers.Dense(num_classes, activation='softmax'))


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

  print(type(training_dataset))
# with tf.device('/GPU'):

#   # train the model
#   epochs=20
#   train = model.fit(
#     x=training_dataset,
#     batch_size=batch_size,
#     validation_data=validation_dataset,
#     epochs=epochs,
#     shuffle=True
#   )

#   # save the model
#   model.save('model.h5')

#   model.summary()