import os
from tkinter import *

from ButtonImage import ButtonImage
from ToolTip import ToolTip
from SynthSpeech import SynthSpeech


class Page:
    elements_images = None
    root = None
    background_image = None
    photos = []

    def __init__(self, title, geometry):  # konstruktor tworzący glowne okno aplikacji
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(geometry)
        self.background_image = ButtonImage.find_image("bckground.png", 792, 700, "")
        background_label = Label(self.root, image=self.background_image['image'], width=self.background_image['x_size'],
                                 height=self.background_image['y_size'])
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.run_action('main')

    @staticmethod
    def create_tool_tip(widget, text):
        toolTip = ToolTip(widget)

        def enter(event):
            toolTip.show_tip(text)

        def leave(event):
            toolTip.hide_tip()

        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)

    def get_root(self):
        return self.root

    def find_path(self):
        return os.path.abspath(os.path.dirname(__file__))

    def create_elements(self, setup_txt, current_action):    # funkcja tworząca przyciski symulujące bankomat
        elements = [None] * len(setup_txt)
        frames = [None] * len(setup_txt)
        frame_position_x, frame_position_y = -25, 330
        for i, image in enumerate(setup_txt):
            frames[i] = Frame(self.root)
            image = image.split(";")
            self.photos.append(PhotoImage(file=os.path.join(self.find_path(), "img/" + current_action + "/"+image[0])))
            if len(image) > 5 and image[5]:
                element_type = image[5].split('\n')[0]
                if element_type == 'entry':
                    elements[i] = Entry(frames[i])
            else:
                elements[i] = Button(frames[i])
                elements[i].pack()
                elements[i]['image'] = self.photos[i]
                if len(image) > 4 and image[4].split('\n')[0]:
                    action_name = image[4].split('\n')[0]
                    elements[i]['command'] = lambda: self.run_action(action_name)
            elements[i].pack()

            Page.create_tool_tip(elements[i], image[3])

            frames[i].pack()
            hover_over_label = Label(self.root, width=40)
            frame_position_x += 240 - (int(image[1]) / 4)
            if int(image[1]) < 100:
                frame_position_x += 25
            frames[i].place(x=frame_position_x, y=frame_position_y, bordermode=OUTSIDE, width=int(image[1]),
                            height=int(image[2]))
            if i % 2:
                frame_position_x = -25
                frame_position_y += 95
        # Page.clear_window(self.root)

    def run_action(self, action):
        self.clear_root()
        self.photos = []
        welcome_txt, setup_txt = ButtonImage.find_action_elements(action)
        self.speech_engine = SynthSpeech()
        self.speech_engine.start_synth_speech_thread(welcome_txt)
        self.create_elements(setup_txt, action)


    def clear_root(self):
        for i, child in enumerate(self.root.winfo_children()):
            if i > 0:
                child.destroy()
