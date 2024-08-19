# CLient Program to send data from server to client in order to achieve about 100Mbps speed between 2 different systems
import socket
import time

# Server configuration
HOST = '127.0.0.1'  # Server IP address
PORT = 1234        # Server port number
BUFFER_SIZE = 8192

def send_data():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        # Generate dummy data
        data = b'X' * 10 * 1024 * 1024  # 1 MB

        start_time = time.time()

        client_socket.sendall(data)

        end_time = time.time()

        print('Data sent successfully.')
        print('Elapsed time:', end_time - start_time, 'seconds')

if __name__ == '__main__':
    send_data()
