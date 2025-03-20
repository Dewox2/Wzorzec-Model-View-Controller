import tkinter as tk
from tkinter import messagebox


class CDController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def add_album(self, title, artist, year, publisher):
        self.model.add_album(title, artist, year, publisher)
        self.view.show_message("Album dodany!")
    
    def remove_album(self, title):
        self.model.remove_album(title)
        self.view.show_message("Album usunięty!")
    
    def update_album(self, title, new_title=None, new_artist=None, new_year=None, new_publisher=None):
        self.model.update_album(title, new_title, new_artist, new_year, new_publisher)
        self.view.show_message("Album zaktualizowany!")
    
    def display_albums(self):
        self.view.update_view()
