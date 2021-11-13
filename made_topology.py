import os
import yaml
from draw_network_graph import draw_topology

from get_show_command_from_routers import (send_and_parse_show_command,
                                           send_and_parse_command_parallel)


def get_connect_dict(output):
    """
    Функция принимает от send_and_parse_command_parallel вывод команды
    show cdp neighbors deteil со всех роутеров, отфильтровывает повторяющиеся
    соединения и возвращает словарь в том формате,
    который необходим функции draw_topology.

    """
    connect_dict = {}
    for key, value in output.items():
        try:
            for i in value:
                if not (i['DEST_HOST'], i['REMOTE_PORT']) in connect_dict:
                    connect_dict[i['LOCAL_HOST'],
                                 i['LOCAL_PORT']] = (i['DEST_HOST'],
                                                     i['REMOTE_PORT'])
        except (TypeError) as error:
            print(error)
    draw_topology(connect_dict)
    return connect_dict


def get_connect_dict_call():
    full_pth = os.path.join(os.getcwd(), 'templates')
    command = 'show cdp neighbors det'
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    for device in devices:
        send_and_parse_show_command(device, command,
                                    template_path=full_pth)
    path_dir = f'{os.getcwd()}/templates'
    get_connect_dict(send_and_parse_command_parallel
                     (devices, command, path_dir))


if __name__ == "__main__":
    result = get_connect_dict_call()
