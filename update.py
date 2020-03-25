#python update.py -a update -r us-east-1 -s test-service-5 -c connector-clus -i 758637906269.dkr.ecr.us-east-1.amazonaws.com/connector-dev:tom -dc 1 -l  https://37mwxnme44.execute-api.us-east-1.amazonaws.com/ecs/


import requests
import argparse
import json







def update_ecs(ac,reg,svc,clus,img,dc,url): 
    body = {
             "action": ac,
             "region": reg,
             "service": svc,
             "cluster": clus,
             "image":  img,
             "desiredCount": int(dc)
             }
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url,headers=headers,json=body)
    data=json.loads(r.text)
    print(data)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a")
    parser.add_argument("-r")
    parser.add_argument("-s")
    parser.add_argument("-c")
    parser.add_argument("-i")
    parser.add_argument("-d")
    parser.add_argument("-l")
    args = parser.parse_args()

    if (args.a is not None) and (args.a in ["update"]): 
       if args.a == "update":
           update_ecs(args.a,args.r, args.s, args.c, args.i, args.d,args.l)
       else:
            print("Error")
            return None
    else:
        print("kindly parse correct key")
        return None

if __name__ == "__main__":
    main()      
       

#python update.py -a update -r us-east-1 -s test-service-5 -c connector-clus -i 758637906269.dkr.ecr.us-east-1.amazonaws.com/connector-dev:tom -dc 1 -l  https://37mwxnme44.execute-api.us-east-1.amazonaws.com/ecs/
