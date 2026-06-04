import sqlite3

class myDB:

    def create_table(self, table, rows, id_auto):
        # takes a list in the format [rowname, valuetype, rowname, valuetype, ...]
        # and converts it into a string in the form (rowname valuetype, rowname valuetype, ...)
        file = 'dbase.db'
        connection = sqlite3.connect(file)
        cursor = connection.cursor()
        query_build = ''
        first_part=''
        for i in range(0, len(rows), 2):
            if i == 0:
                first_part = f'{rows[i]} {rows[i+1]}'
            else:
                query_build += f', {rows[i]} {rows[i+1]}'

        if id_auto == True:    
            query = f'create table if not exists {table} (id integer primary key autoincrement, {first_part}{query_build});'
        else:
            query = f'create table if not exists {table} ({first_part}{query_build});'
        cursor.execute(query)
    
    def add_entries(self, table, rows, values):
        query = f'insert into {table} ({rows}) values ({values});'
        self.cursor.execute(query)

    def edit_entries(self, table, row, value, identifier, id_value):
        query = f"""
        UPDATE {table}
        SET {row} = {value}
        WHERE {identifier} = {id_value};
        """
        self.cursor.execute(query)

    def search_for_entries(self, table, row, value):
        query = f'select * from {table} where {row}={value};'
        self.cursor.execute(query)
        result = self.cursor.fetchall()


    def __init__(self):
        file = 'dbase.db'
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()




