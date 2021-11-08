import os
import yaml

from send_and_parse_cmd_parallel import send_and_parse_command_parallel
from draw_network_graph import draw_topology


def get_connect_dict(output):
    """
    Функция принимает от send_and_parse_command_parallel вывод команды show cdp neighbors deteil
    со всех роутеров, отфильтровывает повторяющиеся соединения и возвращает словарь в том формате,
    который необходим функции draw_topology.

    """
    nei_dict = output
    connect_dict = {}
    for key, value  in nei_dict.items():
        for i in value:
            if not (i['DEST_HOST'], i['REMOTE_PORT']) in connect_dict:
                connect_dict[i['LOCAL_HOST'], i['LOCAL_PORT']] = (i['DEST_HOST'], i['REMOTE_PORT'])
    return connect_dict 


if __name__ == '__main__':
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    command = 'show cdp neighbors det'
    path_dir = f'{os.getcwd()}/templates'
    connect_dict = get_connect_dict(send_and_parse_command_parallel(devices, command, path_dir))
    draw_topology(connect_dict)
