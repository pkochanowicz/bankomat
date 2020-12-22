
class ButtonCommand:

    @staticmethod
    def withdraw(root):
        ButtonCommand.clear_root(root)
        

    @staticmethod
    def clear_root(root):
        for i, child in enumerate(root.winfo_children()):
            if i > 0:
                child.destroy()
