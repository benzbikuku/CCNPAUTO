import datetime

with open('show_commands.txt') as sh_cmd:
    commands = sh_cmd.readlines()
# time_seq_no_commands
print(commands)
now = datetime.datetime.now().replace(microsecond=0)
print(now)
for cmd in enumerate(commands, start=1):
    print(cmd)
    # print(str(cmd[0]).zfill(2))
    # print(cmd[1])#.replace(' ','_').strip())
    file_name = f"{str(now).replace(' ',':')}_{str(cmd[0]).zfill(2)}_{cmd[1].replace(' ','_').strip()}.txt"
    # print(file_name)
    # print(cmd[1])
    with open(file_name, 'a') as cmd_data:
        cmd_data.write(cmd[1])