import requests
import json
import pandas as pd
'''
@Author:Josh
This is a simply code to find ip location 
'''


def is_json(myjson):
    try:
        json.loads(myjson)
        print ("this is json")
    except ValueError as e:
        return False
    return True


def write_csvfile(response): # write file output csv
    df = pd.DataFrame(data=response, index=[0])
    print(df)
    df.to_csv(r'iplocation.csv', mode='a', header=False)

def read_iplocation_api(ip_list): # query ip to iplocation api
    api = "https://api.iplocation.net/?ip="
    url = api + ip_list
    response = requests.get(url).json()
    write_csvfile(response)

def read_iplist(): # read ip list
    path = 'list.txt'
    with open(path) as f:
        linelist = f.readlines()
        for ip_list in range(len(linelist)):
            linelist[ip_list] = linelist[ip_list].strip()
            read_iplocation_api(linelist[ip_list])

if __name__ == '__main__':
    read_iplist()












