import os
import yaml
from get_show_command_from_routers import (send_and_parse_show_command,
                                           send_and_parse_command_parallel)


def get_show_version_params(output):
    """
    Функция принимает от send_and_parse_command_parallel вывод команды
    show sh version со всех роутеров, отфильтровывает нужные значения
    и записывает в yaml-файлы для каждого из роутеров
    """
    for device, params in output.items():
        for list_item in params:
            list_name = str(device)
            device = {}
            for key, value in list_item.items():
                if 'HOSTNAME' in key or 'UPTIME' in key:
                    device[key] = value
                elif 'UPTIME' in key:
                    device[key] = value
                elif 'VERSION' in key:
                    device[key] = value
                elif 'RUNNING_IMAGE' in key:
                    device[key] = value
                elif 'RUNNING_IMAGE' in key:
                    device[key] = value
                elif 'HARDWARE' in key:
                    device[key] = value[0]
                elif 'SERIAL' in key:
                    device[key] = value[0]
            with open(list_name + '_inventory.yaml', 'w') as f:
                yaml.dump(device, f, default_flow_style=False)
    return device


def get_show_version_params_call():
    full_pth = os.path.join(os.getcwd(), 'templates')
    command = 'show version'
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    for device in devices:
        send_and_parse_show_command(device, command,
                                    template_path=full_pth)
    path_dir = f'{os.getcwd()}/templates'
    get_show_version_params(send_and_parse_command_parallel
                            (devices, command, path_dir))


if __name__ == "__main__":
    result = get_show_version_params_call()
