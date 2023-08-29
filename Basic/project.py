import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

# Set the parameters for training
batch_size = 32
epochs = 10
target_size = (128, 128)
input_shape = (128, 128, 3)
num_classes = 7

# Define the list of class names
class_names = ['10', '20', '50', '100', '200', '500', '2000']

# Set the paths to the training and validation directories
train_dir = 'path/to/train_dir'
val_dir = 'path/to/val_dir'

# Create the data generators for training and validation
train_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(train_dir, target_size=target_size, batch_size=batch_size, class_mode='categorical', shuffle=True)
val_datagen = ImageDataGenerator(rescale=1./255)
val_generator = val_datagen.flow_from_directory(val_dir, target_size=target_size, batch_size=batch_size, class_mode='categorical', shuffle=False)

# Build the model architecture
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dropout(0.5))
model.add(Dense(512, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(train_generator, epochs=epochs, validation_data=val_generator)

# Save the trained model
model.save('path/to/model.h5')

# Load the trained model
model = load_model('path/to/model.h5')

# Prompt the user to enter the path to the input image file
image_path = input('Enter path to image file: ')

# Load the input image and make a prediction on the image
img = load_img(image_path, target_size=target_size)
x = img_to_array(img)
x = x / 255.
x = tf.expand_dims(x, axis=0)
preds = model.predict(x)[0]
class_idx = preds.argmax()
class_name = class_names[class_idx]

# Print the predicted class name
print('Predicted class:', class_name)
