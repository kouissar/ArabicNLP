from _curses import flash

import requests
from flask import Flask, Response, redirect, url_for, session, abort, render_template, request
from flask_login import LoginManager, UserMixin,  login_required, login_user, logout_user, current_user
import sqlite3 as sql
# from helper import ArabicHelp
from arabic_nlp import Arabic_helper
import random
import os


app = Flask(__name__)



@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin@google.com':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

#
# @app.route('/')
# @login_required
# def home():
#     return render_template('home.html', name=current_user.name)

@app.route('/login')
def login():
    return render_template('login.html')



@app.route('/enternew')
def new_search():
    return render_template('search_verse_form.html')

@app.route('/tokenize')
def new_token():
    return render_template('tokenize_text_form.html')

@app.route('/addtok', methods=['POST', 'GET'])
def addtok():
    if request.method == 'POST':
        tok_txt = request.form['txt']
        h = Arabic_helper()
        result = h.tokenize(tok_txt)
        count= h.word_count(tok_txt)
        names= h.get_name(tok_txt)
        names_count= len(names)
        lcount=h.get_letter_count(tok_txt)
        # freq = h.freq_dist(tok_txt)
        return render_template("response_token.html", result=result, orig_txt=tok_txt, c=count, n=names, l=lcount, nc=names_count)



@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        sourah = request.form['sourah']
        verse = request.form['verse']
        # txt = request.form['txt']
        # pin = request.form['pin']

        h = Arabic_helper()
        full_verse = h.getVerse(sourah, verse)
        print("values are ", save, sourah, verse, full_verse)

        return render_template("result.html",  s=sourah, v=verse, fv=full_verse)

@app.route('/random')
# @login_required
def random_verse():
    aya = random.randint(1, 6237)
    h = Arabic_helper()
    ran=h.get_random_verse(aya)
    return render_template("random.html", r=ran)

@app.route('/save', methods=['POST', 'GET'])
def save():
    if request.method == 'POST':
        sourah= request.form['sourah']
        verse = request.form['verse']
        full_verse = request.form['full_verse']

        print('data is ', sourah, verse, full_verse)
        try:
            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO verses (sourah,verse,txt) VALUES(?, ?, ?)", (sourah, verse, full_verse))

                con.commit()
                msg = "Record successfully added"
        except sql.DatabaseError as err:
            con.rollback()
            msg = "error in insert operation " + err

        finally:
            return render_template("result.html", msg=msg)
            con.close()

@app.route('/delete')
def delete():
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()

            cur.execute("DELETE FROM verses")

            con.commit()
            msg = "Record successfully deleted"
    except sql.DatabaseError as err:
        con.rollback()
        msg = "error in insert operation " + err

    finally:
        return render_template("result.html", msg=msg)
        con.close()


@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from verses")

    rows = cur.fetchall();
    return render_template("list.html", rows=rows)




if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(port=5000, debug=True)