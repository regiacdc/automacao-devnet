import paramiko
import time

device_list = [
{
    'hostname': '192.168.1.154',
    'port': 22,
    'username': 'cisco',
    'password': 'cisco',
    },
{
    'hostname': '192.168.1.155',
    'port': 22,
    'username': 'cisco',
    'password': 'cisco',
    },
]

interface_commands = [
    'configure terminal',
    'interface Loopback1',
    'description PythonDevNet',
    'ip address 10.10.0.10 255.255.255.255',

    'interface Loopback2',
    'description PythonDevNet',
    'ip address 10.20.0.20 255.255.255.255',

    'interface Loopback3',
    'description PythonDevNet',
    'ip address 10.30.0.30 255.255.255.255',

    'interface Loopback4',
    'description PythonDevNet',
    'ip address 10.40.0.40 255.255.255.255',

    'interface Loopback5',
    'description PythonDevNet',
    'ip address 10.50.0.50 255.255.255.255',
    'end',
]

def configure_loopback(device_info, commands):
    try:
        # Cria uma conexão SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(
            device_info['hostname'],
            port=device_info['port'],
            username=device_info['username'],
            password=device_info['password'],
            timeout=10
        )

        # Inicia uma sessão interativa
        remote_conn = ssh.invoke_shell()

        for command in commands:
            remote_conn.send(command + '\n')
            output = remote_conn.recv(65535).decode('utf-8')
            print(output)

        ssh.close()
        print(f"Configurações aplicadas em {device_info['hostname']}")

    except Exception as e:
        print(f"Erro na conexão com {device_info['hostname']}: {str(e)}")

# Loop através da lista de dispositivos e aplique as configurações
for device_info in device_list:
    configure_loopback(device_info, interface_commands)
