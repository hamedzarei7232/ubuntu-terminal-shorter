import os
from socket import gethostname
hostname = gethostname()
username = os.environ['USER']
pwd = os.getcwd()
homedir = os.path.expanduser('~')
pwd = pwd.replace(homedir, '~', 1)
#if len(pwd) > 33:
#    pwd = pwd[:10] # first 10 chars+last 20 chars
#print("[%s@%s:%s]"%(username, hostname, pwd))
pwd = str.split(pwd, '/')[-1]
print("[%s@local: %s]# "%(username, pwd))
