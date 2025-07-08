import requests
import hashlib
import random
import time

def hash(string: str) -> str:
    return hashlib.sha256(string.encode()).hexdigest()

print("eShell Miner")
print("by SeafoodStudios")
print("To login, signup and/or access your account, go here:")
print("https://eshells.seafoodstudios.com/\n")

start = ""
while True:
    while not start == "mine" and not start == "exit":
        start = str(input("Would you like to begin mining or exit (mine/exit)? "))
    if start == "mine":
        address = str(input("Where would you like to send the results of the mining? "))
        print("Mining has begun. To exit, press Control + C, or close the window.")
        while True:
            try:
                theproof = str(random.randint(1,10000000000))
                thehash = str(hash(theproof))
                if thehash.startswith("0000000"):
                    response = requests.get(f"""https://eshells.pythonanywhere.com/submit_hash/{address}-{thehash}-{theproof}""")
                    print("\nNew Hash Found!")
                    print(response.text)
                    print(f"""Technical data: {thehash} was made from {theproof}.""")
            except Exception as e:
                print("Error: " + str(e))
            time.sleep(10)
    elif start == "exit":
        print("Exiting...")
        break
    else:
        print("Error: Input Error")
