from flask import Flask, g, session, redirect, render_template, request, jsonify, Response
from markupsafe import escape
from Misc.functions import *
import database_init  # Use our uniquely named file to avoid conflicts

app = Flask(__name__)
app.secret_key = '#$ab9&^BB00_.'

# Initialize the DAO inside our new file
database_init.init_db(app)

# Inject custom functions into Jinja templates
app.jinja_env.globals.update(
    ago=ago,
    str=str,
)

# Registering blueprints AFTER database is initialized to prevent loops
from routes.user import user_view
from routes.book import book_view
from routes.admin import admin_view

app.register_blueprint(user_view)
app.register_blueprint(book_view)
app.register_blueprint(admin_view)

if __name__ == "__main__":
    app.run(debug=True)