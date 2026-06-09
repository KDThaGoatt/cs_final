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
        self.viewedData = False
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
        self.row_list = []
        self.table_create.pack_forget()
        if self.viewedData == True:
            self.datatypes.pack_forget()
            self.viewedData = False
        self.last_row = False

        self.wait_var = tk.IntVar()
        for i in range(self.row_amount):
            if i != 0:
                self.row_create.pack_forget()
            self.row_create = tk.Frame(self.window)

            label1 = tk.Label(self.row_create, text="Enter the title and datatype of your row")
            label2 = tk.Label(self.row_create, text=f"Row {i}")
            label3 = tk.Label(self.row_create, text="Enter the name of your row")
            label4 = tk.Label(self.row_create, text="Enter the datatype of your row")


            self.rowentry = tk.Entry(self.row_create, width=20)
            self.row_datatype_entry = tk.Entry(self.row_create, width=20)

            button1 = tk.Button(self.row_create, text="View Datatypes", width=20,height=5,anchor="center", command=self.datatype_screen)

            button2 = tk.Button(self.row_create, text="Enter", width=20,height=5,anchor="center", command=self.row_list_build)
            
            if i == (self.row_amount-1):
                self.last_row = True

            label1.grid(row=0, column=0, columnspan=3, sticky="n", pady=10)
            label2.grid(row=2, column=0, columnspan=3, sticky="n", pady=10)
            label3.grid(row=3, column=0, columnspan=3, sticky="n", pady=10)
            label4.grid(row=5, column=0, columnspan=3, sticky="n", pady=10)

            self.rowentry.grid(row=4,column=0,columnspan=3,sticky="n",pady=10)
            self.row_datatype_entry.grid(row=6,column=0,columnspan=3,sticky="n",pady=10)

            button1.grid(row=1, column=0, columnspan=3, sticky="n", pady=10)
            button2.grid(row=7,column=0,columnspan=3,sticky="n",pady=10)

            self.row_create.pack()

            button1.wait_variable(self.wait_var)

    def row_list_build(self):
        db_create = myDB()
        row_name = self.rowentry.get()
        row_datatype = self.row_datatype_entry.get()
        self.row_list.append(row_name)
        self.row_list.append(row_datatype)
        print(self.row_list)
        if self.last_row == True:
            db_create.create_table(self.table_name,self.row_list,self.id_bool)
            if self.id_bool == True:
                print(f"You have created a table with the name {self.table_name}, {self.row_amount} rows and ID autoincrement")
            if self.id_bool == False:
                print(f"You have created a table with the name {self.table_name}, {self.row_amount} rows and no ID autoincrement")

            self.row_create.pack_forget()
            self.main_menu.pack()
        else:
            self.wait_var.set(1)


    
    def datatype_screen(self):
            self.row_create.pack_forget()

            self.datatypes = tk.Frame(self.window)
            
            label1 = tk.Label(self.datatypes, text="Datatypes")
            label2 = tk.Label(self.datatypes, text="INT / BIGINT: Whole numbers")
            label3 = tk.Label(self.datatypes, text="DECIMAL / NUMERIC: Fixed point fractional numbers (exact)")
            label4 = tk.Label(self.datatypes, text="FLOAT / REAL: Floating point fraction numbers (inexact)")
            label5 = tk.Label(self.datatypes, text="CHAR(n): Fixed-length text strings, input the length you need as an integer for n")
            label6 = tk.Label(self.datatypes, text="VARCHAR(n): Variable-length text strings, input the length you need as an integer for n")
            label7 = tk.Label(self.datatypes, text="TEXT / LONGTEXT: Extremely large unstructured text blocks")
            label8 = tk.Label(self.datatypes, text="DATE: Calendar dates without time")
            label9 = tk.Label(self.datatypes, text="TIME: Duration or hour markers without date")
            label10 = tk.Label(self.datatypes, text="DATETIME / TIMESTAMP: Calendar date aswell as clock time")
            label11 = tk.Label(self.datatypes, text="DATETIMEOFFSET: Tracks point in time entries combined with explicit time zone offsets")
            label12 = tk.Label(self.datatypes, text="BOOLEAN / BIT: Strict logical storage holding a true or false state")
            label13 = tk.Label(self.datatypes, text="JSON: Semi-structured text column that natively validates JavaScript Object Notation syntax")
            label13 = tk.Label(self.datatypes, text="VARBINARY(MAX) / BLOB: Stores raw unformatted binary byte streams")

            button1 = tk.Button(self.datatypes, text="Return", width=20,height=5,anchor="center", command=self.row_creation)

            self.viewedData=True

            label1.grid(row=0, column=0, columnspan=3, sticky="n", pady=10)
            label2.grid(row=1, column=0, columnspan=3, sticky="n", pady=10)
            label3.grid(row=2, column=0, columnspan=3, sticky="n", pady=10)
            label4.grid(row=3, column=0, columnspan=3, sticky="n", pady=10)
            label5.grid(row=4, column=0, columnspan=3, sticky="n", pady=10)
            label6.grid(row=5, column=0, columnspan=3, sticky="n", pady=10)
            label7.grid(row=6, column=0, columnspan=3, sticky="n", pady=10)
            label8.grid(row=7, column=0, columnspan=3, sticky="n", pady=10)
            label9.grid(row=8, column=0, columnspan=3, sticky="n", pady=10)
            label10.grid(row=9, column=0, columnspan=3, sticky="n", pady=10)
            label11.grid(row=10, column=0, columnspan=3, sticky="n", pady=10)
            label12.grid(row=11, column=0, columnspan=3, sticky="n", pady=10)
            label13.grid(row=12, column=0, columnspan=3, sticky="n", pady=10)

            button1.grid(row=14, column=0, columnspan=3, sticky="n", pady=10)

            self.datatypes.pack()
            
            
    def add_entry(self):
        #Enter table name and row name then when you press the button it will take you to a page to input a value which will tell you the datatype of the row
        self.main_menu.pack_forget()
        self.add_entries = tk.Frame(self.window)

        label1 = tk.Label(self.add_entries, text="Enter the title of the table you want to add an entry to")
        entry1 = tk.Entry(self.add_entries, width=20)
        label2 = tk.Label(self.add_entries, text="Enter the row you want to insert into")
        entry2 = tk.Entry(self.add_entries, width=20)
        button1 = tk.Button(self.add_entries, text="Enter", width=20,height=5,anchor="center")
        

        label1.grid(row=0,column=0,columnspan=3,sticky="n",pady=10)
        entry1.grid(row=1,column=0,columnspan=3,sticky="n",pady=10)
        label2.grid(row=2,column=0,columnspan=3,sticky="n",pady=10)
        entry2.grid(row=3,column=0,columnspan=3,sticky="n",pady=10)
        button1.grid(row=4,column=0,columnspan=3,sticky="n",pady=10)

        self.add_entries.pack()

    def insert_value(self):
        query = "select type from pragma"


    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Database Manager 9000")
        self.window.geometry("1000x675")

        #MAIN MENU

        self.main_menu = tk.Frame(self.window)

        label1 = tk.Label(self.main_menu, text="Main Menu", font=("Arial", 16))

        button1 = tk.Button(self.main_menu, text="Create Tables", width=20, height=5, anchor="center", command=self.create_table)
        button2 = tk.Button(self.main_menu, text="Add Entries", width=20, height=5, anchor="center", command=self.add_entry)
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