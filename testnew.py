import re
import os
import json
from git import Repo

#https://github.com/GitGuardian/sample_secrets.git

#main(r"C:\Users\sagar\AppData\Local\Temp\tmpj6skycmv","feature_branch")

#print(os.environ)

#os.environ['GitAccessToken'] = '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'

#os.environ["GitAccessToken"] = "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"

"""if os.stat("Git_access.txt").st_size == 0:
    print("add git access token for private repo")
    access_token = input("Add token:")
    with open("Git_access.txt","w") as f:
        f.write(access_token)
        f.close()
else:
    with open("Git_access.txt","r") as f:
        print(f.readlines())
"""
#f = open(r"C:\Users\sagar\OneDrive\Desktop\truffle\cloned\bucket_s3.py", 'r').readlines()
#srv://testuser:hub24aoeu@gg-is-awesome-gg273.mongodb.net/test?retryWrites=true&w=majority

file_lang = open(r'secret_scanner\secret_output\feature_branch.json', 'r') # contains extensions for languages
languages = json.load(file_lang)
data = []
start = []
for lang in languages:
    if "High Entropy" == lang["reason"]:
        string = lang["stringsFound"]
        data.append(string[-1])
        data.append(string[1])
        f = open(r"C:\Users\sagar\OneDrive\Desktop\truffle\cloned\shared_key.rsa", "r")
        for number,line in enumerate(f):
            for strings in data:
                for match in re.finditer(strings, line):
                    start.append(number + 1)
        
print(start)                   
           