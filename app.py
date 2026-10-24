from flask import Flask, render_template

app = Flask(__name__)

books = [
    {"id": 1, "title": "Python Programming"},
    {"id": 2, "title": "DevOps Essentials"},
    {"id": 3, "title": "Cloud Computing"}
]

members = [
    {"id": 101, "name": "Rahul"},
    {"id": 102, "name": "Priya"},
    {"id": 103, "name": "Anjali"}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/books')
def books_page():
    return render_template('books.html', books=books)

@app.route('/members')
def members_page():
    return render_template('members.html', members=members)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
