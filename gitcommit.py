import os

commitsInfoFileName = "commit_sha_and_commit_messages.txt"
os.system("git log --pretty=format:%H,%s >> " + commitsInfoFileName)

commitInfoFile = open(commitsInfoFileName, mode='r', encoding='UTF-8')

for fileLine in commitInfoFile :
    print(fileLine.strip())

os.system("rm -rf " + commitsInfoFileName)
