import socket
import argparse

host = 'localhost'
data_payload = 1024

def echo_client_input(port):
    # Membuat objek socket dengan protokol TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)

    # Menginisialisasi koneksi ke server
    sock.connect(server_address)

    try:
        # Mengirim data ke server
        message = input("Ketikkan input: ")
        print("Sending %s" % message)
        sock.sendall(message.encode('utf-8'))

        # Melihat respon
        amount_received = 0
        amount_expected = len(message)
        
        while amount_received < amount_expected:
            # Menerima data, balasan dari server
            data = sock.recv(16)
            amount_received += len(data)
            print("Received: %s" % data.decode('utf-8'))

    except socket.error as e:
        print("Socket error: %s" % str(e))
    except Exception as e:
        print("Other error: %s" % str(e))
    finally:
        print("Closing connection to the server")
        sock.close()

if __name__ == '__main':
    parser = argparse.ArgumentParser(description='Socket Client Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client_input(port)
