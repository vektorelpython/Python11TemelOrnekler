from OOPOrnek import FileTools

Log = FileTools(fileName="Log",
fileAddress=r"c:\2019",field=["Log Type","Log Message","Time"])
Contacts = FileTools(fileName="Contacts",
fileAddress=r"d:",field=["Name","Surname","Telephone"])

Contacts.AnaMenu()