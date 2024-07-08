import sqlite3

# Kapcsolódás az adatbázishoz (ha nem létezik, akkor létrehozza)
conn = sqlite3.connect('books.db')

# Cursor létrehozása
c = conn.cursor()

# Tábla létrehozása
c.execute('''
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

# Néhány könyv hozzáadása
books = [("book1",), ("book2",), ("book3",)]
c.executemany('INSERT INTO books (name) VALUES (?)', books)

# Változtatások mentése és kapcsolat bezárása
conn.commit()
conn.close()

print("Database created and initialized with sample data.")
