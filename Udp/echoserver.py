import socket
import sys
import argparse

host = '10.253.128.5'
data_payload = 2048

def echo_server_udp(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (host, port)
    print("Starting up echo server on %s port %s" % server_address)

    sock.bind(server_address)
    while True:
        print("Waiting to receive message from client")
        data, address = sock.recvfrom(data_payload)
        if data:
            print("Data: %s" % data)
            sock.sendto(data, address)
            print("sent %s bytes back to %s" % (data, address))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example for UDP')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server_udp(port)
