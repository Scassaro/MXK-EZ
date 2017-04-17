###############################################################
# Name: Test Helper                                                                                                          #
# Company: Dasan Zhone Solutions                                                                              #
# Author: Stephen Cassaro                                                                                               #
# Description: Automates boring tasks.                                                                          #
###############################################################

import paramiko
import sys
import time
import select
import string

# Choose which MXK to connect to (IP) [in beta]

#mxk = raw_input("What is the IP of the MXK you would like to connect to?: ")

# Set up SSHClient object

ssh = paramiko.SSHClient()

# This copies whatever host key policy the MXK you are connecting to uses

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Try to connect to the provided IP, throw error and quit if it fails.

try:
    ssh.connect('10.155.2.104', username = 'admin', password = 'zhone', port=22)
except paramiko.SSHException:
    print ("Connection Failed")
    quit()

# Create transport and open session

chan = ssh.get_transport().open_session()
#chan.settimeout(120)
#chan.set_combine_stderr(True)
chan.get_pty()

chan.exec_command('slots')






#chan.exec_command('slots')
#chan.invoke_shell()
#chan.send('dir')
#data = ""
#for x in range (0, 10):
  #  received = chan.recv(1024)
    #if len(received) == 0:
      #  sys.exit(3)
    #data += received.decode('utf-8')
    #sys.stdout.write(received.decode('utf-8'))
   # sys.stdout.flush()
#stdout = chan.makefile('r', -1)
#stdout_text = stdout.read()
#status = int(chan.recv_exit_status())

# Invoke_shell, store in buffer WIP

#buffer = ''
#shell = ssh.invoke_shell()
#shell.send('slots')
#response = shell.recv(9999)
#buffer += response.decode('utf-8')
#print(response)

# Exec_command WIP (line below throws errors and kills connection)

#stdin, stdout, stderr = ssh.exec_command("slots")
#print("dgfodsjodsj")
#print(stdout.channel.recv_exit_status())
#lines = stdout_.readlines();
#for line in lines:
   # print (line);

# Deallocate memory associated with the SSH session.
#shell.close()

#print(stdout_text)
ssh.close()
