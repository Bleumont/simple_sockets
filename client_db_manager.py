import sqlite3
import traceback
import sys

def create_db_table():
    try:
        sqliteConnection = sqlite3.connect('market_saved_data.db')
        sqlite_create_table_query = f'''CREATE TABLE Products (
                                    id INTEGER PRIMARY KEY,
                                    provider_name TEXT NOT NULL UNIQUE,
                                    product_name TEXT NOT NULL,
                                    product_category TEXT NOT NULL,
                                    buying_price REAL NOT NULL,
                                    selling_price REAL NOT NULL,
                                    bulk_price REAL NOT NULL,
                                    price_date datetime);'''

        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        print("SQLite table created")

        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    # finally:
    #     if sqliteConnection:
    #         sqliteConnection.close()
    #         print("sqlite connection is closed")



def insert_values(b_price, s_price, blk_price, category, name, provider_id, date):
    try:
        sqliteConnection = sqlite3.connect('market_saved_data.db')
        cursor = sqliteConnection.cursor()
        print("Connected... OK")

        sqlite_insert_query = f"""INSERT INTO superAPI_products
                            (buying_price, selling_price, bulk_price, product_category, product_name, provider_id, price_date) 
                          VALUES ({b_price},{s_price},{blk_price},{category},{name},{provider_id},{date});"""

        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print("Record inserted... ", cursor.rowcount)
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
            print("Connection closed...")