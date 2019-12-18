from flask import Flask, flash, redirect, render_template, request, url_for, session

app = Flask(__name__)

books = [
    {1:{'title': 'of Mice and Men',
        'author': 'John Steinbeck',
        'page count': '112',
        'average rating': '4 out of 5 stars'
        },
     2:{'title': 'Dracula',
        'author': 'Bram Stoker',
        'page count': '48',
        'average rating': '5 out of 5 stars'
        },
    3:{'title': 'Drown',
       'author': 'Junot Diaz',
       'page count': '240',
       'average rating': '4 out of 5 stars'
       },
    4:{'title': 'I am Legend (and Other Stories)',
       'author': 'Richard Matheson',
       'page count': '320',
       'average rating': 'N/A'
       }
     }
]

users = [
    {1:{'username': 'admin', 'password': 'admin' },
     2:{'username': 'user1', 'password': 'password1'},
    }
]

@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            return render_template('dashboard.html', books = books, users=users)
        else:
            flash('Invalid username and/or password entered. Please try again.')
            return redirect(url_for('login'))

@app.route('/add_book')
def add_book():
    pass

@app.route('/remove_book')
def remove_book():
    pass

@app.route('/clear')
def clear_books():
    pass

@app.route('/logout')
def logout():
    pass

if __name__ == '__main__':
    app.run(debug=True)