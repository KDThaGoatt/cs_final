import tkinter as tk
from tkinter import *
from tkinter import ttk
from functions import myDB

class gui:
    def create_table(self):
        #gui maker for the create table function, lets you input table name, column amount, and true or false ID autoincrement
        self.main_menu.pack_forget()

        self.table_create = tk.Frame(self.window)

        label1 = tk.Label(self.table_create, text="Enter the name for your table")
        self.name_entry = tk.Entry(self.table_create, width=20)
        label2 = tk.Label(self.table_create, text="How many columns are in your table? (Integer)")
        self.column_entry = tk.Entry(self.table_create, width=20)
        label3 = tk.Label(self.table_create, text="ID autoincrement? (type True or False)")
        self.id_entry = tk.Entry(self.table_create, width=20)

        button1 = tk.Button(self.table_create, text="Continue", width=20,height=5,anchor="center", command=self.get_values)

        label1.grid(row=0, column=0, columnspan=3, sticky="n", pady=10)
        self.name_entry.grid(row=1,column=0,columnspan=3,sticky="n",pady=10)
        label2.grid(row=2, column=0, columnspan=3, sticky="n", pady=10)
        self.column_entry.grid(row=3,column=0,columnspan=3,sticky="n",pady=10)
        label3.grid(row=4, column=0, columnspan=3, sticky="n", pady=10)
        self.id_entry.grid(row=5,column=0,columnspan=3,sticky="n",pady=10)
        button1.grid(row=6,column=0,columnspan=3,sticky="n",pady=10)


        self.table_create.pack()


    def get_values(self):
        #special get function for table creation to make sure they are the correct datatypes
        self.viewedData = False
        self.table_name = self.name_entry.get()
        try:
            self.column_amount = int(self.column_entry.get())
        except:
            print("Non integer inputted")
        try:
            self.id_bool = bool(self.id_entry.get())
        except:
            print("Non Bool value inputted")
        self.column_creation()
        

    def column_creation(self):
        #looped gui function that uses tk.IntVar to iterate the loops when you press the button
        #This function creates a list in the format [value,datatype,value,datatype,...]
        self.col_list = []
        self.table_create.pack_forget()
        if self.viewedData == True:
            self.datatypes.pack_forget()
            self.viewedData = False
        self.last_col = False

        self.wait_var = tk.IntVar()
        for i in range(self.column_amount):
            if i != 0:
                self.column_create.pack_forget()
            self.column_create = tk.Frame(self.window)

            label1 = tk.Label(self.column_create, text="Enter the title and datatype of your column")
            label2 = tk.Label(self.column_create, text=f"Column {i+1}")
            label3 = tk.Label(self.column_create, text="Enter the name of your column")
            label4 = tk.Label(self.column_create, text="Enter the datatype of your column")


            self.colentry = tk.Entry(self.column_create, width=20)
            self.column_datatype_entry = tk.Entry(self.column_create, width=20)

            button1 = tk.Button(self.column_create, text="View Datatypes", width=20,height=5,anchor="center", command=self.datatype_screen)

            button2 = tk.Button(self.column_create, text="Enter", width=20,height=5,anchor="center", command=self.column_list_build)
            
            if i == (self.column_amount-1):
                self.last_col = True

            label1.grid(row=0, column=0, columnspan=3, sticky="n", pady=10)
            label2.grid(row=2, column=0, columnspan=3, sticky="n", pady=10)
            label3.grid(row=3, column=0, columnspan=3, sticky="n", pady=10)
            label4.grid(row=5, column=0, columnspan=3, sticky="n", pady=10)

            self.colentry.grid(row=4,column=0,columnspan=3,sticky="n",pady=10)
            self.column_datatype_entry.grid(row=6,column=0,columnspan=3,sticky="n",pady=10)

            button1.grid(row=1, column=0, columnspan=3, sticky="n", pady=10)
            button2.grid(row=7,column=0,columnspan=3,sticky="n",pady=10)

            self.column_create.pack()

            button1.wait_variable(self.wait_var)

    def column_list_build(self):
        #appends the values to create the list
        column_name = self.colentry.get()
        column_datatype = self.column_datatype_entry.get()
        self.col_list.append(column_name)
        self.col_list.append(column_datatype)
        if self.last_col == True:
            self.db_create.create_table(self.table_name,self.col_list,self.id_bool)
            if self.id_bool == True:
                print(f"You have created a table with the name {self.table_name}, {self.column_amount} columns and ID autoincrement")
            if self.id_bool == False:
                print(f"You have created a table with the name {self.table_name}, {self.column_amount} columns and no ID autoincrement")

            self.column_create.pack_forget()
            self.main_menu.pack()
        else:
            self.wait_var.set(1)


    
    def datatype_screen(self):
            #A screen available in the table creation process that shows you all the different datatypes and when to use them
            self.column_create.pack_forget()

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

            button1 = tk.Button(self.datatypes, text="Return", width=20,height=5,anchor="center", command=self.column_creation)

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
        #Enter table name and column name then when you press the button it will take you to a page to input a value which will tell you the datatype of the column
        self.main_menu.pack_forget()
        self.add_entries = tk.Frame(self.window)

        label1 = tk.Label(self.add_entries, text="Enter the title of the table you want to add an entry to")
        self.table_name_entry = tk.Entry(self.add_entries, width=20)
        label2 = tk.Label(self.add_entries, text="Enter the column you want to insert into")
        self.column_name_entry = tk.Entry(self.add_entries, width=20)
        button1 = tk.Button(self.add_entries, text="Enter", width=20,height=5,anchor="center",command=self.get_table_and_col_name)

        label1.grid(row=0,column=0,columnspan=3,sticky="n",pady=10)
        self.table_name_entry.grid(row=1,column=0,columnspan=3,sticky="n",pady=10)
        label2.grid(row=2,column=0,columnspan=3,sticky="n",pady=10)
        self.column_name_entry.grid(row=3,column=0,columnspan=3,sticky="n",pady=10)
        button1.grid(row=4,column=0,columnspan=3,sticky="n",pady=10)

        self.add_entries.pack()

    def get_table_and_col_name(self):
        self.table_name = self.table_name_entry.get()
        self.column_name = self.column_name_entry.get()
        self.add_entries.pack_forget()
        self.insert_value()

    def insert_value(self):
        #Page where you insert the value for the column you chose
        #this page also tells you what datatype the column is so you dont input the wrong one by accident
        datatype = self.db_create.datatype_get(self.table_name,self.column_name)

        self.value_insert = tk.Frame(self.window)

        label1 = tk.Label(self.value_insert, text=f"The datatype is for column {self.column_name} is: {datatype}")
        label2 = tk.Label(self.value_insert, text="Enter your value")
        self.value_entry = tk.Entry(self.value_insert, width=20)
        button1 = tk.Button(self.value_insert, text="Enter", width=20,height=5,anchor="center",command=self.entry_adder)

        label1.grid(row=0,column=0,columnspan=3,sticky="n",pady=10)
        label2.grid(row=1,column=0,columnspan=3,sticky="n",pady=10)
        self.value_entry.grid(row=2,column=0,columnspan=3,sticky="n",pady=10)
        button1.grid(row=3,column=0,columnspan=3,sticky="n",pady=10)

        self.value_insert.pack()

    def entry_adder(self):
        #function to actually add the entries 
        value = self.value_entry.get()
        self.db_create.add_entries(self.table_name,self.column_name,value)
        print(f"In the table {self.table_name}, you have added a row in the column {self.column_name} with the value {value}")
        self.value_insert.pack_forget()
        self.main_menu.pack()

    def entry_edit(self):
        #gui function for editing entries
        self.main_menu.pack_forget()
        self.edit_main = tk.Frame(self.window)

        label1 = tk.Label(self.edit_main,text="Enter the table you want to edit from")
        self.table_name_entry = tk.Entry(self.edit_main,width=20)
        label2 = tk.Label(self.edit_main,text="Enter the column you want to edit from")
        self.column_name_entry = tk.Entry(self.edit_main,width=20)
        label3 = tk.Label(self.edit_main,text="Enter what identifier you will use (could be the value or id)")
        self.identifier_entry = tk.Entry(self.edit_main,width=20)
        label4 = tk.Label(self.edit_main,text="Enter what value the identifier should have to be edited")
        self.id_value_entry = tk.Entry(self.edit_main,width=20)
        label5 = tk.Label(self.edit_main,text="Enter the value you want to change to")
        self.value_entry = tk.Entry(self.edit_main,width=20)
        button1 = tk.Button(self.edit_main, text="Enter", width=20,height=5,anchor="center",command=self.edit_adder)

        label1.grid(row=0,column=0,columnspan=3,sticky="n", pady=10)
        self.table_name_entry.grid(row=1,column=0,columnspan=3,sticky="n", pady=10)
        label2.grid(row=2,column=0,columnspan=3,sticky="n", pady=10)
        self.column_name_entry.grid(row=3,column=0,columnspan=3,sticky="n", pady=10)
        label3.grid(row=4,column=0,columnspan=3,sticky="n", pady=10)
        self.identifier_entry.grid(row=5,column=0,columnspan=3,sticky="n", pady=10)
        label4.grid(row=6,column=0,columnspan=3,sticky="n", pady=10)
        self.id_value_entry.grid(row=7,column=0,columnspan=3,sticky="n", pady=10)
        label5.grid(row=8,column=0,columnspan=3,sticky="n", pady=10)
        self.value_entry.grid(row=9,column=0,columnspan=3,sticky="n", pady=10)
        button1.grid(row=10,column=0,columnspan=3,sticky="n", pady=10)

        self.edit_main.pack()

    def edit_adder(self):
        #actually adds the entries to the database
        table_name = self.table_name_entry.get()
        column_name = self.column_name_entry.get()
        identifier = self.identifier_entry.get()
        id_value = self.id_value_entry.get()
        value = self.value_entry.get()
        self.db_create.edit_entries(table_name,column_name,value,identifier,id_value)
        print(f"You have edited the value for the column {column_name} in the table {table_name} to {value} when {identifier} is {id_value}")
        self.edit_main.pack_forget()
        self.main_menu.pack()

    def search_entries(self):
        #gui function for searching for entries
        self.main_menu.pack_forget()
        self.search_main = tk.Frame(self.window)

        label1 = tk.Label(self.search_main,text="Enter the table to search in")
        self.table_name_entry = tk.Entry(self.search_main,width=20)
        label2 = tk.Label(self.search_main,text="Enter the column to search in")
        self.column_name_entry = tk.Entry(self.search_main,width=20)
        label3 = tk.Label(self.search_main,text="Enter the value to search for") 
        self.value_entry = tk.Entry(self.search_main,width=20)
        button1 = tk.Button(self.search_main, text="Enter", width=20,height=5,anchor="center",command=self.search)

        label1.grid(row=0,column=0,columnspan=3,sticky="n",pady=10)
        self.table_name_entry.grid(row=1,column=0,columnspan=3,sticky="n",pady=10)
        label2.grid(row=2,column=0,columnspan=3,sticky="n",pady=10)
        self.column_name_entry.grid(row=3,column=0,columnspan=3,sticky="n",pady=10)
        label3.grid(row=4,column=0,columnspan=3,sticky="n",pady=10)
        self.value_entry.grid(row=5,column=0,columnspan=3,sticky="n",pady=10)
        button1.grid(row=6,column=0,columnspan=3,sticky="n",pady=10)

        self.search_main.pack()

    def search(self):
        #function that actually searches for the entries and displays it on the screen
        table_name = self.table_name_entry.get()
        column_name = self.column_name_entry.get()
        value = self.value_entry.get()
        self.db_create.search_for_entries(table_name,column_name,value)
        self.search_main.pack_forget() 

        self.search_display = tk.Frame(self.window)
        


    def __init__(self):
        self.db_create = myDB()
        self.window = tk.Tk()
        self.window.title("Database Manager 9000")
        self.window.geometry("1000x675")

        #MAIN MENU

        self.main_menu = tk.Frame(self.window)

        label1 = tk.Label(self.main_menu, text="Main Menu", font=("Arial", 16))

        button1 = tk.Button(self.main_menu, text="Create Tables", width=20, height=5, anchor="center", command=self.create_table)
        button2 = tk.Button(self.main_menu, text="Add Entries", width=20, height=5, anchor="center", command=self.add_entry)
        button3 = tk.Button(self.main_menu, text="Edit Entries", width=20, height=5, anchor="center",command=self.entry_edit)
        button4 = tk.Button(self.main_menu, text="Search For Entries", width=20, height=5, anchor="center",command=self.search_entries)

        label1.grid(row=0,column=0,columnspan=3,sticky="n",pady=10)
        button1.grid(row=1, column=0, padx=10,pady=10)
        button2.grid(row=1,column=1,padx=10,pady=10)
        button3.grid(row=2,column=0,padx=10,pady=10)
        button4.grid(row=2,column=1,padx=10,pady=10)

        self.main_menu.pack()

        self.window.mainloop()

gui()