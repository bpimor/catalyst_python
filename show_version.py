from genie.testbed import load
from tabulate import tabulate

testbed = load('testbed.yaml')
data = []

for device in testbed.devices:
    host = testbed.devices[device]
    host.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False)

    show_version = host.parse('show version')['version'] 
    version = show_version['version']
    os_device = show_version['os']
    chassis = show_version['chassis']
    hostname = show_version['hostname']


    value = (hostname, chassis, os_device, version)
    data.append(value)
    host.disconnect()
my_headers = ["Hostname", "Model", "OS", "Version"]
print(tabulate(data, headers=my_headers, tablefmt="grid"))
