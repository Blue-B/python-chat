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


def send(s):
    while True:

        print(Colors.WHITE+">>"+Colors.RESET,end="")
        message = input("")

        if message == 'exit':
            break

        s.send(str(message).encode("utf-8")) 

        


        
def receive(s):
    while True:
        reply = s.recv(1024).decode("utf-8")               
        
        print(Colors.GREEN+"Client:" + reply+Colors.RESET)


s = socket(AF_INET, SOCK_STREAM)


s.bind(("0.0.0.0",7777))
s.listen(5) #정수5는 해당 소켓이 5개의 접속을 허용한다는 내용임

print('서버가 연결을 기다리고 있습니다')



s,addr = s.accept() #접속할때까지 대기하다가 클라이언트가 접속하면 새로운 소켓을 리턴한다
print(str(addr)+"에서 접속하였습니다")

send = Thread(target = send, args = (s,))
receive = Thread(target = receive, args = (s,))

send.start()
receive.start()

send.join()
s.close()
