from time import sleep
from turtle import color

#TODO
#  design a modular file System
#


# colors
class COLOR:
    red = '\033[31m'
    white = '\033[37m'
    green = '\033[32m'


# Tuple Variables
local_user = ("local")
local_machine = ("localmachine")
local_ip = ("56.65.137.128")
root_user = ("root")

# variables for what Computer/ip address you are connected to
connected_ip = local_ip
connected_user = local_user
connected_machine = local_machine

active_directory = "home"

#Indexes info for remote machines
remote_ip = []
remote_machine = []
remote_user = []
remote_pass = []
root_pass = []


class RemoteHost():
    # collectes and assign the Remote user data to the appriate variables
    def __init__(self, username, password, root_password, ip_address, machine):

        # Adds user informaton to the appropriate global lists
        remote_ip.append(ip_address)
        remote_user.append(username)
        remote_pass.append(password)
        remote_machine.append(machine)
        root_pass.append(root_password)

        # file system
        self.files = []
        self.file_contents = []
        self.email = []
        self.email_contents = []
        self.bin = []
        self.logs = []

        # Network Defence
        self.proxy = []
        self.firewall = []

        # Network Ports
        self.port21 = []
        self.port22 = []
        self.port25 = []
        self.port80 = []
        self.port1433 = []


# Remote Machines
google = RemoteHost("greg", "password", "toor", "10.10.10.10", "google")
google.files = ["new.txt"]
google.file_contents = ["this is a test"]

amazon = RemoteHost("bob", "kittens", "admin", "11.11.11.11", "amazon")

print("""
      |'-______-'|
      | __    __ |
     / /  |  |  \ \   
     \/ O /  \ O \/
      \  / == \  / 
       ''--__--''  
---------------------------
Booting RakoonOS Kernal 2.0
---------------------------\n""")
sleep(2)

print(COLOR.red + 'Input "help" for available commands\n')

while True:

    # Creates Command Imput
    cmd = input(COLOR.white + "\n" + connected_user + "@" + connected_machine +
                ":~$ ")
    cmd = cmd.split()

    # Help Command
    if cmd[0].lower() == "help":
        # print("\nexit\nTerminates The Kernal.\n")
        print(
            "\n[ping]\nChecks for Connection with the Specified Ip.\nExample: Ping 10.10.10.10"
        )
        print("\n[ipconfig]\nLists the ip of the current connected machine\n")
        print(
            "\n[connect]\nChecks for Connection with the Specified Ip.\nExample: connect 10.10.10.10"
        )
        print("\n[quit]\nDissconnectes from the remote machine.\n")
        print("\n[whoami]\nDisplays the Name of the current user.\n")
        print("\n[help]\nDisplays available commands.\n")
        continue

    #Ping Command
    if cmd[0].lower() == "ping":
        # checks if Local Ip
        if len(cmd) >= 2 and cmd[1].lower() in connected_ip:
            print("\nPinging " + cmd[1] + " with 32 bytes of data:")
            for x in range(3):
                print("Reply from " + cmd[1] + ": bytes=32 time<1ms TTL=128")
                sleep(1)
            print(
                COLOR.green + "\nPing statistics for " + cmd[1] +
                ":\n   Packets: Sent = 3, Received = 3, Lost = 0 (0% loss),\nApproximate round trip times in milli-seconds:\n    Minimum = 0ms, Maximum = 1ms, Average = 0ms"
            )
            continue
        #checks if remote Ip
        if len(cmd) >= 2 and cmd[1].lower() in remote_ip:
            print("\nPinging " + cmd[1] + " with 32 bytes of data:")
            for x in range(3):
                print("Reply from " + cmd[1] + ": bytes=32 time<1ms TTL=128")
                sleep(1)
            print(
                COLOR.green + "\nPing statistics for " + cmd[1] +
                ":\n   Packets: Sent = 3, Received = 3, Lost = 0 (0% loss),\nApproximate round trip times in milli-seconds:\n    Minimum = 0ms, Maximum = 1ms, Average = 0ms"
            )
            continue
        # Checks for 3 decmals
        elif len(cmd) >= 2 and cmd[1].count(".") == 3:
            print("\nPinging " + cmd[1] + " with 32 bytes of data:")
            for x in range(3):
                print(F"Reply from " + cmd[1] +
                      ": Destination host unreachable.")
                sleep(1)

            print(COLOR.red + "\nPing statistics for " + cmd[1] +
                  ":\n   Packets: Sent = 3, Received = 0, Lost = 3 (0% loss)")
            continue
        else:
            print(COLOR.red + "Ping request could not find host " + cmd[1] +
                  ". Please check the name and try again. ")
            continue

    # whoami Command
    if cmd[0].lower() == "whoami":
        print("\n" + connected_user)
        continue

    # Ipconfig Command
    if cmd[0].lower() == "ipconfig":
        print("\n" + "Your Ip Address Is " + connected_ip)
        continue

    # Connect Command
    if cmd[0] == "connect":
        #checks if Local Ip
        if len(cmd) >= 2 and cmd[1] in connected_ip:
            print(COLOR.red + "\nCan Not connect Local Address " + cmd[1])
            continue
        #checks if remote Ip
        elif len(cmd) >= 2 and cmd[1] in remote_ip:
            login_user = input("enter username: ")
            login_pass = input("enter Password: ")
            # checks of login is root
            if login_user == root_user and login_pass == root_pass[
                    remote_ip.index(cmd[1])]:
                print(cmd[1] + " connected")
                connected_ip = cmd[1]
                connected_machine = remote_machine[remote_ip.index(cmd[1])]
                connected_user = root_user
                continue
            # checks if login is other user
            elif login_user == remote_user[remote_ip.index(
                    cmd[1])] and login_pass == remote_pass[remote_ip.index(
                        cmd[1])]:
                print(cmd[1] + " connected")
                connected_ip = cmd[1]
                connected_machine = remote_machine[remote_ip.index(cmd[1])]
                connected_user = remote_user[remote_ip.index(cmd[1])]
                continue
            else:
                # if login not valid
                print("incorrect login")
                continue
        # Checks for 3 decmals
        elif len(cmd) >= 2 and cmd[1].count(".") == 3:
            print(COLOR.red + cmd[1] + " not connected")
            continue
        else:
            print(COLOR.red + "\nIp Address Not Specified")
            continue

    # Dissconnect from Remote Ip
    if cmd[0].lower() == "exit":
        if connected_ip == local_ip[0]:
            print(COLOR.red + "Can Not Dissconect From Local User")
        else:
            print("Disconnected from " + connected_ip)
            connected_ip = local_ip[0]
            connected_user = local_user
            connected_machine = local_machine
            continue

# nmap Command

# ls command
    if cmd[0].lower() == "ls":

        print()

# cat command

# mail command

# ftp connect

# ssh connect command

# scp command

    else:
        print(COLOR.red + "\nInvalid Command")
        continue

# while connected_ip == remote_ip[0]:
