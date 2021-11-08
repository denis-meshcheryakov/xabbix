import subprocess
import re
from datetime import datetime
import yaml
import schedule
# from schedule import every, repeat, run_pending
import time


def get_ping(ip_addr):
    """
    Функция пингует роутер и возврыщает резултат в виде строки
    """
    ping = subprocess.run(['ping', '-i', '0.2', '-c', '10', ip_addr],
                          stdout=subprocess.PIPE, encoding='utf-8')
    ping_result = str(ping.stdout)
    # print(ping_result)
    # return ping_result


# def get_loss_perc(ping_result):
    """
    Функция принимает резултат работы функции get_ping, получает из него
    процент потерь и
    конвертирует в процент успешно полученных пакетов
    """
    perc_of_loss = re.search(r'.+ (\d+)% packet loss,.*', ping_result).group(1)
    success_perc = str(100 - int(perc_of_loss)) + '%'
    print(ip_addr)
    print(success_perc)
    return success_perc


# # @repeat(every(10).seconds)
def get_ping_rslt_dict(success_perc):
    """
    Функция создает словать где ключ- текущие дата/время, а значение
    резултат работы функции get_loss_proc. Затем добавляет результат
    в файл success_packet_perc.yaml
    """
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
        ping_result = get_ping(ip_addr)
        # success_perc = get_loss_perc(ping_result)
        # print(success_packet_perc)
        result_dict = get_ping_rslt_dict(ping_result)

        # schedule.every(15).seconds.do(get_ping, ip_addr=ip_addr)
        # # schedule.every(20).seconds.do(get_loss_perc, get_ping)
        schedule.every(20).seconds.do(get_ping_rslt_dict, ping_result)
    while True:
        schedule.run_pending()
        time.sleep(1)
