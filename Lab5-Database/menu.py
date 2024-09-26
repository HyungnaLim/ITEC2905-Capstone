"""
A menu - you need to add the database and fill in the functions.
"""

import sqlite3

db = 'record.sqlite'


def main():

    conn = sqlite3.connect(db)
    conn.execute(
        'CREATE TABLE IF NOT EXISTS record (record_id INTEGER PRIMARY KEY, name text, country text, number_of_catches int, UNIQUE( name COLLATE NOCASE, country COLLATE NOCASE))')

    # insert_sample_data()

    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


# Add sample data - every string is in uppercase so that the program is case-insensitive
def insert_sample_data():
    conn = sqlite3.connect(db)
    conn.execute('INSERT INTO record (name, country, number_of_catches) VALUES ("JANNE MUSTONEN", "FINLAND", 98)')
    conn.execute('INSERT INTO record (name, country, number_of_catches) VALUES ("IAN STEWART", "CANADA", 94)')
    conn.execute('INSERT INTO record (name, country, number_of_catches) VALUES ("AARON GREGG", "CANADA", 88)')
    conn.execute('INSERT INTO record (name, country, number_of_catches) VALUES ("CHAD TAYLOR", "USA", 78)')
    conn.commit()
    conn.close()


# Display all the record holders in the database
def display_all_records():
    conn = sqlite3.connect(db)
    all_records = conn.execute('SELECT * FROM record')
    for record in all_records:
        print(record)
    conn.close()


# Let the user search for a record holder by name
# It will display all records searched by name if there are multiple record under the same name
def search_by_name():
    conn = sqlite3.connect(db)
    try:
        name = input('Enter name to search record: ').strip().upper()
        res = conn.execute('SELECT * FROM record WHERE name = ?', (name,) )
        searched_record = res.fetchall()
        if searched_record is not None:
            print(searched_record)
        else:
            print('Record not found')
    except Exception as e:
        print('Error:', e)
    finally:
        conn.close()


# Let the user add a new record row for a record holder
def add_new_record():
    conn = sqlite3.connect(db)
    try:
        name = input('Enter name: ').strip().upper()
        country = input('Enter country: ').strip().upper()
        number_of_catches = int(input('Enter number of catches: '))
        conn.execute('INSERT INTO record (name, country, number_of_catches) VALUES (?, ?, ?)', (name, country, number_of_catches,) )
        conn.commit()
        print('Successfully added')
    except Exception as e:
        print('Error:', e)
    finally:
        conn.close()


# update the number of catches for a record holder - search and edit record by id
def edit_existing_record():
    conn = sqlite3.connect(db)
    try:
        record_id = int(input('Enter id: '))
        new_record = int(input('Enter new record: '))
        conn.execute('UPDATE record SET number_of_catches = ? WHERE record_id = ?', (new_record, record_id,) )
        conn.commit()
        print('Successfully updated')
    except Exception as e:
        print('Error:', e)
    finally:
        conn.close()


# Delete a record by record holder's name
# It will delete all records searched by the name if there are multiple record under the same name
# Note: deleting data by primary key (id) is much more desirable than this!
def delete_record():
    conn = sqlite3.connect(db)
    try:
        name = input('Enter name: ').strip().upper()
        res = conn.execute('DELETE FROM record WHERE name = ?', (name,) )
        if res.rowcount > 0:
            conn.commit()
            print('Successfully deleted')
        else:
            print('Record not found')
    except Exception as e:
        print('Error:', e)
    finally:
        conn.close()


if __name__ == '__main__':
    main()