import socket, pickle
s = socket.socket()
s.connect(("localhost", 50001))
filetosend = open("./entrada.mp3", "rb")
aux = filetosend.read(1024)
#data = pickle.dumps(aux)
while aux:
    print("Sending...")
    s.send(aux)
    aux = filetosend.read(1024)
    #data = pickle.dumps(aux)

filetosend.close()
s.send('fin')
print("Done Sending.")
print(s.recv(1024))
s.shutdown(2)
s.close()
