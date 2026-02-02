    import socket
    server_socket = socket.socket()
    host = '127.0.0.1'
    port = 6364
    server_socket.bind((host, port))
    server_socket.listen(1)
    f = open('logfile.txt', 'w') #apertura file in scrittura, la fx open non ha bisogno di import e la w apre il file in modalità scrittura
    f.write(f"server listening on {host}:{port}\n")
    for i in range (6):
        conn, addr = server_socket.accept() #accept è un metodo, ascolta la porta indicata sopra
        f.write(f"connected by {addr}\n")
        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                richiesta = data.decode()
                if richiesta == 'SHUTDOWN':
                    break
                risposta = f"ho ricevuto il tuo messaggio: {richiesta}\n"  
            #print(risposta)
                f.write(risposta)
                conn.sendall(risposta.encode())
            
            if richiesta == 'SHUTDOWN':
                break
        finally:
            conn.close() 
    f.close()    #chiudere funzione f
    server_socket.close()
