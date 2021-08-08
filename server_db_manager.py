import sqlite3

def get_data_from_db(database):
    try:
        sqliteConnection = sqlite3.connect(database)
        cursor = sqliteConnection.cursor()

        sqlite_select_Query = "SELECT * FROM superAPI_products ORDER BY RANDOM() LIMIT 5;"
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
        print(record)
        cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
