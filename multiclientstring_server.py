#Program to read multiple strings from the client
import socket


def server_program():
   
    host = 'localhost'
    port = 5000 

    server_socket = socket.socket()  # get instance
   
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
       
        data = conn.recv(1024).decode()
        if not data:
           
            break
        print("Data from the user: " + str(data))
        data = 'Enter the next name'
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
