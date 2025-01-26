# import Flask, SQLAlchemy, and CORS
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initialize Flask App
App = Flask(__name__)
# Disable Cors
CORS(App)

# Database Configuration
# This line creates a new database file .db in the current directory
App.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

# Disable Tracking Across Database
App.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create Database Instance and Access CRUD Methods
Db = SQLAlchemy(App)