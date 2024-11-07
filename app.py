from flask import Flask
from pages.routes import pages
from api.routes import api

app = Flask(__name__)

   # Register blueprints
app.register_blueprint(pages)
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)