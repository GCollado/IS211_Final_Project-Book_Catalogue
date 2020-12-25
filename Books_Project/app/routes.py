from flask import flash, redirect, render_template,  request,  url_for
from app import app, db
from app.forms import RegistrationForm, UserLoginForm
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User
from werkzeug.urls import url_parse


# Maps and routes view function to '/' and 'index' urls
@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title="Home Page", books=books)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = UserLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("""Invalid username or password. Please try again.""")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404
    books = {1: dict(book_title='Lord of the flies', author='William Golding',
                     page_total='224', isbn10='n/a', isbn13='9780399501487'),
             2: dict(book_title='The Complete Short Stories of Mark Twain',
                     author='Mark Twain', page_total='744', isbn10='n/a',
                     isbn13='9780307959379')}
    return render_template('user.html', user=user, books=books)


@app.route('/user/<username>/add_book')
@login_required
def add_book(username):
    user = User.query.filter_by(username).first_or_404()
    return render_template('add_book.html')


@app.route('/user/<username>/delete_book')
@login_required
def delete_book(username):
    user = User.query.filter_by(username).first_or_404()
    return render_template('delete_book.html')


@app.route('/user/<username>/clear_books')
@login_required
def clear_books(username):
    user = User.query.filter_by(username).first_or_404()
    return render_template('clear_books.html')


@app.route('/logout')
def user_logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations! You are now registered.')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
