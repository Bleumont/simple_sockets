import sqlite3

def get_data_from_db(database):
    try:
        sqliteConnection = sqlite3.connect(database)
        cursor = sqliteConnection.cursor()

        sqlite_select_Query = "SELECT * FROM superAPI_products ORDER BY RANDOM() LIMIT 5;"
        cursor.execute(sqlite_select_Query)
        desc = cursor.description
        column_names = [col[0] for col in desc]
        
        data = [dict(zip(column_names, row))  
                for row in cursor.fetchall()]
        cursor.close()
        return data



    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

