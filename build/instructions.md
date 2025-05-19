## How to Self Host
1. Download the Bash script from the server folder you want (BlockDB is the wrapper for Scratch modifications, and depends on a WebDB server, so if you are self hosting a BlockDB server, please ensure to also run the WebDB server, and edit the code of the BlockDB server to meet the URL of your WebDB server.), move it into your documents folder and make it executable.
To make it executable, run these commands after moving it into your documents folder:
```
cd Documents
chmod u+x main.sh
./main.sh
```
3. Run the Bash script to run the Flask program.
4. After the program runs, you should be able to visit http://127.0.0.1:5000 to get the REST API locally.
5. The cloned repository should be in your documents folder.
6. Please use a WSGI server for deployment (I recommend [PythonAnywhere](https://www.pythonanywhere.com/)), but you can use a local server for developing.
7. To rerun the Flask program after you closed your server, run this command:
```
cd Documents
python3 -m flask --app WebDB/src/server/main.py run
```
or for Scratch modifications,
```
cd Documents
python3 -m flask --app WebDB/src/scratchwrapper/main.py run
```
Please note that your server is only hosted locally using this method.
