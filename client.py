from socket import *
from select import select
import sys

PORT=20000
BUFFER_SIZE = 65507

def main():
    sock = socket(AF_INET, SOCK_DGRAM)  
    serverAddr = ('localhost', PORT)
    user_input=input('''What's your username?''')
    user_name=user_input
    msg='join '+user_input
    sock.sendto(msg.encode(), serverAddr)

    while True:
        rset, _, _ = select([sock, sys.stdin], [], [], 0.05)

        for s in rset:
            if s is sock:
                data, peer = sock.recvfrom(BUFFER_SIZE)
                print(data.decode())
            elif s is sys.stdin:
                user_input = sys.stdin.readline().strip()
                if user_input == 'users':
                    msg='users'
                    sock.sendto(msg.encode(),serverAddr)

                elif user_input.startswith('to '):
                    sock.sendto(user_input.encode(),serverAddr)

                elif user_input=='leave':
                    sock.sendto('leave'.encode(), serverAddr)  
                    sock.close()  
                    return  # ?

if __name__ == "__main__":
    main()


