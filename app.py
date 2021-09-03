from flask import Flask, render_template ,request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100),nullable=False)
    contnet = db.Column(db.Text,nullable=False)
    author = db.Column(db.String(20),nullable=False,default="N/A")
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return "BlogPost" + str(self.id)


posts_data =[
    {"songs":"valimama vali","singer":"sana","hero":"sanatham"},
    {"songs":"bigil bgm","hero":"atly"},
    {"songs":"master the blaster vali","singer":"aruvi","hero":"vijay"},        
    {"songs":"vaga na vanaga na","singer":"vijay","hero":"vijay"},        
    ]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/posts',methods=['GET',"POST"])
def posts():
    if request.method == "POST":
        post_title = request.form['title']
        post_post = request.form['post']
        new_post = BlogPost(title=post_title,contnet=post_post,author="varun the grate")
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_data = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template("post.html",datas=all_data)

@app.route('/<string:name>/<int:id>')
def hello(name,id):
    return f"hello {name} your id :{id}"

@app.route("/home",methods=['POST'])
def geting():
    return "varun not comming"

# @app.route("/login")
# def login():
#     return render_template('login.html')

# @app.route("/singin",methods=['post'])
# def singin(data):
#     return f"singin page render {data}"

if __name__ == "__main__":
    app.run(debug=True)