from flask import request, jsonify
from config import App, Db
from models import Contact

# What is JSONIFY?
# JSONIFY is a function in Flask that converts a Python dictionary into a JSON object

# We need to run our main Flask application
# This is the main entry point for our application

if __name__ == "__main__":
    # Database Instansiation
    # Once application starts we need to get the context of the application
    # Create all models in the database
    # This only works if they have not been created yet

    with App.app_context():
        Db.create_all()

    App.run(debug=True)

# Create a new route for the application
# This route will be used to create a new Contact
# POST Request
@App.route("/create_contact", methods=["POST"])
def create_contact():

    # We first need to get the data associated with the 
    data = request.get_json()
    first_name = data.get("firstName")
    last_name = data.get("lastName")
    email = data.get("email")

    # All must be filled in or return an error
    if not first_name or not last_name or not email:
        return jsonify({"message": "Please provide a first name, last name, and email"}), 400
    
    # Pass Values to Contact Model
    # Create a new Contact object
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)

    try:
        # Add the new Contact to the Database
        Db.session.add(new_contact)
        Db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
    return jsonify({"message": "Contact has been created" }), 200

# Create a new route for the application
# This route will be used to view existing Contacts
# GET Request
@App.route("/contacts", methods=["GET"])
def get_contacts():
    
    # Get all Contacts from database
    contacts = Contact.query.all()

    # Remember these are python objects that need to be converted to JSON objects before returning them
    # We can use the to_json() function we created in the Contact model
    # Map function: Apply a function to all the elements in a list

    # Lambda function: small anonymous function (no name) with infinite arguments but only one expression
    # lambda [arguments]: [expression]
    # combine with map function to apply to each item in a lsist

    # Example:
    # Normal function
    # def add(x,y):
        # return x + y
    # Lambda equivalent
    # add = lambda x,y: x+y
    

    json_contacts = list(map(lambda x: x.to_json(), contacts))
    
    return jsonify({"contacts": json_contacts})


# Create a new route for the application
# This route will be used to Update a Contact
# PATCH Request
@App.route("/update_contacts<int:user_id>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "Contact not found"}), 404

    data = request.get_json()
    if "firstName" in data:
        contact.first_name = data.get("firstName")
    if "lastName" in data:    
        contact.last_name = data.get("lastName")
    if "email" in data:    
        contact.email = data.get("email")

    Db.session.commit()

    return jsonify({"message": "Contact has been updated!!!"}), 200


# Create a new route for the application
# This route will be used to delete a Contact
# DELETE Request
@App.route("/delete_contact<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "Contact not found"}), 404
    
    Db.session.delete(contact)
    Db.session.commit()

    return jsonify({"message": "Contact has been deleted!!!"}), 200

# Default root
@App.route('/', methods=['GET'])
def home():
    return "Hello! Welcome to the Full-Stack Contact Web Application!!!"