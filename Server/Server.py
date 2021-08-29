from flask import Flask, request, send_from_directory
from des import DesKey
import os
app = Flask(__name__)

SERVER_KEY = "prabhu333"

@app.route('/file_server', methods=["Post"])
def Grant_Access():
    req_messege = request.get_json()
    encrypted_ticket = req_messege['Ticket']
    file_name = req_messege['File']
    desKey = DesKey(bytes(SERVER_KEY, encoding='UTF'))
    decrypted_ticket = desKey.decrypt(bytes(encrypted_ticket,encoding="UTF-16")[2:], padding = True)
    if decrypted_ticket.decode('UTF') == 'Access Granted!!':
        return Get_File(file_name)
    else:
        return '0'

def Get_File(file_name):
    try:
        File = open('Files/'+file_name,'r')
        return File.read()
    except:
        return '-1'



if __name__== "__main__":
    app.run(port=int(os.getenv('PORT', 3000)))