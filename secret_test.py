import os
import sys
import json
import tempfile
import stat
from git import Repo
from secret import main

clone_location = []
branches_name = []
exception_branch_name = []

GitAccessToken = "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"

#samples tested : 
    # https://github.com/ramitsurana/awesome-kubernetes.git
    # https://github.com/bytedance/flutter_ume.git
    # https://github.com/amirgamil/apollo.git
    # https://github.com/golang-jwt/jwt.git
    # https://github.com/apex/up.git
    # https://github.com/google/go-cloud.git
    # https://github.com/GitGuardian/sample_secrets.git
    # https://github.com/angristan/openvpn-install.git

# Trufflehog function to run trufflehog on every branches of git repo.
def trufflehog(url,branches):
    num = 1
    os.system(f"trufflehog --regex {url} --json > {branches}{num}.json")
    num = 2
    file = open(f"{branches}{num}.json", 'a')
    in_file = open(f'{branches}1.json', 'r').readlines()
    file.write("[")
    for line in in_file:
        if (line!=in_file[-1]):
            file.writelines(str(line) + ",")
        else:
            file.writelines(str(line))
    file.write("]")
    file.close()

    with open(f'{branches}2.json') as fp:
        data = json.load(fp)
    with open(f'truffle_output/{branches}.json', 'w') as f:
        json.dump(data, f, indent=4)

    # Number of lines in file.
    num_lines = sum(1 for line in open(f'{branches}2.json'))
    print("Branch Name:" + branches, "Number of lines:", num_lines - 1)
    # Delete the cloned repo temp file.
    rmtree(url)
    # remove extrafiles which were made at the start.
    os.remove(f'{branches}1.json')
    os.remove(f'{branches}2.json')

def clone_git_repo(git_url,branch= None):
    # Create temp file.
    project_path = tempfile.mkdtemp()
    if branch == None:
        # Clones the default branch so we can fetch all other branches
        repo = Repo.clone_from(git_url, project_path)
        # Get all branches
        active = repo.git.branch('-a')
        # String manipulation to get only branch name.
        branch = active.split('\n')
        for ele in branch[2:]:
            element = ele.split('origin')[-1]
            split_element = element.split("/", 1)
            # Append branch names to list 
            exception_branch_name.append(split_element[1])
        for branch_element in exception_branch_name:
            # Pass branches to clone_git_repo to clone branches
            clone_git_repo(git_url, branch=f"{branch_element}")
        for ele in branch[2:]:
            element = ele.split('/')[-1]
            branches_name.append(element)
    else:
        # All branches are cloned
        repo = Repo.clone_from(git_url, project_path, branch=f"{branch}")
        clone_location.append(project_path)
        print("Git cloned on this temp location:",project_path)
        print(branch)

def rmtree(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            # Change permissions for files
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            # Remove empty(temp) dir
            os.rmdir(os.path.join(root, name))
    os.rmdir(top) 

"""opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
if "-p" in opts:
    for arg in args:
        user = arg.split("/")[3]
        repo_name = arg.split("/")[4]    
clone_git_repo(f'https://{user}:{GitAccessToken}@github.com/{user}/{repo_name}')"""
clone_git_repo("https://github.com/GitGuardian/sample_secrets.git")
for tmp,truffle in zip(clone_location,branches_name):
    # Pass branch_name and cloned location of that branch
	main(tmp,truffle)
