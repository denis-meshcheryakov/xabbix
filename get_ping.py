import subprocess
import re
from datetime import datetime
import yaml
import schedule
import time


def get_ping(ip_addr):
    """
    Функция пингует роутер и возврыщает резултат в виде строки
    """
    ping = subprocess.run(['ping', '-n', '3', ip_addr],
                          stdout=subprocess.PIPE, encoding='utf-8')
    ping_result = str(ping.stdout)
    return ping_result


def get_loss_perc(ping_result):
    """
    Функция принимает резултат работы функции get_ping, получает из него
    процент потерь и
    конвертирует в процент успешно полученных пакетов
    """
    perc_of_loss = re.search(r'.+ \((\d+)% .*', ping_result).group(1)
    success_perc = str(100 - int(perc_of_loss)) + '%'
    print(success_perc)
    return success_perc


def get_ping_rslt_dict(success_perc):
    """
    Функция создает словать где ключ- текущие дата/время, а значение
    резултат работы функции get_loss_proc. Затем добавляет результат
    в файл success_packet_perc.yaml
    """
    to_yaml_file = {}
    dt_now = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    to_yaml_file[dt_now] = success_perc
    with open(ip_addr + '_success_packet_perc.yaml', 'a') as f:
        yaml.dump(to_yaml_file, f, default_flow_style=False)
    return to_yaml_file


if __name__ == '__main__':
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for device in devices:
        ip_addr = device['host']
        success_packet_perc = get_loss_perc(get_ping(ip_addr))
        result_dict = get_ping_rslt_dict(success_packet_perc)

    # schedule.every(5).seconds.do(get_ping_rslt_dict, name=success_packet_perc)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
