#Flask API server

import auxiliary
from flask import Flask, render_template
from flask import jsonify
from flask import request
import json
import model
from model import User, Notification, Action, Signal, Raw_data
import flask
from flask_sqlalchemy import SQLAlchemy
import SQLAlchemy
from flask_admin import Admin

app = Flask(__name__, template_folder='')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
app.config['SECRET_KEY'] = 'postgres'

db = SQLAlchemy(app)
admin = Admin(app)
tools = auxiliary.ostools()
tools.db_connection()


ferramenta = auxiliary.ostools()
session = ferramenta.dbconnetion()
user_handler = auxiliary.user_handler()
data_handler= auxiliary.data_handler()
signal_handler = auxiliary.signal_handler()
notification_handler = auxiliary.notification_handler()
action_handler = auxiliary.action_handler()
invoice_handler = auxiliary.invoice_handler()

@app.teardown_request
def app_teardown(response_or_exc):
    session.remove()
    return response_or_exc

class MyModelView(ModelView):
    def __init__(self, model, session, name=None, category=None, endpoint=None,\
                 url=None, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
            super(MyModelView, self).__init__(model, session, name=name, category=category, endpoint=endpoint, url=url)

    def is_accessible(self):
        return True

@app.route('/')
def index():
    return "Index"

@app.route('/register/<string:email>/<string:password>/<string:username>')
def register():
    if request.method == 'GET':
        return True
    elif request.method == 'POST':
        newuser = user_handler.create_user(email, username, password)
        if newuser:
            return True
        else:
            return False

@app.route('/invoice_register/<string:invoice_name>/<float:amount>')
def invoice_register():
    if request.method == 'GET':
        return True
    elif request.method == 'POST':
        newinvoice = invoice_handler.create_invoice(amount, invoice_name)
        if newinvoice:
            return True
        else:
            return False

