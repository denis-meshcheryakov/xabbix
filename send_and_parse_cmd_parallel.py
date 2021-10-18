"""
Функция send_and_parse_command_parallel запускает в 
параллельных потоках функцию send_and_parse_show_command 
"""

from send_and_parse_command import send_and_parse_show_command
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
import os
import yaml


def send_and_parse_command_parallel(devices, command, templates_path, limit=3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result_all = [
            executor.submit(send_and_parse_show_command, device, command, templates_path)
            for device in devices
        ]
        output = {device['host']: f.result() for device, f in zip(devices, result_all)}
    return output


if __name__ == "__main__":
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    command = 'show cdp neighbors detail'
    path_dir = f'{os.getcwd()}/templates'
    pprint(send_and_parse_command_parallel(devices, command, path_dir))
