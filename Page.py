import os
from tkinter import *

from ButtonImage import ButtonImage
from ToolTip import ToolTip


class Page:
    buttons_images = None
    root = None
    background_image = None
    photos = []

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

    def create_buttons(self, setup_txt):    # funkcja tworząca przyciski symulujące bankomat
        buttons = [None] * len(setup_txt)
        frames = [None] * len(setup_txt)
        frame_position_x, frame_position_y = -25, 330
        for i, image in enumerate(setup_txt):
            frames[i] = Frame(self.root)
            image = image.split(";")
            self.photos.append(PhotoImage(file=os.path.join(self.find_path(), "img/" + image[4] + "/"+image[0])))
            buttons[i] = Button(frames[i])
            buttons[i].pack()
            if image[4]:
                command = getattr(self, image[4])
                buttons[i]['command'] = lambda: command()
                buttons[i]['image'] = self.photos[i]
                buttons[i].pack()

            Page.create_tool_tip(buttons[i], image[3])

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

    def withdraw(self):
        self.clear_root()
        self.photos = []
        welcome_txt, setup_txt = ButtonImage.find_action_buttons('withdraw')
        self.create_buttons(setup_txt)

    def clear_root(self):
        for i, child in enumerate(self.root.winfo_children()):
            if i > 0:
                child.destroy()
