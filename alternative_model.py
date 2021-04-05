#first creating the model
model = Sequential()

#now adding layers
in_size=(28,28,1)
# "Rectified Linear Activation" has been proven to work well for neural networks.
# The number of filters here can be experimented with, using 32 or 64
model.add(Conv2D(32,(3,3),activation='relu',input_shape=(in_size)))
# the pool_size can be experimented with 2 by 2 and 3 by 3
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
#connects the layers
model.add(Dense(100, activation='relu'))
# helps avoiding overfittiung, can be experimented with 0.25 or 0.5
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

#Specifiying the optimizer being used
exp = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)

model.compile(loss='categorical_crossentropy', optimizer = exp, metrics = ['accuracy'])