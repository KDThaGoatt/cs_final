import sqlite3

class myDB:

    def create_table(self, name, rows, id_auto):
        # takes a list in the format [rowname, valuetype, rowname, valuetype, ...]
        # and converts it into a string in the form (rowname valuetype, rowname valuetype, ...)
        query_build = ''
        for i in range(0, len(rows), 2):
            if i == 0:
                first_part = f'{rows[i]} {rows[i+1]}'
            else:
                query_build += f', {rows[i]} {rows[i+1]}'

        if id_auto == True:    
            query = f'create table if not exists {name} (id integer primary key autoincrement, {first_part}{query_build})'
        else:
            query = f'create table if not exists {name} ({first_part}{query_build})'
        self.cursor.execute(query)
    
    def add_entries(self, name, rows, values):
        query = f'insert into {name} ({rows}) values ({values})'
        self.cursor.execute(query)

    def __init__(self):
        file = 'dbase.db'
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()




