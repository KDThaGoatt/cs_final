import tkinter as tk
from tkinter import *
from tkinter import ttk
from functions import myDB
import sqlite3

class gui:
    def create_table(self):
        self.main_menu.pack_forget()

        self.table_create = tk.Frame(self.window)

        label1 = tk.Label(self.table_create, text="Enter the name for your table")
        name_entry = tk.Entry(self.table_create, width=20)
        label2 = tk.Label(self.table_create, text="How many rows are in your table? (Integer)")
        rows_entry = tk.Entry(self.table_create, width=20)
        label3 = tk.Label(self.table_create, text="ID autoincrement? (type True or False)")
        id_entry = tk.Entry(self.table_create, width=20)
        button1 = tk.Button(self.table_create, text="Continue", width=20,height=5,anchor="center",command=myDB.create_table(self, name_entry.get(), rows_entry.get(), id_entry.get()))

        label1.grid(row=0, column=0, columnspan=3, sticky="n", pady=10)
        name_entry.grid(row=1,column=0,columnspan=3,sticky="n",pady=10)
        label2.grid(row=2, column=0, columnspan=3, sticky="n", pady=10)
        rows_entry.grid(row=3,column=0,columnspan=3,sticky="n",pady=10)
        label3.grid(row=4, column=0, columnspan=3, sticky="n", pady=10)
        id_entry.grid(row=5,column=0,columnspan=3,sticky="n",pady=10)
        button1.grid(row=6,column=0,columnspan=3,sticky="n",pady=10)

        self.table_create.pack()


    def __init__(self):
        file = 'dbase.db'
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

        self.window = tk.Tk()
        self.window.title("Database Manager 9000")
        self.window.geometry("1000x675")

        #MAIN MENU

        self.main_menu = tk.Frame(self.window)

        label1 = tk.Label(self.main_menu, text="Main Menu", font=("Arial", 16))

        button1 = tk.Button(self.main_menu, text="Create Tables", width=20, height=5, anchor="center", command=self.create_table)
        button2 = tk.Button(self.main_menu, text="Add Entries", width=20, height=5, anchor="center")
        button3 = tk.Button(self.main_menu, text="Edit Entries", width=20, height=5, anchor="center")
        button4 = tk.Button(self.main_menu, text="Search For Entries", width=20, height=5, anchor="center")

        label1.grid(row=0,column=0,columnspan=3,sticky="n",pady=10)
        button1.grid(row=1, column=0, padx=10,pady=10)
        button2.grid(row=1,column=1,padx=10,pady=10)
        button3.grid(row=2,column=0,padx=10,pady=10)
        button4.grid(row=2,column=1,padx=10,pady=10)

        self.main_menu.pack()

        self.window.mainloop()

gui()