from ButtonImage import ButtonImage
from Page import Page

class ButtonCommand:

    @staticmethod
    def withdraw(root):
        ButtonCommand.clear_root(root)
        withdraw_page = Page()
        withdraw_page.buttons_images = ButtonCommand.find_withdraw_buttons()
        withdraw_page.create_buttons(root, withdraw_page.buttons_images)

    @staticmethod
    def find_withdraw_buttons():  # metoda zwracajaca domyslne elementy GUI jako słownik
        global twenty_image, forty_image, fifty_image, hundred_image, two_hundred_image, inna_kwota_image  # definicja zmiennych globalnych (PhotoImage Objects do not get garbage-collected)
        twenty_image = ButtonImage.find_image("button_20.png", 175, 47,
                                               "Po naciśnięciu przycisku wypłacona zostanie dana kwota.",
                                               ButtonCommand.withdraw)
        forty_image = ButtonImage.find_image("button_40.png", 175, 47,
                                               "Po naciśnięciu przycisku wypłacona zostanie dana kwota.",
                                               ButtonCommand.withdraw)
        fifty_image = ButtonImage.find_image("button_50.png", 175, 47,
                                               "Po naciśnięciu przycisku wypłacona zostanie dana kwota.",
                                               ButtonCommand.withdraw)
        hundred_image = ButtonImage.find_image("button_100.png", 175, 47,
                                               "Po naciśnięciu przycisku wypłacona zostanie dana kwota.",
                                               ButtonCommand.withdraw)
        two_hundred_image = ButtonImage.find_image("button_200.png", 175, 47,
                                               "Po naciśnięciu przycisku wypłacona zostanie dana kwota.",
                                               ButtonCommand.withdraw)
        inna_kwota_image = ButtonImage.find_image("button_inna_kwota.png", 175, 47,
                                               "Po naciśnięciu przycisku uzytkownik zostanie poproszony o wpisanie kwoty,"
                                               "która ma zostać wypłacona przy użyciu klawiatury bankomatu.",
                                               ButtonCommand.withdraw)

        return [twenty_image, forty_image, fifty_image, hundred_image, two_hundred_image, inna_kwota_image]

    @staticmethod
    def clear_root(root):
        for i, child in enumerate(root.winfo_children()):
            if i > 0:
                child.destroy()
