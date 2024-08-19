# Sending multiple data calls for download dated 11th July
import socket
import time

# Server configuration
HOST = 'localhost'  # Server IP address
PORT = 1234        # Server port number
BUFFER_SIZE = 8192
def calculate_upload_speed(start_time, end_time, data_size):
    duration = end_time - start_time
    speed = data_size / duration  # Bytes per second
    speed = speed/125000
    return speed
def send_data():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        data_size = 0
        start_time = time.time()
        while True:
                data = client_socket.recv(BUFFER_SIZE)
                if not data:
                    break
                data_size += len(data)

        end_time = time.time()
        upload_speed = calculate_upload_speed(start_time, end_time, data_size)
        print('Download speed:', upload_speed, 'Mbps')
        #sum=sum+upload_speed
        client_socket.close()
if __name__ == '__main__':
    for i in range(0,10):
        send_data()
