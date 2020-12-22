from tkinter import *

import os


class ButtonImage:
    photo_image = None
    action = None

    @staticmethod
    def find_image(img_path, x_size, y_size, hover_over_txt, *action):
        my_path = os.path.abspath(os.path.dirname(__file__))
        photo_image = PhotoImage(file=os.path.join(my_path, "img/" + img_path))
        image_dict = {'image': photo_image, 'x_size': x_size, 'y_size': y_size, 'hover_over_txt': hover_over_txt, 
                      'action': action}
        return image_dict