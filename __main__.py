from MainPage import *
from Page import Page

if __name__ == "__main__":
    main_page = MainPage("Nauka obsługi bankomatu", "700x792")
    root = main_page.get_root()
    root.mainloop()
