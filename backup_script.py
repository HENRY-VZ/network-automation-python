import time
from netmiko import ConnectHandler

network_device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'password123',
}

def backup_config():
    try:
        print(f"Conectando a {network_device['ip']}...")
        net_connect = ConnectHandler(**network_device)
        output = net_connect.send_command("show running-config")
        
        with open("router_backup.txt", "w") as file:
            file.write(output)
            
        print("¡Backup exitoso!")
        net_connect.disconnect()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    backup_config()
