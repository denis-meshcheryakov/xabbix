import yaml

with open("devices.yaml") as f:
    devices = yaml.safe_load(f)
for device in devices:
    # print(device)
    ip_addr = device['host']
    print(ip_addr)
