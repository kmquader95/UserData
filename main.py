from class_ReadData import ReadData
ReadData()
# Getting existing data (if available)
####################### STORAGE ####################################
db_status = input("[S]tore/ [U]pdate/ [D]elete: ")
if db_status.lower() == "s":
    #Creating User data
    from class_CreateData import CreateData
    CreateData()
#################### UPDATING DATA #################################
elif db_status.lower() == "u":
    #Updating database
    from class_update import update
    update()
#################### DELETING DATA #################################
elif db_status.lower() == "d":
    #Deleting data from database
    from class_delete import delete
    delete()

else:
    print("Invalid Input from the user")
    print("End of program")
