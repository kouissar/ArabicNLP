import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/v1/resources/emp/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('../db/employee.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_employees = cur.execute('SELECT * FROM emp;').fetchall()

    return jsonify(all_employees)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>Oh my! The resource could not be found.</p>", 404


@app.route('/api/v1/resources/emps', methods=['GET'])
def api_filter():
    query_parameters = request.args

    id = query_parameters.get('id')
    name = query_parameters.get('name')
    age = query_parameters.get('age')
    address = query_parameters.get('address')
    query = "SELECT * FROM emp WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if name:
        query += ' name=? AND'
        to_filter.append(name)
    if age:
        query += ' age=? AND'
        to_filter.append(age)
    if address:
        query += ' address=? AND'
        to_filter.append(address)
    if not (id or name or age or address):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('employee.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)


app.run()

# usage
# http://127.0.0.1:5000/api/v1/resources/emps?id=4
# http://127.0.0.1:5000/api/v1/resources/emps?address=123+st
# http://127.0.0.1:5000/api/v1/resources/emps?age=27
# http://127.0.0.1:5000/api/v1/resources/books/all
    # http://127.0.0.1:5000/api/v1/resources/books?author=Connie+Willis
# http://127.0.0.1:5000/api/v1/resources/books?author=Connie+Willis&published=1999
# http://127.0.0.1:5000/api/v1/resources/books?published=2010