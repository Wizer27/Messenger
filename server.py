import socket
import threading 



HOST = '127.0.0.1' # HOST
PORT = 1234 # PORT
LIMIT = 5
active_clinets = [] # all connected users

 
#listenig for messages from user
def listen_for_messages(client,username):
    while 1:
        
        message = client.recv(2048).decode('utf-8')
        if message != '':
            final_msg = username + '-' +  message  
            send_meesages(final_msg)
        else:
            print(f'the message send from clinet {username}  is empty')
            
            
# send message to a single user            
def send_mes_to_clinet(message,client):
    client.sendall(message.encode())
                
# send message to users
def send_meesages( message):
    for user in active_clinets:
        send_mes_to_clinet(user[1], message)
        
        



def client_handler(client):
    # Server listening for client message
    while 1:
        
        
        
        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clinets.append((username, client))
            break
            
        else:
            print("username if empty")    
    threading.Thread(target = listen_for_messages, args = (client, username, )).start() 

#main fubction
def main():
    #server
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    #server.bind((HOST,PORT))
    try:
        server.bind((HOST,PORT))
        print("Server is running ")
    except: 
        print(f"Unable  to connect to {HOST} on port {PORT}")       
    server.listen(LIMIT) # only 5 connections allowed 
    while 1:
        cl,addr = server.accept()
        print(f"connected from {addr}")
        
        threading.Thread(target = client_handler, args = (cl, )).start()
if __name__ == "__main__":
    main()
    
     
