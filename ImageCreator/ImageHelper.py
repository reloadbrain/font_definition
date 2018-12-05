from PIL import Image, ImageDraw, ImageFont
import random
from DBcm import UseDatabase, CustomException


class ImageGenerator:
    def img_gen(self,
                cycle: int,
                image_path: str,
                _DB_config: dict,
                function_font: str = 'Arial',
                function_fill: tuple = (0, 0, 0, 255),
                folder: str = '',
                DB_save = False) -> object:

        # Creating an image for network training.
        # The amount of images depends on cycle's parameter.

        font_function_path = 'C:\WINDOWS\\fonts\\' + function_font + '.ttf'
        font = ImageFont.truetype(font_function_path, 18)

        while cycle > 0:

            image = Image.open(image_path)
            draw = ImageDraw.ImageDraw(image)
            xy = (random.randint(100, image.size[0])-100, random.randint(100, image.size[1])-100)

            # Russian text
            text = ''
            for i in range(7):
                text += str(chr(random.randint(1040, 1103)))

            # English text
            # text = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=10))

            draw.text(xy=xy, text=text, font=font, fill=function_fill)

            # saving the image
            new_image_path = 'ImageCreator\Images\\' + folder + '\\' + function_font + '\\' \
                             + str(cycle) + '_' + str(function_font) + '.jpg'

            image.crop((xy[0]-10, xy[1]-10, 100+xy[0], 25+xy[1])).save(new_image_path)

            if DB_save is True:
                # saving the image's path and font to DB
                ImageGenerator().img_save_toDB(path=new_image_path, font=function_font, _DB_config=_DB_config)
                print('Cycles left: ' + str(cycle))
                cycle -= 1

    def img_save_toDB(self, path: str, font: str, _DB_config) -> None:

        # Simple insert of images to local DB

        try:
            with UseDatabase(_DB_config) as cursor:

                _SQL = """insert into image_path (path, font) values (%s, %s)"""
                cursor.execute(_SQL, (path, font))

        except Exception as error:
            print(error)
