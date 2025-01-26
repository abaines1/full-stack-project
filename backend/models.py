from config import Db

# Create a python class for Contact
# This represents a database model as a Python class
# This is where we define the fields of the database table

class Contact(Db.Model):

    # Create Fields Required for a Contact (FirstName, LastName, Email, Phone)
    # These fields represent columns in the database table
    # String fields must set a character limit
    # Unique constraint on fields ensures no duplicate entries
    # Nullable constraint on fields ensures the field is not empty

    # Contact ID Field (Primary Key) as an Integer
    id = Db.Column(Db.Integer, primary_key=True)

    # First Name Field as a String (20 characters)
    first_name = Db.Column(Db.String(20), unique=False, nullable=False)

    # Last Name Field as a String (20 characters)
    last_name = Db.Column(Db.String(20), unique=False, nullable=False)

    # Email Field as a String (50 characters)
    # Unqiue constraint to ensure no duplicate emails are created
    email = Db.Column(Db.String(50), unique=True, nullable=False)

    # Next define a function to_json()
    # Function converts the Contact object to a Python Dictionary and then returns it
    def to_json(self):
        return {

            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email

        }
