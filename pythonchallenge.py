import json
import requests
import csv
from threading import Thread
from time import perf_counter

user = "xxx"
passw = "xxx"
platform_base_url = "xxx"
repo_name = "libs-release-local"
params = {'user':user, 'passw':passw,'api':'no','list':'','deep':'1'}
string_to_find = "This is a short story !"
final_lst = []
f = open('stories.csv', 'w')

def generateToken(func):
    def inner():
        InitialGetToken = requests.post(url=f'{platform_base_url}/artifactory/api/security/token',auth=(user, passw),data={"username":user, "expires_in": 5, "refreshable": True})
        InitialGetTokenJson = InitialGetToken.json()
        global access_token; access_token = InitialGetTokenJson['access_token']
        print("Generating token..")
        return func()
    return inner

@generateToken
def retrieveUri():
    initialGetRequest = requests.get(url=f'{platform_base_url}/artifactory/api/storage/{repo_name}',params=params,auth=(user, access_token))
    initialGetResponse = initialGetRequest.json()
    uri_list = [x['uri'] for x in initialGetResponse['files'] if x['size'] < 80000]
    return uri_list

def getStoryIntoCsv(listOfUris, story):
    try:
        GetContentOfFile = requests.get(url=f'{platform_base_url}/artifactory/{repo_name}{story}',headers={"Authorization":f"Bearer {access_token}"},stream=True)
        if GetContentOfFile.status_code == 200:
            ContentOfFile = GetContentOfFile.iter_content(chunk_size=len(string_to_find))
            for content in ContentOfFile:
                if string_to_find in content.decode():
                    final_lst.append(f'\"{platform_base_url}{story}\" | \"{repr(GetContentOfFile.content.decode())}\"\n')
                else:
                    break
    except Exception:
        pass

def main():
    f.write(f'File Name, Story Txt (without the title)\n')
    listOfUris = retrieveUri()
    
    threads = [Thread(target=getStoryIntoCsv, args=(listOfUris, i)) for i in listOfUris]  
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    for i in final_lst[::-1]:
        if "Nothing" in i:
            f.write(i)

if __name__ == "__main__":
    start_time = perf_counter()
    main()
    end_time = perf_counter()
    print("*                  *                 *")
    print(f'It took {end_time-start_time: 0.4f} second(s) to complete.')
    print("*                  *                 *")
