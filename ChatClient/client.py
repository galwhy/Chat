import  socket
import threading
import tkinter

class chat:
    window = tkinter.Tk()
    frame1 = tkinter.Frame(master=window, width = 500, height = 300, bg="")
    label = tkinter.Text(master=frame1, width=50, height=30,state='disabled', bg= "#ccc")
    entry = tkinter.Text(master= frame1, width = 50, height = 1 , bg= "#ccc")
    button = tkinter.Button(master=frame1,text = "Send")
    text:str
    sock:socket.socket



    def __init__(self, sock):
        self.window.minsize(width = 400, height = 530)
        self.window.maxsize(width = 400, height = 530)
        self.frame1.pack(fill=tkinter.BOTH, side=tkinter.TOP)
        self.label.pack()
        self.button.pack(fill=tkinter.BOTH)
        self.entry.pack()
        self.text = ""
        self.sock = sock



    def print_on_screen(self, message):
        self.label.config(state = 'normal')
        self.label.insert("end",message)
        self.label.config(state='disabled')
        self.label.yview_pickplace("end")

    def handle_click(self, event):
        message = self.entry.get("1.0",tkinter.END)[:1024]
        if(message[0] == "\n"): message = message[1:]
        self.sock.send(message.encode())
        self.print_on_screen(f"you: {message}")
        self.entry.delete("1.0",tkinter.END)

    def start(self):
        self.window.mainloop()

    def bind(self):
        self.entry.bind('<Return>', self.handle_click)
        self.button.bind('<Button-1>', self.handle_click)


def send(sock):
    while True:
        sock.send(input('').encode())

def recieve(sock, w):
    while True:
        message = sock.recv(1024).decode()
        if message != None:
            w.print_on_screen(message)


def client():
    port = 6200
    Ip = input('Enter an Ip address: ')
    address = (Ip, port)

    sock = socket.socket()
    sock.connect(address)
    print("Connected")
    sock.send(input('Please enter you name: ').encode())
    Chat = chat(sock)
    Chat.bind()


    #thread1 = threading.Thread(target=obj.start)
    thread2 = threading.Thread(target=recieve, args=(sock,Chat))


    thread2.start()
    Chat.start()

def main():
    client()



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
