from paramiko import  RSAKey
from deviceconfig import cisco_cmd_executor


router_name = "Copp_R1.ant.amazon.com"

with open("/home/benz/ENTAUTO/CCNPAUTO/Paramiko/Paramiko/192.168.1.22", 'r') as conf_file:
    csr_command = conf_file.readlines()
    print(csr_command)
    
    # cisco_cmd_executor(cmd=csr_command, hostname=router_name)