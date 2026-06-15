import sqlite3

class myDB:

    def create_table(self, table, columns, id_auto):
        # takes a list in the format [rowname, valuetype, rowname, valuetype, ...]
        # and converts it into a string in the form (rowname valuetype, rowname valuetype, ...)
        query_build = ''
        first_part=''
        for i in range(0, len(columns), 2):
            if i == 0:
                first_part = f'{columns[i]} {columns[i+1]}'
            else:
                query_build += f', {columns[i]} {columns[i+1]}'

        if id_auto == True:    
            query = f'create table if not exists {table} (id integer primary key autoincrement, {first_part}{query_build});'
        else:
            query = f'create table if not exists {table} ({first_part}{query_build});'
        self.cursor.execute(query)
    
    def add_entries(self, table, column_name, value):
        query = f"insert into {table} ({column_name}) values ('{value}');"
        self.cursor.execute(query)
        self.connection.commit()

    def edit_entries(self, table, column, value, identifier, id_value):
        query = f"""
        UPDATE {table}
        SET {column} = {value}
        WHERE {identifier} = {id_value};
        """
        self.cursor.execute(query)
        self.connection.commit()

    def search_for_entries(self, table, column, value):
        try:
            value = str(value)
            query = f"select * from {table} where {column}='{value}';"
        except:
            query = f'select * from {table} where {column}={value};'
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def datatype_get(self,table,col_name):
        self.cursor.execute(f"PRAGMA table_info({table})")
        columns = self.cursor.fetchall()
        for col in columns:
            if col[1] == col_name:
                return col[2]


    def __init__(self):
        file = 'dbase.db'
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()




