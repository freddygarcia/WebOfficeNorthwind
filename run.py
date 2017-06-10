# # Run Server
from app import app
app.run(port=80, debug=True)

# mapped classes are now created with names by default
# matching that of the table name.
# User = Base.classes.user
