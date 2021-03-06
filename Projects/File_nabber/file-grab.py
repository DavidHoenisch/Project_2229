#!/usr/bin/env python3

# This file is intended to grab files from remote server that have been comprimised.  
# From your SIEM create a csv file of all the files that were created by the attacker, filter our all the clean ones
# leaving you with the malicious ones, and feed that into file-grab

import optparse
import csv 
import time
from paramiko import AutoAddPolicy, SSHClient
from scp import SCPClient
import sys 

def welcome():
    print("[+] File-Nabber version. 0.0.1 ")
    print("[+] use file-grab.py --help to view options")
    print("===========================================")
    time.sleep(.2)

def main(FILE, DESTINATION, OUT, ssh, host_key, no_key, connect, scp_client):
    with open('grab-files.csv') as read_object:
        csv_reader = csv.DictReader(read_object)
        path = []
        for row in csv_reader:
            path.append(row['PATH'])
        for item in path:
            scp_client.get(item)

parser = optparse.OptionParser()
parser.add_option("-f", "--file", dest="FILE", type="str", help="Specify CSV file to read from")
parser.add_option("-d", "--destination", dest="DESTINATION", type="str", help="Specify destiniation host")
parser.add_option("-o", "--output", dest="OUT", type="str", help="Specify where to save files that are downloaded")
(options, arguments) = parser.parse_args()

ssh = SSHClient()
host_key = ssh.load_system_host_keys()
no_key = ssh.set_missing_host_key_policy(AutoAddPolicy())
connect = ssh.connect(options.DESTINATION, username='root', password='YOUR-PASSWORD-HERE')
scp_client = SCPClient(ssh.get_transport())

welcome()
main(options.FILE, options.DESTINATION, options.OUT, ssh, host_key, no_key, connect, scp_client)
scp_client.close()



# FUTURE OBJECTIVES

# 1. SSH Key support
# 2. Better error handling
# 3. Progress tracker to show download progress 
# 4. Hashing Functionality to establish basic forensics baseline
# 5. Integration with Cuckoo Sandbox.  






