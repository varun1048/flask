from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='sqltie'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/posts')
def pages():
    posts_data =[
        {"songs":"valimama vali","singer":"sana","hero":"sanatham"},
        {"songs":"bigil bgm","hero":"atly"},
        {"songs":"master the blaster vali","singer":"aruvi","hero":"vijay"},        
        {"songs":"vaga na vanaga na","singer":"vijay","hero":"vijay"},        
        ]
    return render_template("post.html",datas=posts_data)

@app.route('/<string:name>/<int:id>')
def hello(name,id):
    return f"hello {name} your id :{id}"

@app.route("/home",methods=['POST'])
def geting():
    return "varun not comming"

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/singin",methods=['post'])
def singin(data):
    return f"singin page render {data}"

if __name__ == "__main__":
    app.run(debug=True)