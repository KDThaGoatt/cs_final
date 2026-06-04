import tkinter as tk
from tkinter import *
from tkinter import ttk
from functions import myDB

class gui:
    def create_table(self):
        self.main_menu.pack_forget()

        self.table_create = tk.Frame(self.window)

        label1 = tk.Label(self.table_create, text="Enter the name for your table")
        self.name_entry = tk.Entry(self.table_create, width=20)
        label2 = tk.Label(self.table_create, text="How many rows are in your table? (Integer)")
        self.rows_entry = tk.Entry(self.table_create, width=20)
        label3 = tk.Label(self.table_create, text="ID autoincrement? (type True or False)")
        self.id_entry = tk.Entry(self.table_create, width=20)

        button1 = tk.Button(self.table_create, text="Continue", width=20,height=5,anchor="center", command=self.get_values)

        label1.grid(row=0, column=0, columnspan=3, sticky="n", pady=10)
        self.name_entry.grid(row=1,column=0,columnspan=3,sticky="n",pady=10)
        label2.grid(row=2, column=0, columnspan=3, sticky="n", pady=10)
        self.rows_entry.grid(row=3,column=0,columnspan=3,sticky="n",pady=10)
        label3.grid(row=4, column=0, columnspan=3, sticky="n", pady=10)
        self.id_entry.grid(row=5,column=0,columnspan=3,sticky="n",pady=10)
        button1.grid(row=6,column=0,columnspan=3,sticky="n",pady=10)


        self.table_create.pack()


    def get_values(self):
        self.table_name = self.name_entry.get()
        try:
            self.row_amount = int(self.rows_entry.get())
        except:
            print("Non integer inputted")
        try:
            self.id_bool = bool(self.id_entry.get())
        except:
            print("Non Bool value inputted")
        self.row_creation()
        

    def row_creation(self):
        self.table_create.pack_forget()
        row_list = []
        for i in range(self.row_amount):
            if i != 0:
                self.row_create.pack_forget()
            self.row_create = tk.Frame(self.window)

            label1 = tk.Label(self.row_create, text="Enter the title of your row, followed by the datatype in the format: title, datatype")


            label1.grid(row=0, column=0, columnspan=3, sticky="n", pady=10)
            label2.grid(row=1, column=0, columnspan=3, sticky="n", pady=10)

            self.row_create.pack()
    
    def datatype_screen(self):
            
            label1 = tk.Label(self.row_create, text="Datatypes:")
            label2 = tk.Label(self.row_create, text="INT / BIGINT: Whole numbers")
            label3 = tk.Label(self.row_create, text="DECIMAL / NUMERIC: Fixed point fractional numbers (exact)")
            label4 = tk.Label(self.row_create, text="FLOAT / REAL: Floating point fraction numbers (inexact)")
            label5 = tk.Label(self.row_create, text="CHAR(n): Fixed-length text strings, input the length you need as an integer for n")
            label6 = tk.Label(self.row_create, text="VARCHAR(n): Variable-length text strings, input the length you need as an integer for n")
            label7 = tk.Label(self.row_create, text="TEXT / LONGTEXT: Extremely large unstructured text blocks")
            label8 = tk.Label(self.row_create, text="DATE: Calendar dates without time")
            label9 = tk.Label(self.row_create, text="TIME: Duration or hour markers without date")
            
            



    def __init__(self):
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