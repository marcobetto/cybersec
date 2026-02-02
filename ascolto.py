import socket
server_socket = socket.socket()
host = '127.0.0.1'
port = 6364
server_socket.bind((host, port))
server_socket.listen(1)
print(f"server listening on {host}:{port}") #f consente di incastonare le graffe
conn, addr = server_socket.accept() #accept è un metodo, ascolta la porta indicata sopra
print(f"connected by {addr}")
#apertura file in scrittura, la fx open non ha bisogno di import e la w apre il file in modalità scrittura
f = open("logfile.txt", "w")
try:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        richiesta = data.decode()
        risposta = f"ho ricevuto il tuo messaggio: {richiesta}"  
        #print(risposta)
        f.write(risposta)
        conn.sendall(risposta.encode())
finally:
    #chiudere funzione f
    f.close()
    conn.close()
    server_socket.close()
