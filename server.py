from socket import *

PORT = 20000
BUFFER_SIZE = 65507

def udp_server():
    sock = socket(AF_INET, SOCK_DGRAM)  
    serverAddr = ('', PORT)
    sock.bind(serverAddr)
    print('UDP server is up and listening on port 20000')

    # The server must also keep track of the online clients as they join and leave the chat session
    clients={}

    while True:
        msg, clientAddr=sock.recvfrom(BUFFER_SIZE)
        msg=msg.decode()

        sender=None
        for name in clients:
            if clients[name]==clientAddr:
                sender=name
            
        if msg.startswith('join '):
            user_name=msg.split()[1]
            clients[user_name]=clientAddr
            print(user_name+' joined the chat')

        elif msg=='users':
            message='Online users: '+', '.join(clients)
            sock.sendto(message.encode(),clientAddr)

        elif msg.startswith('to '):
            friends=msg.split(' msg ')[0].split()[1:]
            message=msg.split(' msg ')[1]

            if friends==['all']:
                friends=[]
                for client in clients:
                    if client!=sender:
                        friends.append(client)

            for name in friends: 
                if name != sender:
                    response=''  
                    if name in clients: 
                        response+=sender+' says: <'+message+'>'
                        sock.sendto(response.encode(), clients[name])  
                    else:
                        err = 'Error message: <' + name + ' is not online!>'  
                        sock.sendto(err.encode(), clientAddr)  
        
        elif msg=='leave':
            if sender in clients:
                print(sender+' has left the chat')
                del clients[sender]

    sock.close()
if __name__ == "__main__":
    udp_server()