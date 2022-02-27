from flask import Flask, render_template
from database import Database

app = Flask(__name__)

@app.route("/")
def hello():
    db = Database()
    connection = db.connect_to_database()
    cursor = connection.cursor()
    books = cursor.execute('SELECT * from books;')
    connection.commit() 
    cursor.close()
    connection.close()
    return render_template("index.html", books=books)

if __name__ == '__main__':
    app.run()