from flask import Flask
from pages.routes import pages
from api.routes import api
import json
import os
from openai import OpenAI

app = Flask(__name__)

# Global objects
CONFIG_FILE = 'config.json'
with open(CONFIG_FILE, 'r') as config_file:
    config_file = json.load(config_file)

openai_agent = OpenAI(
    api_key=config_file["OPENAI_API_KEY"]
)
openai_model = config_file["GPT_MODEL"]

# Register blueprints
app.register_blueprint(pages)
app.register_blueprint(api)


if __name__ == '__main__':
    app.run(debug=True)