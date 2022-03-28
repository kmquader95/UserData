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
class update():
    continue_update = True
    while continue_update is True:
        id_status = input("Is the Unique ID known? [Y]/[N]: ")
        if id_status.lower() == "y":
            #Getting the ID of the user which requires an update of its parameter
            Unique_ID = {
                'Unique ID': str(input("Enter unique ID name/number: "))
            }
            update_parameter = str(input(
                "Enter the parameter you wish to update. [F]irstname/ [L]astname/ [S]treet/ [St]ate/ [C]ity/ [Z]ip Code: "))
            if update_parameter.lower() == "f":
                # Getting current firstname
                current_data = db.child("User Data").child(Unique_ID).child("Address").child("Name").child("Firstname").get()
                print("Existing firstname: " +current_data.val())
                updated_firstname = str(input("Enter updated firstname: "))
                db.child("User Data").child(Unique_ID).child("Address").child("Name").update(
                    {'Firstname': updated_firstname})
                print("Successfully updated")
            elif update_parameter.lower() == "l":
                # Getting current lastname
                current_data = db.child("User Data").child(Unique_ID).child("Address").child("Name").child(
                    "Lastname").get()
                print("Existing Lastname: " + current_data.val())
                updated_lastname = str(input("Enter updated lastname: "))
                db.child("User Data").child(Unique_ID).child("Address").child("Name").update(
                    {'Lastname': updated_lastname})
                print("Successfully updated")
            elif update_parameter.lower() == "s":
                # Getting current Street name/number
                current_data = db.child("User Data").child(Unique_ID).child("Address").child("street").get()
                print("Existing Street name/number: " + current_data.val())
                updated_street = str(input("Enter updated Street name/number: "))
                db.child("User Data").child(Unique_ID).child("Address").update({'street': updated_street})
                print("Successfully updated")
            elif update_parameter.lower() == "st":
                # Getting current state name
                current_data = db.child("User Data").child(Unique_ID).child("Address").child("state").get()
                print("Existing State name: " + current_data.val())
                updated_state = str(input("Enter updated state: "))
                db.child("User Data").child(Unique_ID).child("Address").update({'state': updated_state})
                print("Successfully updated")
            elif update_parameter.lower() == "c":
                # Getting current city name
                current_data = db.child("User Data").child(Unique_ID).child("Address").child("city").get()
                print("Existing City: " + current_data.val())
                updated_city = str(input("Enter updated city: "))
                db.child("User Data").child(Unique_ID).child("Address").update({'city': updated_city})
                print("Successfully updated")
            elif update_parameter.lower() == "z":
                # Getting current zip code
                number_check = True
                while number_check == True:
                    # Getting existing data from database
                    current_data = db.child("User Data").child(Unique_ID).child("Address").child("zip_code").get()
                    print("Existing ZIP code: " + current_data.val())
                    updated_zip = str(input("Enter updated ZIP code: "))
                    # Checking whether the input is a number or not
                    if updated_zip.isnumeric():
                        db.child("User Data").child(Unique_ID).child("Address").update({'zip_code': updated_zip})
                        print("Successfully updated")
                        number_check = False
                    else:
                        number_check = True
            else:
                print("Invalid Input")
        elif id_status.lower() == "n":
            ID = db.child("User Data").get()
            print("Existing Information: ")
            print(ID.val())
            Unique_ID = {
                'Unique ID': str(input("Enter unique ID name/number: "))
            }
            update_parameter = str(input(
                "Enter the parameter you wish to update. [F]irstname/ [L]astname/ [S]treet/ [St]ate/ [C]ity/ [Z]ip Code: "))
            if update_parameter.lower() == "f":
                # Getting current firstname
                current_data = db.child("User Data").child(Unique_ID).child("Address").child("Name").child(
                    "Firstname").get()
                print("Existing firstname: " + current_data.val())
                updated_firstname = str(input("Enter updated firstname: "))
                db.child("User Data").child(Unique_ID).child("Address").child("Name").update(
                    {'Firstname': updated_firstname})
                print("Successfully updated")
            elif update_parameter.lower() == "l":
                # Getting current lastname
                current_data = db.child("User Data").child(Unique_ID).child("Address").child("Name").child(
                    "Lastname").get()
                print("Existing Lastname: " + current_data.val())
                updated_lastname = str(input("Enter updated lastname: "))
                db.child("User Data").child(Unique_ID).child("Address").child("Name").update(
                    {'Lastname': updated_lastname})
                print("Successfully updated")
            elif update_parameter.lower() == "s":
                # Getting current street name
                current_data = db.child("User Data").child(Unique_ID).child("Address").child("street").get()
                print("Existing Street name/number: " + current_data.val())
                updated_street = str(input("Enter updated Street name/number: "))
                db.child("User Data").child(Unique_ID).child("Address").update({'street': updated_street})
                print("Successfully updated")
            elif update_parameter.lower() == "st":
                # Getting current state name
                current_data = db.child("User Data").child(Unique_ID).child("Address").child("state").get()
                print("Existing State name: " + current_data.val())
                updated_state = str(input("Enter updated state: "))
                db.child("User Data").child(Unique_ID).child("Address").update({'state': updated_state})
                print("Successfully updated")
            elif update_parameter.lower() == "c":
                # Getting current city name
                current_data = db.child("User Data").child(Unique_ID).child("Address").child("city").get()
                print("Existing City: " + current_data.val())
                updated_city = str(input("Enter updated city: "))
                db.child("User Data").child(Unique_ID).child("Address").update({'city': updated_city})
                print("Successfully updated")
            elif update_parameter.lower() == "z":
                # Getting current zip code
                number_check = True
                while number_check == True:
                    current_data = db.child("User Data").child(Unique_ID).child("Address").child("zip_code").get()
                    print("Existing ZIP code: " + current_data.val())
                    updated_zip = str(input("Enter updated ZIP code: "))
                    if updated_zip.isnumeric():
                        db.child("User Data").child(Unique_ID).child("Address").update({'zip_code': updated_zip})
                        print("Successfully updated")
                        number_check = False
                    else:
                        number_check = True

            else:
                print("Invalid Input")
        else:
            print("Invalid Input")
        # Checking to see if user wants to continue updating or exit the loop
        check_update_status = str(input("Do you want to continue update? [Y]/[N]: "))
        if check_update_status.lower() == "y":
            continue_update = True
        elif check_update_status.lower() == "n":
            continue_update = False
        else:
            print("Invalid Request")
            continue_update = False