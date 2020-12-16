from tkinter import *
from Image import ImageButton
from ToolTip import ToolTip

class Page():
    @staticmethod
    def find_default_images(): ##metoda zwracajaca domyslne elementy GUI jako słownik
        global wplata_image,wyplata_image,stan_konta_image, interface_image, safety_image, button_test  # definicja zmiennych globalnych (PhotoImage Objects do not get garbage-collected)
        wyplata_image = ImageButton.find_image("button_wyplata.png", 175, 47, "Tutaj wyjaśniamy funkcje wypłacania gotówki z bankomatu.")
        wplata_image = ImageButton.find_image("button_wplata.png", 175, 47,"Tutaj wyjaśniamy funkcje wpłacania gotówki do bankomatu.")
        stan_konta_image = ImageButton.find_image("button_stan.png", 175, 47, "Tutaj pokazujemy jak sprawdzić stan swojego konta bankowego.")
        interface_image = ImageButton.find_image("button_interface.png", 175, 47, "Tutaj wyjaśnione są funkcje poszczególnych części fizycznych bankomatu.")
        button_test = ImageButton.find_image("button_test.png", 72, 72, "Test wiedzy, sprawdzający zrozumienie zagadnień wyjaśnionych w instruktarzu.")
        safety_image = ImageButton.find_image("button_exclamation.png", 72, 72, "Zasady bezpieczeństwa podczas korzystania z bankomatu.")


        return [wplata_image, wyplata_image, stan_konta_image, interface_image, button_test, safety_image]

    @staticmethod
    def create_tool_tip(widget, text):
        toolTip = ToolTip(widget)

        def enter(event):
            toolTip.showtip(text)

        def leave(event):
            toolTip.hidetip()

        widget.bind('<Enter>', enter)
        widget.bind('<Leave>', leave)


    def __init__(self):                 ## konstruktor tworzący glowne okno aplikacji
        root = Tk()
        root.title("Nauka obsługi bankomatu")
        root.geometry("700x792")
        background_image = ImageButton.find_image("bckground.png", 792, 700, "")
        background_label = Label(root, image=background_image['image'], width=background_image['x_size'],
                                 height=background_image['y_size'])
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.create_launch_buttons(root)
        root.mainloop()

    def create_launch_buttons(self, window): ## funkcja tworząca przyciski symulujące bankomat
        buttons_images = self.find_default_images()
        buttons = [None] * len(buttons_images)
        frames = [None] * len(buttons_images)
        frame_position_x, frame_position_y = -25, 330
        for i, image in enumerate(buttons_images):
            frames[i] = Frame(window)
            buttons[i] = Button(frames[i], image = image['image'])
            buttons[i].pack()
            self.create_tool_tip(buttons[i], image['hover_over_txt'])

            frames[i].pack()
            hover_over_label = Label(window, width=40)
            frame_position_x += 240 - (image['x_size'] / 4)
            if image['x_size'] < 100:
                frame_position_x += 25
            frames[i].place(x=frame_position_x, y=frame_position_y, bordermode=OUTSIDE, width=image['x_size'], height=image['y_size'])
            if i % 2:
                frame_position_x = -25
                frame_position_y += 95

        def enter(self, event):
            self.showtip()

        def leave(self, event):
            self.hidetip()