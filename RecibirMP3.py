import socket, pickle
import os
s = socket.socket()
s.bind(('', 5000))
s.listen(1)
c,a = s.accept()
filetodown = open("./salidaprueba.mid", "wb")
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
os.system('cp salidaprueba.mid ../../app/Symbolic-Melody-Identification/salidaprueba.mid')
os.system('conda run -n IA ../../app1/Symbolic-Melody-Identification/terminal_client.py --model model.pkl --extract ../../app1/Symbolic-Melody-Identification/prueba2.mid edusalidaprueba1.mid')
os.system('ls')
c.shutdown(2)
c.close()
s.close()
