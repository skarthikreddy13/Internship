#The program to send multiple calls of upload data dated 11th July
import socket
import time

# Server configuration
HOST = 'localhost'  # Server IP address
PORT = 1234        # Server port number
BUFFER_SIZE = 8192
def start_server():
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        global count
        global sum
        
        
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print('Server listening on {}:{}'.format(HOST, PORT))
        client_socket, client_address = server_socket.accept()
        data = b'X' * 10 * 1024 * 1024  # 1 MB
        #start_time = time.time()

        client_socket.sendall(data)

        #end_time = time.time()
        
if __name__ == '__main__':
       
    for i in range(0,10):
            start_server()
