from socket import *
from threading import Thread



BRIGHT_BLACK = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
BRIGHT_WHITE = '\033[97m'
BRIGHT_END = '\033[0m'

class Colors: 
	BLACK = '\033[30m' 
	RED = '\033[31m' 
	GREEN = '\033[32m' 
	YELLOW = '\033[33m' 
	BLUE = '\033[34m' 
	MAGENTA = '\033[35m' 
	CYAN = '\033[36m' 
	WHITE = '\033[37m' 
	UNDERLINE = '\033[4m' 
	RESET = '\033[0m'

class Background: 
	BLACK = '\033[40m' 
	RED = '\033[41m' 
	GREEN = '\033[42m' 
	YELLOW = '\033[43m' 
	BLUE = '\033[44m' 
	MAGENTA = '\033[45m' 
	CYAN = '\033[46m' 
	WHITE = '\033[47m'


s=socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1",7777))

print('서버에 접속하였습니다')


def send(s):
    while True:
        print(Colors.WHITE+">>"+Colors.RESET)
        msg = input("")
       
        if msg == 'exit' or '종료':
            break   
        
        s.send(str(msg).encode())
        

def receive(s):
    while True:
        reply = s.recv(1024).decode("utf-8")
        print(Colors.GREEN+"Server: " + reply+Colors.RESET)
        #print(Colors.WHITE+">>"+Colors.RESET)

  
        
 
send = Thread(target = send, args = (s,))
receive = Thread(target = receive, args = (s,))
    

send.start()
receive.start()

send.join()
s.close() 
