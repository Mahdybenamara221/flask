from flask import Flask , render_template , url_for
from flask_mysqldb import MySQLdb
from datetime import datetime

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

db=MySQLdb(app)

class Todo(db.Model):
    id= db.Column(db.Integer , primary_key=True)
    content=db.Column(db.String(200),nullable=False)
    date_created = db.Column(db.DateTime,default=datetime.utcnow)
    def __repr__(self):
        return '<Task %r>' %self.id


@app.route('/')
def index():
    return render_template('index.html')

if __name__ =="__main__":
    app.run(debug=True)
