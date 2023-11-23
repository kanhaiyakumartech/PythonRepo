#Basically in this question we have to create a list and do some operation like insert append remove---
def process_commands(My_List, commands):
# Here  i definrd a function
    for cmd in commands:
        input_cmd = cmd.split()
# After that i am  using  if and elif conditions to identify the command.

        if input_cmd[0] == 'print':
#At the last command gets identified an operation is performed.
            print(My_List)

        elif input_cmd[0] == 'insert':
            My_List.insert(int(input_cmd[1]), int(input_cmd[2]))

        elif input_cmd[0] == 'remove':
            My_List.remove(int(input_cmd[1]))

        elif input_cmd[0] == 'append':
            My_List.append(int(input_cmd[1]))

        elif input_cmd[0] == 'sort':
            My_List.sort()

        elif input_cmd[0] == 'pop':
            My_List.pop()

        elif input_cmd[0] == 'reverse':
            My_List.reverse()

    return My_List
