import socket
import rsa_algorithm as rsa


def client():
    host = socket.gethostname()  # get local machine name
    port = 8080  # Make sure it's within the > 1024 $$ <65535 range

    print("Connecting to socket...")
    s = socket.socket()
    s.connect((host, port))
    print("Socket is connected.")

    print("Waiting receive public key...")
    publickey = s.recv(1024).decode('utf-8')
    print("Received public key: " + publickey)

    e, n = publickey.split(',')
    e, n = int(e), int(n)

    print("------------------------------------------------------")
    message = input('Enter message to send (To close, type "exit()"): ')
    while message != 'exit()':
        if message == '':
            message = input(
                'Invalid, Enter message to send (To close, type "exit()"): ')
            continue

        print("Encrypting message...")
        ciphertext_key_code, ciphertext_char = rsa.encryption(message, e, n)
        print("Message encrypted: " + ciphertext_char)

        print("Sending encrypted message...")
        s.send(ciphertext_key_code.encode('utf-8'))
        message = input('Enter message to send (To close, type "exit()"): ')

    print("Closing socket...")
    s.close()


if __name__ == '__main__':
    client()
