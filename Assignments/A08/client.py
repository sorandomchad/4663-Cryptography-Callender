"""
https://requests.readthedocs.io/en/master/user/quickstart/
"""
import requests
import json
from crypto_class2 import Crypto
import pprint as pp
import base64
import sys
import sched, time      #modules for performing an action every x seconds


##########################
# GLOBAL VARIABLES
##########################
TOKEN = 'af82200aa922a67d1843148b043f1d66'
UID = '5217300'
API = 'http://msubackend.xyz/api/?route='
USERS = {}
PUBKEYS = {}


##########################
# GET METHODS
##########################
def pubKey():
    """ Gets all users' public keys from the server. """

    print("Fetching all public keys from the server...")
    global PUBKEYS
    route = 'getPubKey'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"
    r = requests.get(url)

    try:
        keys = r.json()
    except ValueError as e:
        print("Invalid Json!!!")
        print(r.text)

    for key in keys['data']:
        PUBKEYS[key['uid']] = key


def getUsers():
    """ Gets all users from the server. """

    print("Fetching all users from the server...")
    global USERS
    global PUBKEYS

    route = 'getUser'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"
    r = requests.get(url)

    try:
        users = r.json()
    except ValueError as e:
        print("Invalid Json!!!")
        print(r.text)

    for user in users['data']:
        if user['uid'] in PUBKEYS:
            user['pubkey'] = PUBKEYS[user['uid']]
            USERS[user['uid']] = user



def getActive():
    """ Gets the active users. """

    route = 'getActive'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"
    r = requests.get(url)

    active_users = r.json()
    active_users = active_users['data']

    real_active_users = []
    for active in active_users:
        active['fname'] = USERS[active['uid']]['fname']
        active['lname'] = USERS[active['uid']]['lname']
        active['email'] = USERS[active['uid']]['email']
        active['pubkey'] = PUBKEYS[active['uid']]
        real_active_users.append(active)

    return real_active_users


def getMessages(count=1, latest=True):
    """ Gets decrypted messages from the server. """

    print("Checking for new messages...")

    route = 'getMessage'
    url = f"{API}{route}&token={TOKEN}&uid={UID}&count={count}"
    r = requests.get(url)

    D = Crypto()
    D.load_keys(priv_file="my_key.txt")

    messages = r.json()
    messages = messages['data']         # get all the messages received from other users

    for message in messages:
        fid, received = message['fid'], message['message']         # grabs most recent message and user's id
        received_bytes = received.encode('utf-8')               # prepares message
        received = base64.decodebytes(received_bytes)           # for decryption

        try:
            decrypted = D.decrypt(received)         #decrypts message
            print(f"\nfrom: {USERS[fid]['fname']} {USERS[fid]['lname']}")
            print("message:", decrypted, '\n')
        except ValueError:
            print(f"\nfrom: {USERS[fid]['fname']} {USERS[fid]['lname']}")
            print("message:", received, '\n')


###################################
# POST METHODS
###################################
def postPubKey(pub_key):
    """ Post generated public key to the server. """

    print("Uploading your public key to the server...")
    route = 'postPubKey'

    url = f"{API}{route}&token={TOKEN}&uid={UID}&pub_key={pub_key}"

    payload = {
        'uid':UID,
        'pubkey':pub_key
    }
    
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, headers=headers, json=payload)
    return r.json()


def postMessage(message,to_uid):
    """ Posts an encrypted message to the server for the specified user to get. """

    print(f"Posting message to {USERS[to_uid]['fname']} {USERS[to_uid]['lname']}...")

    route = 'postMessage'
    url = f"{API}{route}&token={TOKEN}&uid={UID}"

    A = Crypto()
    A.load_keys(PUBKEYS[to_uid]['pubkey'])

    encrypted = A.encrypt(message)
    encrypted_bytes = base64.b64encode(encrypted)
    message = encrypted_bytes.decode('utf-8')

    payload = {
       'uid':UID,
       'to_uid':to_uid,
       'message':message,
       'token':TOKEN
    }

    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, headers=headers, json=payload)
    return r.json()


if __name__ == '__main__':
    print("Starting session...")
    print("Generating your session keys...")

    action = 0
    option = ''

    option = input("Would you like to generate new keys for this session? (y/n) ")
    if option == 'y':
        C = Crypto()
        C.generate_keys()

        C.store_keys()
    elif option == 'n':
        pass

    # with open("my_pub_key.txt", "r") as f:
    #     my_key = f.read()
    
    # C.load_keys(pub_key=my_key)
    # print(C.public_key)


    # postPubKey(my_key)


    pubKey()
    getUsers()

    print("\n---------------------------------")
    print("MENU")
    print("1. Check messages.")
    print("2. Post a message.")
    print("3. Kill program")
    print("---------------------------------\n")

    action = input("Choose an option from the menu: ")

    while action != '3':
        if action == '1':
            getMessages(count=2)
        elif action == '2':
            to_uid = input("Enter the recepient's id: ")
            message = input("Type message here: ")
            postMessage(message, to_uid)
        elif action == '3':
            sys.exit(1)

        print("\n---------------------------------")
        print("MENU")
        print("1. Check messages.")
        print("2. Post a message.")
        print("3. Kill program")
        print("---------------------------------\n")
        action = input("Choose an option from the menu: ")
        
    # active = getActive()

    # os.remove("my_pub_key.txt")
    # os.remove("my_priv_key.txt")
