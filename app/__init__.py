from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sys

# use utf-8
reload(sys)
sys.setdefaultencoding('utf8')

# App Instance
app = Flask(__name__)

# Configuration
# app.config.from_object('config')

# registre routes
from app.maintenance.routes import routes

# registre apis
from app.maintenance.admin import admin
