"""
Функция принимает словарь с параметрами подключения к устройству, комманду и 
флаг command_type. В зависимости от флага отправляет show или 
config комманду на роутер и возвращает вывод роутера.
"""

from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException
)

def send_command(device, command, command_type):
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            if command_type is False:
                output = ssh.send_command(command, strip_command=False)
            else:
                output = ssh.send_config_set(command, strip_command=False)
        return output
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)
