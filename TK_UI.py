import tkinter as tk

class TkEditUI:
    def __init__(self, root, app):
        self.root = root
        self.app = app

        # Setting up the main text area
        self.text_area = tk.Text(root, wrap="word", undo=True)
        self.text_area.pack(expand=True, fill=tk.BOTH)
        
        # Creating the menu bar
        self.create_menu()

    def create_menu(self):
        # Setting up the menu bar
        menu_bar = tk.Menu(self.root)
        
        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.app.open_file)
        file_menu.add_command(label="Save", command=self.app.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.app.exit_app)
        
        menu_bar.add_cascade(label="File", menu=file_menu)
        
        # Adding the menu bar to the root window
        self.root.config(menu=menu_bar)
