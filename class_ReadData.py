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

# Reading Existing data
class ReadData():
    ID = db.child("User Data").get()
    print("Reading Existing Information...")
    print(ID.val())
