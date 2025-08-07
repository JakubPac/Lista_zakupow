# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 15:17:41 2025

@author: jakub
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
from tkinter import simpledialog
import sqlite3

class BazaProduktow():
    
    def __init__(self, db_name = 'lista_db'):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.create_table()
        
    def create_table(self):
        c = self.conn.cursor()
        c.execute('''
                  CREATE TABLE IF NOT EXISTS ProductList (
                      id INTEGER PRIMARY KEY,
                      item TEXT UNIQUE NOT NULL
                      )
                  ''')
        self.conn.commit()
    
    def dodaj_produkt(self, product):
        c = self.conn.cursor()
        try:
            c.execute('''
                      INSERT INTO ProductList (item) VALUES (?)
                      ''', (product, ))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
        
    def usun_produkt(self, product):
        c = self.conn.cursor()
        c.execute('''
                  DELETE FROM ProductList WHERE item == ?
                 ''', (product,))
        self.conn.commit()

    
    def pobierz_produkty(self):
        c = self.conn.cursor()
        c.execute('SELECT item FROM ProductList')
        produkty = c.fetchall()  
        return [p[0] for p in produkty]  
    
    def zamknij_polaczenie(self):
        self.conn.close()

class ListaZakupow():
    def __init__(self, master, tasks):
        self.master = master
        self.baza = BazaProduktow()
        self.tasks = tasks
        self.master.title('Lista zakupow')
        self.master.geometry('600x400')
        self.master.configure(bg = 'grey')
        self.plus_b = tk.Button(self.master, text = '+', command = self.add_task, font = ('Arial', 14), fg = 'green')
        self.plus_b.pack(pady = 5)
        self.remove_b = tk.Button(self.master, text = 'Remove selected', command = self.remove_selected, font = ('Arial', 14), fg = 'red')
        self.remove_b.pack(pady = 5)
        self.load_tasks_from_db()
        
    def load_tasks_from_db(self):
        produkty = self.baza.pobierz_produkty()
        for produkt in produkty:
            self.frame = tk.Frame(self.master)
            self.frame.pack(fill=tk.X, padx=5, pady=2)
            self.var = tk.BooleanVar()
            check_b = tk.Checkbutton(self.frame, variable=self.var)
            check_b.pack(side=tk.LEFT)
            label = tk.Label(self.frame, text=produkt)
            label.pack(side=tk.LEFT, padx=5)
            button = tk.Button(self.frame, text='-', command=lambda f=self.frame, v=self.var, p=produkt: [f.destroy(), self.tasks.remove((f, v)), self.baza.usun_produkt(p)], fg='red')
            button.pack(side=tk.RIGHT)
            self.tasks.append((self.frame, self.var))
    
    def add_task(self):
        self.master.update()
        self.text = simpledialog.askstring('Add', 'Task:', parent = self.master)
        self.master.focus_force()
    
        if self.text and self.text.strip():
            product = self.text.strip()
            dodano = self.baza.dodaj_produkt(product)
            if dodano:
                frame = tk.Frame(self.master)
                frame.pack(fill=tk.X, padx=5, pady=2)
                var = tk.BooleanVar()
                check_b = tk.Checkbutton(frame, variable=var)
                check_b.pack(side=tk.LEFT)
                label = tk.Label(frame, text=product)
                label.pack(side=tk.LEFT, padx=5)
                button = tk.Button(frame, text='-', command=lambda f=frame, v=var, p=product: [f.destroy(), self.tasks.remove((f, v)), self.baza.usun_produkt(p)], fg='red')
                button.pack(side=tk.RIGHT)
                self.tasks.append((frame, var))
            else:
                tk.messagebox.showerror('Błąd', f'Produkt "{product}" już istnieje w bazie.')
        else:
            pass
            
    def remove_selected(self):
        for self.frame, self.var in self.tasks[:]:
            if self.var.get():
                for widget in self.frame.winfo_children():
                    if isinstance(widget, tk.Label):
                       product = widget.cget('text')
                       self.baza.usun_produkt(product)
                self.frame.destroy()
                self.tasks.remove((self.frame, self.var))
                
    def on_closing(self):
        self.baza.zamknij_polaczenie()
        self.master.destroy()
        
if __name__ == '__main__':
    tasks = []
    root = tk.Tk()
    lista_zakupow = ListaZakupow(root, tasks)
    root.protocol("WM_DELETE_WINDOW", lista_zakupow.on_closing)
    root.mainloop()      