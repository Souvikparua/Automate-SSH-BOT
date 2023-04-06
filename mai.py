import re
import getpass
from fabric import Connection, Config

password = getpass.getpass("Enter your root password: ")

config = Config(overrides={'sudo': {'password': password}})
conn = Connection("192.168.0.1", user="souvik", config=config)

result = conn.run("ls -la", hide=True)

conn.run("pwd")

with conn.cd("c:/Users/souvik parua/desktop"):
    conn.run("touch myfile.txt")
    conn.run("pwd")
    
   #conn.sudo("apt install vim")
   # conn.run("neofetch")

result = conn.run("ifconfig")
lines = result.stdout.split("\n")
inet_lines = [l for l in lines if "inet " in l and "127.0.0.1" not in l]
span = re.search("inet ([0-9]+\.){3}[0-9]+", inet_lines[0]).span()
ip_address = inet_lines[0][span[0]+5:span[1]]
print(ip_address)
