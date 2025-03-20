import tkinter as tk
from tkinter import messagebox

class CDView:
    def __init__(self, root, controller):
        self.root = root
        self.root.title("CD Manager")
        self.root.geometry("550x500")
        self.root.configure(bg="#2c3e50")
        self.controller = controller
        
        # Stylizacja czcionki
        label_font = ("Arial", 12, "bold")
        entry_font = ("Arial", 12)
        button_font = ("Arial", 12, "bold")
        button_bg = "#3498db"
        button_fg = "white"
        
        # Pola tekstowe
        tk.Label(root, text="Tytuł:", font=label_font, fg="white", bg="#2c3e50").pack(pady=2)
        self.title_entry = tk.Entry(root, font=entry_font)
        self.title_entry.pack(pady=2)
        
        tk.Label(root, text="Wykonawca:", font=label_font, fg="white", bg="#2c3e50").pack(pady=2)
        self.artist_entry = tk.Entry(root, font=entry_font)
        self.artist_entry.pack(pady=2)
        
        tk.Label(root, text="Rok wydania:", font=label_font, fg="white", bg="#2c3e50").pack(pady=2)
        self.year_entry = tk.Entry(root, font=entry_font)
        self.year_entry.pack(pady=2)
        
        tk.Label(root, text="Wydawca:", font=label_font, fg="white", bg="#2c3e50").pack(pady=2)
        self.publisher_entry = tk.Entry(root, font=entry_font)
        self.publisher_entry.pack(pady=2)
        
        # Przyciski
        tk.Button(root, text="Dodaj album", font=button_font, bg=button_bg, fg=button_fg, command=self.add_album).pack(pady=5)
        tk.Button(root, text="Usuń album", font=button_font, bg=button_bg, fg=button_fg, command=self.remove_album).pack(pady=5)
        tk.Button(root, text="Edytuj album", font=button_font, bg=button_bg, fg=button_fg, command=self.edit_album).pack(pady=5)
        tk.Button(root, text="Odśwież listę", font=button_font, bg=button_bg, fg=button_fg, command=self.update_view).pack(pady=5)
        
        # Lista albumów - stylizowana
        self.album_frame = tk.Frame(root, bg="#34495e")
        self.album_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.album_listbox = tk.Listbox(self.album_frame, width=70, height=10, font=entry_font, bg="#ecf0f1", fg="#2c3e50", relief=tk.FLAT, borderwidth=5)
        self.album_listbox.pack(pady=5, padx=5, fill=tk.BOTH, expand=True)
        
        self.update_view()
    
    def add_album(self):
        title = self.title_entry.get()
        artist = self.artist_entry.get()
        year = self.year_entry.get()
        publisher = self.publisher_entry.get()
        if title and artist and year and publisher:
            self.controller.add_album(title, artist, year, publisher)
            self.clear_entries()
            self.update_view()
        else:
            messagebox.showwarning("Błąd", "Wszystkie pola muszą być wypełnione!")
    
    def remove_album(self):
        selected = self.album_listbox.curselection()
        if selected:
            title = self.album_listbox.get(selected[0]).split(" (")[0]
            self.controller.remove_album(title)
            self.update_view()
        else:
            messagebox.showwarning("Błąd", "Wybierz album do usunięcia!")
    
    def edit_album(self):
        selected = self.album_listbox.curselection()
        if selected:
            title = self.album_listbox.get(selected[0]).split(" (")[0]
            new_title = self.title_entry.get()
            new_artist = self.artist_entry.get()
            new_year = self.year_entry.get()
            new_publisher = self.publisher_entry.get()
            self.controller.update_album(title, new_title, new_artist, new_year, new_publisher)
            self.clear_entries()
            self.update_view()
        else:
            messagebox.showwarning("Błąd", "Wybierz album do edycji!")
    
    def update_view(self):
        self.album_listbox.delete(0, tk.END)
        albums = self.controller.model.get_albums()
        for album in albums:
            self.album_listbox.insert(tk.END, f"{album['title']} ({album['year']}), {album['artist']}, {album['publisher']}")
    
    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.artist_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.publisher_entry.delete(0, tk.END)
    
    def show_message(self, message):
        messagebox.showinfo("Informacja", message)

if __name__ == '__main__':
    root = tk.Tk()
    app = CDView(root, None)
    root.mainloop()