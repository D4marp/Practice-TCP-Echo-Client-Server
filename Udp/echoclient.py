import socket
import sys
import argparse

host = '10.253.128.5'
data_payload = 2048

def echo_client_udp(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)

    try:
        message = "SELAMAT PAGI WARGA  PENS LAMONGAN"
        print("Sending %s" % message)
        sock.sendto(message.encode('utf-8'), server_address)

        data, server = sock.recvfrom(data_payload)
        print("Received: %s" % data.decode('utf-8'))
    finally:
        print("Closing connection to the server")
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Client Example for UDP')  # Menyesuaikan deskripsi untuk Client UDP
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client_udp(port)
