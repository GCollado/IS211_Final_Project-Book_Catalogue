import _sqlite3


connection = _sqlite3.connect("memmory:")

cursor = connection.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS books(book_id INT PRIMARY KEY,
 book_title TEXT, page_count TEXT, average_rating TEXT""")

cursor.execute("""CREATE TABLE IF NOT EXISTS authors(author_id INT PRIMARY KEY,
 author_name TEXT""")

user_input = []
user_input = input("Please enter book tittle, number of pages, and the average rating: " )

cursor.execute("""INSERT OR IGNORE INTO books(book_title, page_count, average_rating)
VALUES (?,?,?)""",user_input)

cursor.execute("""INSERT OR IGNORE INTO books(book_title, page_count, average_rating)
VALUES (?,?,?)""",user_input)

cursor.execute("INSERT OR IGNOR INTO authors(author_name) VALUES (?)""", user_input)

cursor.commit()

connection.close()
def main():
    pass
