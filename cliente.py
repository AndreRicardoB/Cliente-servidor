import socket
import pickle

HOST = '127.0.0.1'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

lista = []
produto = ""

while produto != 0:
	produto = input("Digite o produto que quer \n Digite 0 para confirmar")


	if produto != "":
		lista.append(produto)

	elif produto == "":
		print("nome do produto necessario!")


numeroDeProdutos = len(lista)

data_string = picke.dumps(lista)
s.send(data_string)
s.send(sendall(numeroDeProdutos))
data = s.recv(5000)
data_arr = pickle.loads(data)
s.close()












