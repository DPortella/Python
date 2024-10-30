import paramiko

host = #endereço
user = #usuário
passwd = #senha

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=passwd)
while True:
    stdin, stdout, stderr = client.exec_command(input("Comando: "))
    for i in stdout:
        print(i.strip())
    for i in stderr:
        print(i.strip())
