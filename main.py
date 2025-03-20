from model import CDModel
from controller import CDController
from view import CDView
import tkinter as tk
from tkinter import messagebox

def main():
    model = CDModel()
    root = tk.Tk()
    controller = CDController(model, None)
    view = CDView(root, controller)
    controller.view = view  # Przekazanie widoku do kontrolera
    root.mainloop()

if __name__ == '__main__':
    main()