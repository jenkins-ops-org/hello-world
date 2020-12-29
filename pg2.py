import argparse,shlex
import subprocess
import csv
from datetime import datetime


IP = "172.17.0.2"
PORT = "5432"
USER = "nik"
DB = "library"
PASS = "post7864"




def _log(data):
    now = datetime.now()
    name = now.strftime("%d-%m-%Y-%H-%M-%S")
    with open("%s.log"%name,"w+") as o:   
        o.write(data)
def execute_multi(mfile):
        tmp = open(mfile,"r")
        files = tmp.readlines()
        tmp.close()
        data = ""
        for file in files:
            file = file.replace("\n","")
#            print(file)
            data = data + execute_db(file)
        return(data)
def execute_db(sql_name):
    cmd = 'PGPASSWORD=%s psql -h %s -p %s -U %s -d %s -f "%s"'%(PASS,IP,PORT,USER,DB,sql_name) 
    p = subprocess.Popen(cmd.replace("\n",""),stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
    out, err = p.communicate()
    print(out.decode('ascii'))
    return(out.decode('ascii'))





def main():
     parser = argparse.ArgumentParser()
     parser.add_argument("-a")
     #parser.add_argument("-i")
     parser.add_argument("-f")
     parser.add_argument("-m")
     args = parser.parse_args()
     if (args.a == "query") and (args.f is not None) and (args.m is None):
               data = execute_db(args.f)
               _log(data)
     elif (args.a == "query") and (args.f is None) and (args.m is not None):
               data = execute_multi(args.m)
               _log(data)
if __name__ == "__main__":
    main()






