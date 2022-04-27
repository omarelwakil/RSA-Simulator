import socket
import rsa_algorithm as rsa


def receiver():
    host = socket.gethostname()   # get local machine name
    port = 8080  # Make sure it's within the > 1024 $$ <65535 range

    print("Creating to socket...")
    s = socket.socket()
    s.bind((host, port))
    print("Socket is created.")

    print("Waiting for connection...")
    s.listen(1)
    client_socket, adress = s.accept()
    print("Connected to sender(" + str(adress) + ")")

    p = input('Enter p value: ')
    while p == '' or not (rsa.is_integer(p) and rsa.is_prime(int(p))):
        p = input('Invalid value, Enter p value: ')

    q = input('Enter q value: ')
    while q == '' or not (rsa.is_integer(q) and rsa.is_prime(int(q))):
        q = input('Invalid value, Enter q value: ')

    print("Generating public key and private_keys...")

    e, d, n, e_s = rsa.key_generation(int(p), int(q))
    print("e: ", e, ", d: ", d, ", n: ", n)
    print("Generated keys.")

    print("Sending public key to sender...")
    client_socket.send((str(e) + "," + str(n)).encode('utf-8'))
    print("Sent public key.")

    print("------------------------------------------------------")
    print("Waiting for message...")
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            print("Socket connection is closed.")
            break
        print("Received encrypted message: " + data)

        print("Decrypting message...")
        plaintext = rsa.decryption(data, d, n)
        print("Message decrypted: " + plaintext)
        print("Waiting for message...")

    client_socket.close()


if __name__ == '__main__':
    receiver()
