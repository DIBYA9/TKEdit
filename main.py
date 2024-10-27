import tkinter as tk
from tkinter import filedialog, messagebox
from TK_UI import TkEditUI 

class TkEditApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TkEdit - Simple Text Editor")
        self.root.geometry("600x400")

        # Initializing the TkEditUI class to set up the UI
        self.ui = TkEditUI(root, self)
        
    # Function to open a file
    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", 
                                               filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.ui.text_area.delete(1.0, tk.END) 
            self.ui.text_area.insert(tk.END, content) 
            self.root.title(f"TkEdit - {file_path}")

    # Function to save a file
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.ui.text_area.get(1.0, tk.END)
                file.write(content)
            self.root.title(f"TkEdit - {file_path}")

    # Function to exit the application
    def exit_app(self):
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TkEditApp(root)
    root.mainloop()
