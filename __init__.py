from flask import Flask
from first_flask.views.user import user_page
from first_flask.extension import db

app = Flask('first_flask')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://tianji:tianji@127.0.0.1/python_admin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "lalskskskskksksjsj"

db.init_app(app)

app.register_blueprint(user_page)


