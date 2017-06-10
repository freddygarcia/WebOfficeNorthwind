from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
engine = create_engine("mysql://root:toor@127.0.0.1/northwind")

# reflect the tables
Base.prepare(engine, reflect=True)

# Session object
session = Session(engine)

# Models reflect
Privileges = Base.classes.privileges
Customers = Base.classes.customers
Suppliers = Base.classes.suppliers
Employees = Base.classes.employees
Products = Base.classes.products
Shippers = Base.classes.shippers
Invoices = Base.classes.invoices
Strings = Base.classes.strings
Orders = Base.classes.orders

InventoryTransactionTypes = Base.classes.inventory_transaction_types
InventoryTransactions = Base.classes.inventory_transactions
PurchaseOrderDetails = Base.classes.purchase_order_details
PurchaseOrderStatus = Base.classes.purchase_order_status
OrderDetailsStatus = Base.classes.order_details_status
OrdersTaxStatus = Base.classes.orders_tax_status
PurchaseOrders = Base.classes.purchase_orders
OrderDetails = Base.classes.order_details
OrdersStatus = Base.classes.orders_status
SalesReports = Base.classes.sales_reports

# define to string method
PurchaseOrders.__str__ = lambda x: 'supplier: {:d} Notes: {:s}'.format(x.supplier_id, x.notes)
InventoryTransactions.__str__ = lambda x: 'Transaction Type: {:d} Product id: {:d} Quantity: {:d}'.format(x.transaction_type, x.product_id, x.quantity)
Employees.__str__ = lambda x: x.first_name + ' ' + x.last_name
Customers.__str__ = lambda x: x.first_name + ' ' + x.last_name
Invoices.__str__ = lambda x: 'Invoice id: ' + str(x.id)
OrdersTaxStatus.__str__ = lambda x: x.tax_status_name
Privileges.__str__ = lambda x: x.privilege_name
OrdersStatus.__str__ = lambda x: x.status_name
Products.__str__ = lambda x: x.product_name
Shippers.__str__ = lambda x: x.company
Orders.__str__ = lambda x: x.ship_name












