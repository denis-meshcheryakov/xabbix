import subprocess
import re
from datetime import datetime
import yaml
import schedule
import time


def get_ping_rslt_dict(ip_addr):
    """
    Функция пингует роутер и возврыщает резултат в виде строки.
    Конвертирует в процент успешно полученных пакетов.
    Создает словать где ключ- текущие дата/время, а значение
    резултат работы функции get_loss_proc. Затем добавляет результат
    в файл ip-address-роутера_success_packet_perc.yaml
    Функция вызывается по расписанию.
    """
    ping = subprocess.run(['ping', '-i', '0.2', '-c', '10', ip_addr],
                          stdout=subprocess.PIPE, encoding='utf-8')
    ping_result = str(ping.stdout)
    perc_of_loss = re.search(r'.+ (\d+)% packet loss,.*', ping_result).group(1)
    success_perc = str(100 - int(perc_of_loss)) + '%'
    print(ip_addr)
    print(success_perc)
    to_yaml_file = {}
    dt_now = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    print(dt_now)
    to_yaml_file[dt_now] = success_perc
    with open(ip_addr + '_success_packet_perc.yaml', 'a') as f:
        yaml.dump(to_yaml_file, f, default_flow_style=False)
    return to_yaml_file


if __name__ == '__main__':
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for device in devices:
        ip_addr = device['host']
        schedule.every(20).seconds.do(get_ping_rslt_dict, ip_addr)
    while True:
        schedule.run_pending()
        time.sleep(1)
