# show_output = '''\
#  GigabitEthernet1       192.168.0.63    YES NVRAM  up                    up
#  GigabitEthernet2       unassigned      YES NVRAM  up                    up
#  GigabitEthernet3       unassigned      YES NVRAM  up                    up
#  GigabitEthernet4       unassigned      YES NVRAM  up                    up
#  Loopback1001           10.1.1.100      YES manual up                    up
#  Loopback1002           20.1.1.100      YES manual up                    up
#  '''
# #
# intf_lines = show_output.splitlines()
# # print(intf_lines)

# for intf in intf_lines:
    
#     #   print(intf)
#         intf_details = intf.split()
#         if intf_details != []:
#             # print(intf_details)
#             # print(intf_details[1])
        
        

#             if intf_details[1] != 'unassigned':
    
#                 print(f"Interface Name: {intf_details[0]} Interface IP {intf_details[1]}") 

#  
#######################################################
with open('../Paramiko/Paramiko/192.168.1.22') as text:
    lines = text.readlines()
    print(lines)
    print("Press Enter.., end='")
    for line in lines:
        if input() == '':
            line = line.strip('\n')
            print(line, end='')
    print("Completed")