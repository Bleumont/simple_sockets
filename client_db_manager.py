import sqlite3
import traceback
import sys
import datetime

def create_db_table():
    try:
        sqliteConnection = sqlite3.connect('market_saved_data.sqlite3')
        sqlite_create_table_query = f'''CREATE TABLE IF NOT EXISTS products (
                                    id INTEGER PRIMARY KEY,
                                    provider_name TEXT NOT NULL,
                                    product_name TEXT NOT NULL,
                                    product_category TEXT NOT NULL,
                                    buying_price REAL NOT NULL,
                                    selling_price REAL NOT NULL,
                                    bulk_price REAL NOT NULL,
                                    price_date TEXT NOT NULL);'''

        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("SQLite table created")

        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)

def insert_values(id, buying_price, selling_price, product_category, product_name, bulk_price, provider_name):
    try:
        sqliteConnection = sqlite3.connect('market_saved_data.sqlite3')
        cursor = sqliteConnection.cursor()
        price_date = datetime.datetime.now()

        cursor.execute(f"""INSERT INTO products (provider_name, product_name, product_category, buying_price, selling_price, bulk_price, price_date)
                          VALUES ('{provider_name}', '{product_name}', '{product_category}', {buying_price}, {selling_price}, {bulk_price}, '{price_date}' );""")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table")
        print("Exception class is: ", error.__class__)
        print("Exception is", error.args)
        print('Printing detailed SQLite exception traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
