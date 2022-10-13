import socket
import _thread


def rec_send(client:socket.socket, clients:list, addr):
    try:
        name = client.recv(1024).decode().replace("\n", "")
        while True:
            msg = client.recv(1024).decode()
            for c in clients:
                msg2 = f"{name}: {msg}"
                if c != client:

                    c.send(msg2.encode())
    except:
        clients.remove(client)



def server():
    clients = []
    port = 6200

    print(f"Server IP: {socket.gethostbyname_ex(socket.gethostname())[2][0]}")
    Ip = socket.gethostbyname_ex(socket.gethostname())[2][0]
    address = (Ip, port)

    sock = socket.socket()
    sock.bind(address)
    sock.listen(10)

    while True:
        (c, addr) = sock.accept()
        print("client connected")
        clients.append(c)
        _thread.start_new_thread(rec_send, (c, clients, addr))




def main():
    server()



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
