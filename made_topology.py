import os
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
import yaml
from textfsm import clitable
from concurrent.futures import ThreadPoolExecutor
from draw_network_graph import draw_topology


def parse_command_dynamic(
        command_output, attributes_dict, index_file='index',
        templ_path='templates'):
    """Функция возвращает список словарей с результатами
       обработки вывода команды"""
    cli_table = clitable.CliTable(index_file, templ_path)
    cli_table.ParseCmd(command_output, attributes_dict)
    return [dict(zip(cli_table.header, row)) for row in cli_table]


def send_and_parse_show_command(device_dict, command,
                                template_path, index='index'):
    """Функция подключаться к одному устройству, отправлять команду show с помощью
       netmiko, а затем парсит вывод команды с помощью TextFSM."""
    attributes = {'Command': command, 'Vendor': device_dict['device_type']}
    try:
        with ConnectHandler(**device_dict) as ssh:
            ssh.enable()
            device_name = ssh.find_prompt()
            output = ssh.send_command(command, strip_prompt=False,
                                      strip_command=False)
            output = device_name + output
            parsed_data = parse_command_dynamic(
                output, attributes, templ_path=template_path, index_file=index
            )
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)
    return parsed_data


def send_and_parse_command_parallel(devices, command, templates_path, limit=3):
    """
    Функция send_and_parse_command_parallel запускает в
    параллельных потоках функцию send_and_parse_show_command
    """
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result_all = [
            executor.submit(send_and_parse_show_command,
                            device, command, templates_path)
            for device in devices
        ]
        output = {device['host']: f.result() for device,
                  f in zip(devices, result_all)}
    return output


def get_connect_dict(output):
    """
    Функция принимает от send_and_parse_command_parallelвывод команды
    show cdp neighbors deteil со всех роутеров, отфильтровывает повторяющиеся
    соединения и возвращает словарь в том формате,
    который необходим функции draw_topology.

    """
    nei_dict = output
    connect_dict = {}
    for key, value in nei_dict.items():
        for i in value:
            if not (i['DEST_HOST'], i['REMOTE_PORT']) in connect_dict:
                connect_dict[i['LOCAL_HOST'],
                             i['LOCAL_PORT']] = (i['DEST_HOST'],
                                                 i['REMOTE_PORT'])
    # print(connect_dict)
    draw_topology(connect_dict)
    return connect_dict


def funcs_calls():
    full_pth = os.path.join(os.getcwd(), 'templates')
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    for device in devices:
        send_and_parse_show_command(device, 'sh cdp neighbors det',
                                    template_path=full_pth)
    command = 'show cdp neighbors det'
    path_dir = f'{os.getcwd()}/templates'
    command = 'show cdp neighbors det'
    get_connect_dict(send_and_parse_command_parallel
                     (devices, command, path_dir))


if __name__ == "__main__":
    result = funcs_calls()
