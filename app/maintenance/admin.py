from flask_restless import APIManager
from flask_admin import Admin
from flask_admin.contrib.geoa import ModelView

from app import app
from app.maintenance.models import session, Customers, Employees, Orders, Products, Privileges, PurchaseOrders


class CustomersModelView(ModelView):
	column_list  = ['first_name','last_name', 'job_title', 'email_address']
	can_view_details = True

class EmployeesModelView(ModelView):
	column_list  = ['first_name','last_name', 'job_title', 'email_address']
	can_view_details = True

class OrdersModelView(ModelView):
	column_list  = ['ship_name', 'order_date', 'ship_address', 'notes', 'employees.first_name']
	can_view_details = True

class ProductsModelView(ModelView):
	column_list  = ['product_code', 'product_name', 'quantity_per_unit', 'standard_cost']
	can_view_details = True

class PurchaseOrdersModelView(ModelView):
	column_list  = ['id', 'submitted_date', 'status_id', 'notes', 'approved_by']
	can_view_details = True


# Administration Site
admin = Admin(app, name='site_recommendations', template_mode='bootstrap3')
admin.add_view(CustomersModelView(Customers, session, 'Customers'))
admin.add_view(EmployeesModelView(Employees, session, 'Employees'))
admin.add_view(OrdersModelView(Orders, session, 'Orders'))
admin.add_view(ProductsModelView(Products, session, 'Products'))
admin.add_view(ModelView(Privileges, session, 'Privileges'))
admin.add_view(PurchaseOrdersModelView(PurchaseOrders, session, 'PurchaseOrders'))
