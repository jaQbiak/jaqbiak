import os
import dotenv
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

dotenv.load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()