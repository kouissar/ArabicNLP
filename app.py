import requests
from flask import Flask, render_template, request
import sqlite3 as sql
# from helper import ArabicHelp
from arabic_nlp import Arabic_helper

app = Flask(__name__)




@app.route('/')
def home():
    # h = ArabicHelp(4,6)
    # full_verse= h.getVerse()
    return render_template('home.html')


@app.route('/enternew')
def new_student():
    return render_template('search_verse_form.html')

@app.route('/tokenize')
def new_token():
    return render_template('tokenize_text_form.html')

@app.route('/addtok', methods=['POST', 'GET'])
def addtok():
    if request.method == 'POST':
        toc_txt = request.form['txt']
        h = Arabic_helper()
        result = h.tokenize(toc_txt)
        print(result)
        return render_template("response_token.html", result=result)

        #     full_verse = h.getVerse()
        #     print("values are ", sourah, verse, full_verse)
        #     with sql.connect("database.db") as con:
        #         cur = con.cursor()
        #
        #         cur.execute("INSERT INTO verses (sourah,verse,txt) VALUES(?, ?, ?)",(sourah,verse,full_verse) )
        #
        #         con.commit()
        #         msg = "Record successfully added"
        # except sql.DatabaseError as err:
        #     con.rollback()
        #     msg = "error in insert operation " + err
        #
        # finally:
        #     return render_template("result.html", msg=msg)
        #     con.close()



@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        sourah = request.form['sourah']
        verse = request.form['verse']
        save = request.form['bookmark_me']
        # txt = request.form['txt']
        # pin = request.form['pin']

        h = Arabic_helper()
        full_verse = h.getVerse(sourah, verse)
        print("values are ", sourah, verse, full_verse)
        if save:

            try:

                with sql.connect("database.db") as con:
                    cur = con.cursor()

                    cur.execute("INSERT INTO verses (sourah,verse,txt) VALUES(?, ?, ?)",(sourah,verse,full_verse) )

                    con.commit()
                    msg = "Record successfully added"
            except sql.DatabaseError as err:
                con.rollback()
                msg = "error in insert operation " + err

            finally:
                return render_template("result.html", msg=msg, fv=full_verse)
                con.close()
        else:
            return render_template("result.html",  fv=full_verse)


@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from verses")

    rows = cur.fetchall();
    return render_template("list.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)