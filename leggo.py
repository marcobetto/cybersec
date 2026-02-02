nomefile = "logfile.txt" 
    try: 
        f = open(nomefile, "r")
        righe = f.readlines()
        for riga in righe:
            print(riga, end='')
    except FileNotFoundError as e:
        print(f"[-] errore bloccante: {str(e)}")

  
