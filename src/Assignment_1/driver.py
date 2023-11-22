from util import process_commands

N = int(input())
the_list = []
commands = []

for _ in range(N):
    input_cmd = input()
    commands.append(input_cmd)

process_commands(the_list, commands)
