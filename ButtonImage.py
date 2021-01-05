import tkinter

import os


class ButtonImage:
    photo_image = None

    @staticmethod
    def find_image(img_path, x_size, y_size, hover_over_txt, *command):
        my_path = os.path.abspath(os.path.dirname(__file__))
        photo_image = tkinter.PhotoImage(file=os.path.join(my_path, "img/" + img_path))
        image_dict = {'image': photo_image, 'x_size': x_size, 'y_size': y_size, 'hover_over_txt': hover_over_txt, 
                      'command': command}
        return image_dict

    @staticmethod
    def find_action_buttons(action):
        my_path = os.path.abspath(os.path.dirname(__file__))
        filelist = os.listdir(os.path.join(my_path, 'img/' + action + '/'))
        setup_file = None
        for file in filelist[:]:
            if file.endswith(".txt"):
                setup_file = file
            elif not (file.endswith(".png")):
                filelist.remove(file)
        welcome_txt, setup_txt = ButtonImage.read_instruction_file(action, setup_file)
        return welcome_txt, setup_txt

    @staticmethod
    def read_instruction_file(action, setup_file):
        setup_txt_file = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'img/' + action + '/' + setup_file), "r")
        setup_txt = setup_txt_file.readlines()
        setup_txt_file.close()
        welcome_txt = setup_txt[0]
        setup_txt.remove(setup_txt[0])
        return welcome_txt, setup_txt