from . import auth
import os

from flask import Flask, render_template
from . import db


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    # Blueprint
    app.register_blueprint(auth.bp)
    

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello,varun!'
    
    # @app.route('/')
    # def index():
    #     return render_template('base.html')
    
    # @app.route('/register')
    # def register():
    #     return render_template('auth/register.html')
    
    # @app.route('/login')
    # def login():
    #     return render_template('auth/login.html')

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app

