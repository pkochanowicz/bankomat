from ButtonImage import ButtonImage
from Page import Page


class ButtonCommand:
    def withdraw(self, root):
        self.clear_root(root)
        withdraw_page = Page()
        welcome_txt, setup_txt = ButtonImage.find_action_buttons('withdraw')

        withdraw_page.create_buttons(root, setup_txt)

    def clear_root(self, root):
        for i, child in enumerate(root.winfo_children()):
            if i > 0:
                child.destroy()
