from netmiko import ConnectHandler
import paramiko
import time

host = '192.168.1.154'
port = 22
username = 'cisco'
password = 'cisco'

# Comandos de configuração da interface
interface_commands = [

    'enable',  # Entra no modo privilegiado
    'cisco',
    'configure terminal',  # Entra no modo de configuração
    'interface loopback1',  # Substitua pela interface desejada
    'description IntDevNet',
    'ip address 10.10.0.10 255.255.255.0',  # Substitua pelo endereço IP desejado
    'no shutdown',  # Habilita a interface

    'interface loopback2',  # Substitua pela interface desejada
    'description IntDevNet',
    'ip address 10.20.0.20 255.255.255.0',  # Substitua pelo endereço IP desejado
    'no shutdown',  # Habilita a interface

    'interface loopback3',  # Substitua pela interface desejada
    'description IntDevNet',
    'ip address 10.30.0.30 255.255.255.0',  # Substitua pelo endereço IP desejado
    'no shutdown',  # Habilita a interface
    'end',  # Sai do modo de configuração
    'exit',  # Encerra a sessão
]

# Cria uma conexão SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(host, port, username, password, timeout=10)

    # Inicia uma sessão interativa
    remote_conn = ssh.invoke_shell()

    for command in interface_commands:
        remote_conn.send(command + '\n')
        time.sleep(1)
        output = remote_conn.recv(65535).decode('utf-8')
        print(output)

    ssh.close()
except Exception as e:
    print(f"Erro na conexão SSH: {str(e)}")

