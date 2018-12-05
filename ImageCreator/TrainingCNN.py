from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D
from tensorflow.python.keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow.python.keras import optimizers


# Data for training
train_dir = 'Images\\train'
val_dir = 'Images\\validation'
test_dir = 'Images\\test'

# images size
img_width, img_height = 110, 35

# data for the network's input
input_shape = (img_width, img_height, 3)

epochs = 2
batch_size = 16

# Images quantity for training
nb_train_samples = 30000
nb_validation_samples = 6600
nb_test_samples = 6600

datagen = ImageDataGenerator(rescale=1. / 255)

# Generator for folders with images
train_generator = datagen.flow_from_directory(
    train_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='sparse')

val_generator = datagen.flow_from_directory(
    val_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='sparse')

test_generator = datagen.flow_from_directory(
    test_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='sparse')

# Layers of network
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(3))
model.add(Activation('sigmoid'))

# Compiling model with several answers
model.compile(optimizer=optimizers.Adadelta(),
              loss='sparse_categorical_crossentropy',
              metrics=['sparse_categorical_accuracy'])
# Network learning run
model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=val_generator,
    validation_steps=nb_validation_samples // batch_size)

# Saving model wights
model.save('test_model.h5')
model.save_weights('test_model_weights.h5')

model_json = model.to_json()
json_file = open("test_model.json", "w")
json_file.write(model_json)
json_file.close()

# Accuracy of model depending on test images
print(model.evaluate_generator(test_generator, nb_test_samples // batch_size))

