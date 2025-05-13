# To use this, download the WebDB Python class file (called main.py) into the folder you are using.
# Rename main.py into webdb.py

from webdb import WebDB

webdb = WebDB()
webdb.create("variable", "password", "value")
webdb.update("variable", "password", "newvalue")
webdb.get("variable")
webdb.delete("variable", "password")
