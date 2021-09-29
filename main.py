import os
import sys
import json
import tempfile
import stat
import requests
from git import Repo

GitAccessToken = "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"

#sample repos for trufflehog scan--
    # url =  "https://github.com/dxa4481/truffleHog.git"
    # url = "https://github.com/shubhamanand43/Applied_AI_Course_Notes.git"
    # url = "https://github.com/GitGuardian/sample_secrets.git"
    # url = "https://github.com/facebook/flipper.git"
    # url = "https://github.com/facebook/bistro.git"

def trufflehog(url):
    os.system(f"trufflehog --regex {url} --json > x.json")

    file = open("b.json", 'a')
    file.write("[")
    in_file = open('x.json', 'r').readlines()
    num = 1
    for line in in_file:
        if (line!=in_file[-1]):
            file.writelines(str(line) + ",\n")
            num = num + 1
        else:
            file.writelines(str(line))
            num = num + 1
    file.write("]")
    file.close()
    with open('b.json') as fp:
        data = json.load(fp)
    with open('c.json', 'w') as f:
        json.dump(data, f, indent=4)

def clone_git_repo(git_url,branch= None):
    project_path = tempfile.mkdtemp()
    if branch == None:
        repo = Repo.clone_from(git_url, project_path, branch=f"{branch}")
        print("Git cloned on this temp location:",project_path)
        branches = repo.remotes.origin.fetch()
        repo_branch_names = [remote_branch.name for remote_branch in branches]
        print(repo_branch_names)
        for ele in repo_branch_names[1:]:
                branch_ele= ele.split('/')[-1]
                clone_git_repo(r'https://github.com/SagarJ17/LSA.git',branch=f"{branch_ele}")
    else:
        repo = Repo.clone_from(git_url, project_path, branch=f"{branch}")
        print("Git cloned on this temp location:",project_path)

    return project_path

def branch(branch_name):
    print(branch_name + "done")
    access_token = "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"
    headers = {'Authorization': f'token {access_token}', 
            'Content-Type':'application/json'}
    data={"name":"LSA", "default_branch": f"{branch_name}"}
    owner = "SagarJ17"
    repo_name = "LSA"
    url = f"https://api.github.com/repos/{owner}/{repo_name}"
    requests.patch(url, data=json.dumps(data), headers=headers)
    path = clone_git_repo('https://github.com/SagarJ17/LSA.git')
    trufflehog(path)

def rmtree(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(top) 
    
#rmtree(r'C:\Users\sagar\AppData\Local\Temp\tmpbz8s0lzj')
    #clone_git_repo(r'https://github.com/SagarJ17/LSA.git')
    #path = clone_git_repo('https://github.com/GitGuardian/sample_secrets.git')
    #trufflehog(r'C:\Users\sagar\OneDrive\Desktop\truffle\LSA')

trufflehog(r'https://github.com/apex/up.git')

# Access private git repos with Access token:
# write the url in following format: 
# https://{username}:{GitAccessToken}@github.com/{username}/repo_name.git
#clone_git_repo(f'https://rajat-9-6:{GitAccessToken}@github.com/rajat-9-6/Salary_Prediction.git')


"""opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
if "-p" in opts:
    for arg in args:
        user = arg.split("/")[3]
        repo_name = arg.split("/")[4]"""