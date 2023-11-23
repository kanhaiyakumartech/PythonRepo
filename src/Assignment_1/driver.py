#here i impore our code in util file and call the method process_commands
from util import process_commands
#Here we are taking N variable to taking Number to command lines/operations.
N = int(input("Enter the NUmber To Perform How many operations : "))
# No we Create a List for storing a elements and i gaves the name as "My_list".
My_List = []
commands = []
# Here i using for loop for iterating the N (Command Lines)
for _ in range(N):
# In side for loop we are taking input for command lines
    input_cmd = input()
    commands.append(input_cmd)

process_commands(My_List, commands)
