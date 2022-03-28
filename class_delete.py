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
class delete():
    remove_all = str(input("Do you wish to remove all user data? [Y]/[N]: "))
    # Removing all data from database
    if remove_all.lower() == "y":
        db.child("User Data").remove()
        print("All existing data have been deleted from the database")
    elif remove_all.lower() == "n":
        # Removing a segment of data from database
        id_status = input("Is the Unique ID known? [Y]/[N]: ")
        if id_status.lower() == "y":
            Unique_ID = {
                'Unique ID': str(input("Enter unique ID name/number: "))
            }
            delete_parameter = str(input("Do you want to delete an entire user detail using its ID? [Y]/[N]: "))
            if delete_parameter.lower() == "y":
                # Deleting an entire user detail from the database using its own unique ID
                db.child("User Data").child(Unique_ID).remove()
            elif delete_parameter.lower() == "n":
                specific_delete_parameter = str(input(
                    "Enter which parameter to remove. [F]irstname/ [L]astname/ [S]treet/ [St]ate/ [C]ity/ [Z]ip Code: "))
                if specific_delete_parameter.lower() == "f":
                    # Deleting the firstname of the user with specified ID
                    db.child("User Data").child(Unique_ID).child("Address").child("Name").child("Firstname").remove()
                elif specific_delete_parameter.lower() == "l":
                    # Deleting the lastname of the user with specified ID
                    db.child("User Data").child(Unique_ID).child("Address").child("Name").child("Lastname").remove()
                elif specific_delete_parameter.lower() == "s":
                    # Deleting the Street details of the user with specified ID
                    db.child("User Data").child(Unique_ID).child("Address").child("street").remove()
                elif specific_delete_parameter.lower() == "st":
                    # Deleting the state details of the user with specified ID
                    db.child("User Data").child(Unique_ID).child("Address").child("state").remove()
                elif specific_delete_parameter.lower() == "c":
                    # Deleting the city detail of the user with specified ID
                    db.child("User Data").child(Unique_ID).child("Address").child("city").remove()
                elif specific_delete_parameter.lower() == "z":
                    # Deleting the zip code of the user with specified ID
                    db.child("User Data").child(Unique_ID).child("Address").child("zip_code").remove()
                else:
                    print("Invalid Input")
            else:
                print("Invalid Input")
        elif id_status.lower() == "n":
            print("Printing existing data")
            ID = db.child("User Data").get()
            print("Existing Information: ")
            print(ID.val())
            Unique_ID = {
                'Unique ID': str(input("Enter unique ID name/number: "))
            }
            delete_parameter = str(input("Do you want to delete an entire user detail using its ID? [Y]/[N]: "))
            if delete_parameter.lower() == "y":
                # Deleting an entire user detail with specified unique ID
                db.child("User Data").child(Unique_ID).remove()
            elif delete_parameter.lower() == "n":
                specific_delete_parameter = str(input(
                    "Enter which parameter to remove. [F]irstname/ [L]astname/ [S]treet/ [St]ate/ [C]ity/ [Z]ip Code: "))
                if specific_delete_parameter.lower() == "f":
                    # Deleting the firstname of the user with specified ID
                    db.child("User Data").child(Unique_ID).child("Address").child("Name").child("Firstname").remove()
                elif specific_delete_parameter.lower() == "l":
                    # Deleting the lastname of the user with specified ID
                    db.child("User Data").child(Unique_ID).child("Address").child("Name").child("Lastname").remove()
                elif specific_delete_parameter.lower() == "s":
                    # Deleting the Street details of the user with specified ID
                    db.child("User Data").child(Unique_ID).child("Address").child("street").remove()
                elif specific_delete_parameter.lower() == "st":
                    # Deleting the state details of the user with specified ID
                    db.child("User Data").child(Unique_ID).child("Address").child("state").remove()
                elif specific_delete_parameter.lower() == "c":
                    # Deleting the city details of the user with specified ID
                    db.child("User Data").child(Unique_ID).child("Address").child("city").remove()
                elif specific_delete_parameter.lower() == "z":
                    # Deleting the zip code of the user with specified ID
                    db.child("User Data").child(Unique_ID).child("Address").child("zip_code").remove()
                else:
                    print("Invalid Input")
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
