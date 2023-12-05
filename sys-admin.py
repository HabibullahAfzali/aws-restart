#Introducing System Administration with Python

#Exercise 1: Using os.system

import os # it import os module 
import subprocess # it imports subprocess module

os.system("ls")

#Exercise 2: Using subprocess.run

subprocess.run(["ls"])

#Exercise 3: Using subprocess.run with two arguments

subprocess.run(["ls","-l"])

#Exercise 4: Using subprocess.run with three arguments

subprocess.run(["ls","-l","README.md"])

#Exercise 5: Retrieving system information
# uname will retrieve the system information, it also accepts parameter/ arguments like -a in this example 

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])


#--------------Exercise 6: Retrieving information about disk space-------

# Display information about active processes using the ps command with -x argument
print("\nBelow process information retrieved using ps command:")
command = "ps"
command_argument = "-e"
print(f'Gathering active process information with command: {command} {command_argument}')
subprocess.run([command, command_argument])

# Display disk space information
print("Below disk information retrieved using df command:")
subprocess.run(["df", "-h"])  # Use -h for human-readable format