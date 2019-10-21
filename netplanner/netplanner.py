# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
from flask_bootstrap import Bootstrap
from datetime import datetime

app = Flask(__name__)  # create the application instance :)
Bootstrap(app)
app.config.from_object(__name__)  # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'netplanner.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='password'
))
app.config.from_envvar('NETPLANNER_SETTINGS', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')


@app.route('/')
def index():
    db = get_db()
    cur = db.execute('SELECT * FROM events')
    dbevents = cur.fetchall()
    allevents = []
    for idx, ev in enumerate(dbevents, start=0):
        newentry = {'title': ev['title'], 'start_time': datetime.strptime(ev['start_time'], '%Y-%m-%d %H:%M:%S').date(),
                    'end_time': datetime.strptime(ev['start_time'], '%Y-%m-%d %H:%M:%S').date()}
        allevents.insert(idx, newentry)
    today = datetime.today().strftime('%Y-%m-%d')
    return render_template('index.html', allevents=allevents, today=today)


@app.route('/users')
def users():
    db = get_db()
    cur = db.execute('select username from users order by id desc')
    users = cur.fetchall()
    return render_template('users.html', users=users)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'invalid password'
        else:
            session['logged_in'] = True
            flash('Successfully logged in as Admin.')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Successfully logged out.')
    return redirect(url_for('index'))


@app.route('/add_event', methods=['GET', 'POST'])
def add_event():
    error = None
    if request.method == 'POST':
        db = get_db()
        db.execute('INSERT INTO events (title, description, start_time, end_time, color) VALUES (?, ?, ?, ?, ?)',
                   [request.form["event_name"],
                    request.form["event_description"],
                    request.form["start_time"],
                    request.form["end_time"],
                    request.form["color"]
                    ])
        db.commit()
        return redirect(url_for("index"))
    return render_template('add_event.html', error=error)


@app.route('/add_note')
def add_note():
    return render_template('add_note.html')


@app.route('/events')
def events():
    db = get_db()
    cur = db.execute('SELECT * FROM events')
    events = cur.fetchall()
    return render_template('events.html', events=events)


@app.route('/notes')
def notes():
    db = get_db()
    cur = db.execute('SELECT * FROM notes')
    notes = cur.fetchall()
    return render_template('notes.html', notes=notes)


if __name__ == '__main__':
    app.run(debug=True)
