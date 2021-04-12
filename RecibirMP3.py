import socket, pickle
import os
s = socket.socket()
s.bind(('', 5000))
s.listen(1)
c,a = s.accept()
filetodown = open("./salida2.mid", "wb")
while True:
   print("Receiving....")
   aux = c.recv(512)
   if aux[-3:] == 'fin':
        aux1 = aux[:-3]
        #data = pickle.loads(aux1)
        filetodown.write(aux1)
        break
   #data = pickle.loads(aux)
   filetodown.write(aux)
filetodown.close()
c.send("Thank you for connecting.")
os.system('ls')
os.system('cp salidaprueba.mid ../../Symbolic-Melody-Identification/')
os.system('conda run -n IA ../../Symbolic-Melody-Identification/terminal_client.py --model model.pkl --extract salidaprueba.mid output.mid')
os.system('ls')
c.shutdown(2)
c.close()
s.close()
