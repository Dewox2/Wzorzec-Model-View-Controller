import tkinter as tk
from tkinter import messagebox

class CDModel:
    def __init__(self):
        self.albums = []
    
    def add_album(self, title, artist, year, publisher):
        album = {'title': title, 'artist': artist, 'year': year, 'publisher': publisher}
        self.albums.append(album)
    
    def get_albums(self):
        return self.albums
    
    def remove_album(self, title):
        self.albums = [album for album in self.albums if album['title'] != title]
    
    def update_album(self, title, new_title=None, new_artist=None, new_year=None, new_publisher=None):
        for album in self.albums:
            if album['title'] == title:
                if new_title: album['title'] = new_title
                if new_artist: album['artist'] = new_artist
                if new_year: album['year'] = new_year
                if new_publisher: album['publisher'] = new_publisher
                break
   