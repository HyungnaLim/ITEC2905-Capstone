import sqlite3

conn = sqlite3.connect('first_db.sqlite')   # connect or create new if not exist

# conn.execute('CREATE TABLE products (id int, name text)')

# conn.execute('INSERT INTO products values (1000, "hat")')
# conn.execute('INSERT INTO products values (1001, "jacket")')

conn.commit()   # required

results = conn.execute('SELECT * FROM products')

# all_rows = results.fetchall()
# print(all_rows)

for row in results:
    print(row)  # each row is a tuple


results = conn.execute('SELECT * FROM products WHERE name like "jacket"')
first_row = results.fetchone()
print(first_row)


new_id = int(input('Enter new id: '))
new_name = input('Enter new product: ')

# conn.execute(f'INSERT INTO products VALUES ({new_id}, "{new_name}")')
conn.execute('INSERT INTO products VALUES (?, ?)', (new_id, new_name))
# format string would work, but it will very easily make program crash or have security problems.
# use parameterized query instead!

conn.commit()

update_product = 'wool hat'
update_id = 1000
conn.execute('UPDATE products SET name = ? WHERE id = ?', (update_product, update_id))
conn.commit()

delete_product = 'jacket'
conn.execute('DELETE FROM products WHERE name = ?', (delete_product, ))  # need to add comma in the end, because it is tuple.
conn.commit()

conn.close()

# can use sqlite shell on terminal to work with database by entering "sqlite3 filename"
# in this case, "sqlite3 first_db.sqlite"
# ".tables" shows a list of tables in the database / "select * from products;" will show all the rows