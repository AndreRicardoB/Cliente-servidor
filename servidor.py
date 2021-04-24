import socket 

HOST = '127.0.0.1'
PORT = 50000



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print('aguardando conexão de um cliente')
conn, ender = s.accept()

print ('conectado em', ender)

produtosDisponiveis = ["arroz", "feijão", "batata", "frango", "carne"]
numeroProdutosDisponiveis = len(produtosDisponiveis)
produtosCompra = []



for i in range (0, numeroDeProdutos-1):
	for j in range (0, numeroProdutosDisponiveis-1):
		if  lista[i] == produtosDisponiveis[j]:
			produtosCompra.append(produtosDisponiveis[j])
			i = i + 1
			j = 0 



while True:
    data = conn.recv(5000)
    if not data:
        print("fechando a conexão")
        conn.close()
        break
    conn.sendall(data)
