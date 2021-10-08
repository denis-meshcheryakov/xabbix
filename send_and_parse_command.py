"""
Функция подключаться к одному устройству, отправлять команду show с помощью netmiko,
а затем парсит вывод команды с помощью TextFSM.

Функция возвращает список словарей с результатами обработки вывода команды:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"
"""

import os
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
import yaml
from parse_command import parse_command_dynamic


def send_and_parse_show_command(device_dict, command, template_path, index='index'):
    attributes = {'Command': command, 'Vendor': device_dict['device_type']}
    try:
        with ConnectHandler(**device_dict) as ssh:
            ssh.enable()
            output = ssh.send_command(command)
            parsed_data = parse_command_dynamic(
                output, attributes, templ_path=template_path, index_file=index
            )
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)
    return parsed_data
