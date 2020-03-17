import os
import requests

file = "sha_save.txt"
filecommit = "Commit_sha_and_commit_messages.txt"
myfilecommit = open(filecommit, mode='w', encoding='Latin_1')
os.system("git log --pretty=format:%H,%s >> Commit_sha_and_commit_messages.txt ")
myfile = open(file, mode='w', encoding='Latin_1')
os.system("git log --pretty=format:%H  >> sha_save.txt")
myfile = open(file, mode='r', encoding='Latin_1')
dir = os.path.basename(os.getcwd())
headers = {'Authorization': 'Basic QnVsZ2Frb3ZBbnRvbjpBa2FtZWdha2lsbDkw'}

for line in myfile:
    line = requests.get('https://api.github.com/repos/architecture-playground/' + dir.strip() +'/git/commits/' + line.strip(), headers=headers)
    print(line.text)
myfile.close()
os.system("rm -rf sha_save.txt")
