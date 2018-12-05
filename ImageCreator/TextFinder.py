from PIL import Image
import pytesseract
from pytesseract import Output
import os
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

path = 'final.jpg'

# Converting image
img = Image.open(path)
img = img.convert('RGB')
img.show()
pix = img.load()
for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pix[x, y][0] < 150 or pix[x, y][1] < 150 or pix[x, y][2] < 150:
            pix[x, y] = (0, 0, 0, 255)
        else:
            pix[x, y] = (255, 255, 255, 255)
img.save('temp.jpg')
img.show()

# Finding Text in an image
text = pytesseract.image_to_data(Image.open('temp.jpg'), output_type=Output.DICT)
os.remove('temp.jpg')
list_of_images = []

for a, b in enumerate(text['text']):
    if b is not '':
        image_crop_tuple = (text['left'][a] - 5,
                            text['top'][a] - 5,
                            text['left'][a] + text['width'][a] + 5,
                            text['top'][a] + text['height'][a] + 5,)
        image = Image.open(path)
        image = image.convert('RGB')

        image.crop(image_crop_tuple).show()
        image.crop(image_crop_tuple).save('image' + str(a) + '.jpg')
        list_of_images.append(image.crop(image_crop_tuple))

print(list_of_images)