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

        elif msg=='users':
            message='Online users: '.join(clients)
            sock.sendto(message.encode(),clientAddr)

        elif msg.startswith('to '):

            if names[i] is not same as names[i] and online:
                socket.sendto(msg)
            for name in recipients: 
                if name == sender:  
                    continue # ignore sender
                if name in clients:  
                    out = sender + ': ' + text  # edited
                    sock.sendto(out.encode(), clients[name])  # edited
                else:
                    err = 'Error message: <' + name + ' is not online!>'  
                    sock.sendto(err.encode(), clientAddr)  
        
        elif msg=='leave':
            if sender in clients:
                del clients[sender]

    sock.close()
if ___name__ == "___main__":
    udp_server()