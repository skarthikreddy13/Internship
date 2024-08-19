#Program to send data from server to client in order to achieve about 100Mbps speed between 2 different systems

import socket
import time

# Server configuration
HOST = '127.0.0.1'  # Server IP address
PORT = 1234        # Server port number
BUFFER_SIZE = 8192

def calculate_upload_speed(start_time, end_time, data_size):
    duration = end_time - start_time
    speed = data_size / duration  # Bytes per second
    speed = speed/125000
    return speed

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print('Server listening on {}:{}'.format(HOST, PORT))

        while True:
            client_socket, client_address = server_socket.accept()
            print('Connected by', client_address)

            start_time = time.time()
            data_size = 0

            while True:
                data = client_socket.recv(BUFFER_SIZE)
                if not data:
                    break
                data_size += len(data)

            end_time = time.time()
            upload_speed = calculate_upload_speed(start_time, end_time, data_size)
            print('Upload speed:', upload_speed, 'Mbps')

            client_socket.close()
            print('Connection closed by', client_address)

if __name__ == '__main__':
    start_server()
