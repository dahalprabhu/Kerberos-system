from des import DesKey
import getpass
import requests
import time

def create_AS_request():
    messege = 'File Request'
    user = 'prabhu'
    print('Enter your Username: ',user)
    key = getpass.getpass("Enter your Password: ")
    try:
        desKey = DesKey(bytes(key, encoding='UTF'))
    except:
        print('Password Error!!\nCharacters in tha password should be multiple of 8 for DES.')
        exit()
    encrypted = desKey.encrypt(bytes(messege, encoding='UTF'), padding=True)
    request = {"User":user, "Request": encrypted.decode("UTF-16")}
    return request

def get_TGT():
    request = create_AS_request()
    try:
        tgt = requests.post('http://localhost:5000/authenticate', json=request).text
        if tgt != '0':
            return tgt
        else:
            print("Key Error!")
            exit()
    except:
        print('Server not Found! Run Key_Distribution/Key_Distribution.py')
        exit()

def get_ticket(tgt):
    request = {'User': 'Ram', "TGT": tgt}
    try:
        ticket = requests.post('http://localhost:5000/get_ticket', json=request).text
        if ticket != '0':
            return ticket
        else:
            print('Key Error!')
            exit()
    except:
        print('Server not Found! Run  Key_Distribution/Key_Distribution.py')
        exit()

def get_file(ticket, File):
    request = {'User': 'Ram', "Ticket": ticket, "File": File}
    try:
        obtained_file = requests.post('http://localhost:3000/file_server', json=request).text
        if obtained_file ==  '0':
            print('Key Error!')
            exit()
        elif obtained_file == '-1':
            print('File Not Found')
            exit()
        else:
            return obtained_file
    except:
        print('File Server not Found! Run Server/Server.py')
        exit()
tgt = get_TGT()
print('\nTicket Granting Ticket has been sucessfully accuried from the Authentication Server')
print('-------------------------------------------------------------------------------------\n')
time.sleep(1)

ticket = get_ticket(tgt)
print('Server Ticket has been sucessfully accuried from the Ticket Granting Server')
print('--------------------------------------------------------------------------------\n')
time.sleep(1)

wanted_file = "Sonnet.txt"
obtained_file = get_file(ticket, wanted_file)
print('File Access Granted. Accessing File \n')
print('--------------------------------------------------------------------------------')
time.sleep(0.75)
print(wanted_file,'\n')
print(obtained_file)
print('--------------------------------------------------------------------------------')