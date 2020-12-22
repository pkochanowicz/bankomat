from tkinter import *

from ToolTip import ToolTip
from ButtonCommand import ButtonCommand


class Page:
    buttons_images = None
    root = None
    background_image = None

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

    def create_buttons(self, window, buttons):    # funkcja tworząca przyciski symulujące bankomat
        buttons = [None] * len(self.buttons_images)
        frames = [None] * len(self.buttons_images)
        frame_position_x, frame_position_y = -25, 330
        for i, image in enumerate(self.buttons_images):
            frames[i] = Frame(window)
            buttons[i] = Button(frames[i], image=image['image'])
            buttons[i].pack()
            if image['command']:
                command = image['command'][0]
                buttons[i]['command'] = lambda: ButtonCommand.withdraw(self.root)


            Page.create_tool_tip(buttons[i], image['hover_over_txt'])

            frames[i].pack()
            hover_over_label = Label(window, width=40)
            frame_position_x += 240 - (image['x_size'] / 4)
            if image['x_size'] < 100:
                frame_position_x += 25
            frames[i].place(x=frame_position_x, y=frame_position_y, bordermode=OUTSIDE, width=image['x_size'],
                            height=image['y_size'])
            if i % 2:
                frame_position_x = -25
                frame_position_y += 95
        # Page.clear_window(self.root)
