import socket, pickle
s = socket.socket()
s.bind(("localhost", 50001))
s.listen(1)
c,a = s.accept()
filetodown = open("./recibido.txt", "wb")
while True:
   print("Receiving....")
   aux = c.recv(1024)
   if aux[-3:] == 'fin':
        aux1 = aux[:-3]
        data = pickle.loads(aux1)
        filetodown.write(data)
        break
   data = pickle.loads(aux)
   filetodown.write(data)
filetodown.close()
c.send("Thank you for connecting.")
c.shutdown(2)
c.close()
s.close()
