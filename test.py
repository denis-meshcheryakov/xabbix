import subprocess
import re
from pprint import pprint


ping = subprocess.run(['ping', '-i', '0.2', '-c', '100', '192.168.0.105'],
                      stdout=subprocess.PIPE, encoding='utf-8')
ping_result = str(ping.stdout)
# pprint(ping_result)
# ping_result = (r'/r/n').join(ping_result)
# print(ping_result)
#     return ping_result
perc_of_loss = re.search(r'.+ (\d+)% packet loss,.*', ping_result).group(1)
success_perc = str(100 - int(perc_of_loss)) + '%'
# print(result)
# perc_of_loss = int(perc_of_loss['sent']) * 100 / int(perc_of_loss['received'])
print(success_perc)


