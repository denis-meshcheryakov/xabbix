from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
from textfsm import clitable
from concurrent.futures import ThreadPoolExecutor


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
        return parsed_data
    except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
        print(error)


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
