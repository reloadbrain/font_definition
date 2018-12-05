from keras_preprocessing import image
import numpy as np
from tensorflow.python.keras.models import load_model
from PIL import Image

# https://github.com/kakul/Alyn
# Alyn's deskew tool
from alyn import Deskew

img_path = 'ImageCreator\\test.jpg'

d = Deskew(input_file=img_path,
           display_image='preview the image on screen',
           output_file='final.jpg',
           r_angle=0)
d.run()

img = Image.open('ImageCreator\\image.jpg')
img = img.resize((110, 35), Image.BILINEAR)
img.show()
img.save(img_path)
img = image.load_img(img_path, target_size=(110, 35))

# Image preparation
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

# Model loading and using for image to determine
model = load_model('test_model.h5')
prediction = model.predict(x)
print(str(prediction))