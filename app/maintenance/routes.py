from flask import Blueprint, jsonify

from app import app
from app.maintenance.models import session, Employees, Customers

routes = Blueprint('routes', __name__, url_prefix='/')

@routes.route("works")
def works():
	employees = session.query(Employees).first()
	return employees.first_name
	# return "It works!"

app.register_blueprint(routes)

