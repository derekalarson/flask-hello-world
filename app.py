from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Derek Larson in 3308'


@app.route('/db_test')
def db_test():
    conn = psycopg2.connect("postgresql://posgresql_db_user:QkA9EaSLNTJSxTdJWDLKYgqDKvOs26Eu@dpg-cqijvrogph6c738qt9sg-a.oregon-postgres.render.com/posgresql_db")
    conn.close()
    return "Database Connection Successful"