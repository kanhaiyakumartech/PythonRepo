def process_commands(the_list, commands):
    for cmd in commands:
        input_cmd = cmd.split()

        if input_cmd[0] == 'print':
            print(the_list)

        elif input_cmd[0] == 'insert':
            the_list.insert(int(input_cmd[1]), int(input_cmd[2]))

        elif input_cmd[0] == 'remove':
            the_list.remove(int(input_cmd[1]))

        elif input_cmd[0] == 'append':
            the_list.append(int(input_cmd[1]))

        elif input_cmd[0] == 'sort':
            the_list.sort()

        elif input_cmd[0] == 'pop':
            the_list.pop()

        elif input_cmd[0] == 'reverse':
            the_list.reverse()

    return the_list
