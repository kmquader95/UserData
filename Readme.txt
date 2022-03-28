Downloading/Installing PyCharm to run the Python code
>>> Go to https://www.jetbrains.com/pycharm/
>>> Click Download
>>> Select the suitable OS (Windows/IOS/Linux) and click 'download' under Community
>>> Once download is completed, run the .exe file and complete installation

Opeing python project files on PyCharm
>>> Click and open PyCharm
>>> Select Open and Navigate to the project folder
>>> Select the folder containing all the required .py files and press 'ok'
>>> This will open the entire project

Opening the necessary files
>>> Upon opening the project successfully, the column on right hand side will show all the files in the project folder
>>> Click and open the following files:
1. main.py
2. class_CreateData.py
3. class_delete.py
4. class_update.py
5. class_ReadData.py

Navigating to "Run" and "Terminal"
>>> At the bottom, you can find "Run", "Terminal", "Version Control" and so on.
>>> Alternatively, go to 'View' > 'Tool Windows' > 'Run'/'Terminal'

Importing/Downloading Modules (Pyrebase and Pylint) used in this project...
...Pyrebase is a simple python wrapper for the Firebase API...
...Firebase is used to store User data in the database.
>>> Open terminal
>>> To check pip version,
    Windows users, type in: pip --version
    Mac users, type in: pip3 --version
>>> Getting an output of the version will confirm that pip is downloaded in the pc
>>> To download the required module/library (pyrebase for firebase database and pylint for linting),
    Windows users, type in the terminal:
    - pip install pyrebase4
    - pip install pylint
    Mac users, type in the terminal:
    - pip3 install pyrebase4
    - pip3 install pylint

Opening/Accessing the Firebase Database
>>> Go to web browser and paste the following link: http://console.firebase.google.com/
>>> Use gmail account: sheikh.kamal@udplatforms.com to sign in (as the project on the database has been shared with this account)
>>> Upon signing in, click "see invitation" and accept the project invitation
>>> Upon accepting the invitation, it will take you to the project page
>>> Click "Real Time Datebase" to access the database that has been used for the project
>>> All the data will be created/updated/deleted in real time when the program is run on the Python IDE (PyCharm)

Running the file
>>> Open 'main.py' and right-click on anywhere on the code
>>> Select "Run 'main'" and follow the instruction on the Run window (Make sure you have installed pyrebase4 module before running the main.py file)
>>> The instruction will allow you to Create Data/ Update Data/ Delete Data
** For update and delete cases when unique ID is not known, an output in following format will be shown upon selecting the option,
("{'Unique ID': '< >'}", {'Address': {'Name': {'Firstname': '< >', 'Lastname': '< >'}, 'city': '< >', 'state': '< >', 'street': '< >', 'zip_code': '< >'}}),...

** Refer to the Unique ID when updating or deleting a complete user data or a certain piece of user data

To test Linting,
>>> Go to the Terminal and type in: pylint main.py

//////////////////////////////////////////////////// Test Cases //////////////////////////////////////////////////////////
>>> Deleting existing dummy data
1. Run the program > Select z
   Expected outcome: Invalid Input

2. Run the program > Select D (d is for Delete) > Select y
   Expected outcome: All existing data have been deleted from the database

>>> Creating user data with firstname, lastname, street, state, city and zipcode and assigning them a unique user ID
3. Run the program > Select s (s is for creating user data)> Enter a unique user ID NUMBER > Enter user details  <--------- When the zip code and user ID are both numeric values
   Expected outcome: Successfully stored in the database

4. Run the program > Select s > Enter a unique user ID NUMBER > Enter user details  <--------- When either the zip code or the user ID is not numeric
   Expected outcome: ZIP code and Unique ID can only be numeric and the program will ask for valid user input again

>>> Updating user data on the database
5.1 Run the program > Select u (u is for Update) > Select y > Input user's unique ID<--------------------- Testing when user ID is known
   5.1.1 Select f to update first name of that user > Update with new firstname > Select Y (to continue updating) or N (to exit updating)
   5.1.2 Select l to update last name of that user > Update with new lastname > Select Y (to continue updating) or N (to exit updating)
   5.1.3 Select s to update street details of that user > Update with new street details > Select Y (to continue updating) or N (to exit updating)
   5.1.4 Select st to update state details of that user > Update with new state details > Select Y (to continue updating) or N (to exit updating)
   5.1.5 Select c to update city detail of that user > Update with new city details > Select Y (to continue updating) or N (to exit updating)
   5.1.6 Select z to update Zip code of that user's address > Update with new zip > Select Y (to continue updating) or N (to exit updating)
   ** Invalid input at any point will eventually exit the program
   Expected outcome: Successfully updated

5.2 Run the program > Select u (u is for Update) > Select n > Existing data will be output in the system > Refer to the output and input user's unique ID<--------------------- Testing when user ID is unknown
   5.2.1 Select f to update first name of that user > Update with new firstname > Select Y (to continue updating) or N (to exit updating)
   5.2.2 Select l to update last name of that user > Update with new lastname > Select Y (to continue updating) or N (to exit updating)
   5.2.3 Select s to update street details of that user > Update with new street details > Select Y (to continue updating) or N (to exit updating)
   5.2.4 Select st to update state details of that user > Update with new state details > Select Y (to continue updating) or N (to exit updating)
   5.2.5 Select c to update city detail of that user > Update with new city details > Select Y (to continue updating) or N (to exit updating)
   5.2.6 Select z to update Zip code of that user's address > Update with new zip > Select Y (to continue updating) or N (to exit updating)
   ** Invalid input at any point will eventually exit the program
   Expected outcome: Successfully updated

>>> Deleting user data from database
6.1 Deleting an entire user details
    Run the program > Select d (d is for delete) > Select n > Select y (if ID is known to user) / Select n (if ID is unknown)
    > Enter Unique user ID > Select y (to delete an entire user details)
6.2 Deleting a parameter of user details
    Run the program > Select d (d is for delete) > Select n > Select y (if ID is known to user) / Select n (if ID is unknown)
    > Enter Unique user ID > Select n (to delete a parameter of a giver user) >
    6.2.1 Select f to remove firstname of user with the unique ID
    6.2.1 Select l to remove lastname of user with the unique ID
    6.2.1 Select s to remove street name/number of user with the unique ID
    6.2.1 Select st to remove state name of user with the unique ID
    6.2.1 Select c to remove city of user with the unique ID
    6.2.1 Select z to remove zip code of user with the unique ID
