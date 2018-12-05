from ImageHelper import ImageGenerator
import optparse

_DB_config = {'host': '127.0.0.1',
                      'user': 'user',
                      'password': 'password',
                      'database': 'database',
                      'port': 3360}


class ImageGenerator:

    def __init__(
        self,
        folder=None,
        font=None,
        fill=None,
        cycle=None,
        start_image_path=None,
        DB_save=None
    ):
        self.folder = folder
        self.font = font
        self.fill = fill
        self.cycle = cycle
        self.start_image_path = start_image_path
        self.DB_save = DB_save

    # folder = 'validation'
    # start_image_path = 'font.jpg'
    # font = 'Arial'
    # # font = 'Bahnschrift'
    # # font = 'Gabriola'
    # fill = (0, 0, 0, 255)
    # cycle = 1

    def run(self):

        ImageGenerator().img_gen(cycle=self.cycle,
                                 image_path=self.start_image_path,
                                 function_font=self.font,
                                 function_fill=self.fill,
                                 _DB_config=_DB_config,
                                 folder=self.folder,
                                 DB_save=self.DB_save)


if __name__ == '__main__':

    parser = optparse.OptionParser()

    folder = None,
    font = None,
    fill = (0, 0, 0, 255),
    cycle = None,
    start_image_path = None,
    DB_save = None

    parser.add_option(
        '-fl', '--folder',
        default=None,
        dest='folder',
        help='Folder to create and save')
    parser.add_option(
        '-fn', '--font',
        default='Arial',
        dest='font',
        help='Font of text')
    parser.add_option(
        '-fi', '--fill',
        default=(0, 0, 0, 255),
        dest='fill',
        help='Background fill')
    parser.add_option(
        '-c', '--cycle',
        default=5,
        dest='cycle',
        help='Number of cycles of network learning',
        type=int)
    parser.add_option(
        '-s', '--start_image_path',
        default=None,
        dest='start_image_path',
        help='Image start path')
    parser.add_option(
        '-d', '--db_save',
        default=False,
        dest='DB_save',
        help='Is saving to DB needed')

    options, args = parser.parse_args()
    data_creation = ImageGenerator(
        options.folder,
        options.font,
        options.fill,
        options.cycle,
        options.start_image_path,
        options.db_save)
    data_creation.run()
