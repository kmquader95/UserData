import pyrebase

#database details
firebaseConfig = {
    "apiKey": "AIzaSyBF3CZj20MihNZz0xIzqGOWdfOfYvfDsx0",
    "authDomain": "udpassignment.firebaseapp.com",
    "databaseURL": "https://udpassignment-default-rtdb.firebaseio.com",
    "projectId": "udpassignment",
    "storageBucket": "udpassignment.appspot.com",
    "messagingSenderId": "280299086634",
    "appId": "1:280299086634:web:4bff4dc5e64c31889cf453",
    "measurementId": "G-RSBK0STPEZ"
}
#Connecting app to the database
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

class CreateData():
    number_check = True
    while number_check is True:
        # Unique ID to store data of user
        Unique_ID = {
            'Unique ID': str(input("Enter unique ID name/number: "))
        }
        data_name = {
            'Firstname': input("Enter your first name: "),
            'Lastname': input("Enter your last name: ")
        }
        data_address = {
            'street': input("Enter Street name/number: "),
            'city': input("Enter the name of your city: "),
            'state': input("Enter your current state: "),
            'zip_code': input("Enter your address zip code: ")
        }
        if data_address['zip_code'].isnumeric() and Unique_ID['Unique ID'].isnumeric():
            db.child("User Data").child(Unique_ID).child("Address").set(data_address)
            db.child("User Data").child(Unique_ID).child("Address").child("Name").set(data_name)
            number_check = False
            print()
            print("Successfully stored in the database")
        else:
            print("ZIP code and Unique ID can only be numeric")
            number_check = True
