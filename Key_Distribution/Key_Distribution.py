from flask import Flask, request
from des import DesKey
from Database import DataBase, Request_Base
app = Flask(__name__)



@app.route('/authenticate', methods=['Post'])
def authenticate_client():
    req_messege = request.get_json()
    user_name = req_messege['User']
    encrypted_request = req_messege['Request']
    key = DataBase[user_name]
    desKey = DesKey(bytes(key, encoding='UTF'))
    req = desKey.decrypt(bytes(encrypted_request,encoding="UTF-16")[2:], padding = True)
    if req.decode('UTF') in Request_Base:
        return TGT()
    else:
        return '0'

def TGT():
    key = DataBase['TGS']
    desKey = DesKey(bytes(key, encoding="UTF"))
    tgt = 'Ticket Granting Ticket'
    encrypted_tgt = desKey.encrypt(bytes(tgt, encoding='UTF'), padding=True)
    return encrypted_tgt.decode('UTF-16')


@app.route('/get_ticket', methods=['Post'])
def grant_ticket():
    req_messege = request.get_json()
    encrypted_tgt = req_messege["TGT"]
    key = DataBase['TGS']
    desKey = DesKey(bytes(key, encoding='UTF'))
    decrypted_tgt = desKey.decrypt(bytes(encrypted_tgt,encoding="UTF-16")[2:], padding = True)
    if decrypted_tgt.decode('UTF') == "Ticket Granting Ticket":
        return Ticket()
    else:
        return '0'

def Ticket():
    key = DataBase['Server']
    desKey = DesKey(bytes(key, encoding='UTF'))
    ticket = 'Access Granted!!'
    encrypted_ticket = desKey.encrypt(bytes(ticket, encoding='UTF'), padding=True)
    return encrypted_ticket.decode('UTF-16')


if __name__ == "__main__":
    app.run()
