# To use this, download the WebDB Python class file (called webdb.py) into the folder you are using.

from webdb import WebDB
webdb = WebDB()
webdb.create("variable", "password", "value")
webdb.update("variable", "password", "newvalue")
print(str(webdb.get("variable")))
webdb.delete("variable", "password")
