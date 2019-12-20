import sqlite3

connection = sqlite3.connect(":memory:")

cursor = connection.cursor()


cursor.execute("""CREATE TABLE IF NOT EXISTS books(book_id INT PRIMARY KEY,
 book_title TEXT, page_count TEXT, average_rating TEXT)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS authors(author_id INTEGER PRIMARY KEY,
 author_name TEXT)""")

user_input = []
book = input("Please enter book tittle: ")
pages =   input("Please enter the number of pages: ")
avg_rating = input("Please enter the average rating: ")
responses = [book, pages, avg_rating]
user_input.append(responses)
print(user_input)

cursor.execute("""INSERT OR IGNORE INTO books(book_title, page_count, average_rating)
VALUES (?,?,?)""",(responses[0][0], responses[0][1], responses[0][2]))

cursor.execute("INSERT OR IGNORE INTO authors(author_name) VALUES (?)""", user_input)

connection.commit()

connection.close()

def main():
    pass
