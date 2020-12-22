from tkinter import *

from Page import Page
from ButtonImage import ButtonImage


class MainPage(Page):

    def __init__(self, title, geometry):  # konstruktor tworzący glowne okno aplikacji
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(geometry)
        self.background_image = ButtonImage.find_image("bckground.png", 792, 700, "")
        background_label = Label(self.root, image=self.background_image['image'], width=self.background_image['x_size'],
                                 height=self.background_image['y_size'])
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.buttons_images = self.find_main_page_images()
        self.create_buttons(self.root, self.find_main_page_images())

    @staticmethod
    def find_main_page_images(): # metoda zwracajaca domyslne elementy GUI jako słownik
        global wplata_image,wyplata_image,stan_konta_image, interface_image, safety_image, button_test  # definicja zmiennych globalnych (PhotoImage Objects do not get garbage-collected)
        wyplata_image = ButtonImage.find_image("button_wyplata.png", 175, 47, "Wyjaśnienie funkcji wypłaty gotówki z bankomatu.")
        wplata_image = ButtonImage.find_image("button_wplata.png", 175, 47,"Wyjaśnienie funkcji wpłaty gotówki do bankomatu.")
        stan_konta_image = ButtonImage.find_image("button_stan.png", 175, 47, "Sprawdzanie stanu swojego konta bankowego.")
        interface_image = ButtonImage.find_image("button_interface.png", 175, 47, "Wyjaśnienie funkcji poszczególnych części fizycznych bankomatu.")
        button_test = ButtonImage.find_image("button_test.png", 72, 72, "Test wiedzy, sprawdzający zrozumienie zagadnień z instruktarzu.")
        safety_image = ButtonImage.find_image("button_exclamation.png", 72, 72, "Zasady bezpiecznego korzystania z bankomatu.")

        return [wplata_image, wyplata_image, stan_konta_image, interface_image, button_test, safety_image]
