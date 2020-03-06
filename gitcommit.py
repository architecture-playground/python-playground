import requests

hashs = ['86ab2b620dc527bf4e0194313dee4f583fa50876', '2f6a54fec7f8dfbf4c0bc87aa55af9c42974d00d', '017263336b94a80fdf2243ccbba46be17a93a92a', 'ee7b8e98ed43a49bf9ada79352aa94ee62043c8a']
for x in hashs:
    x = requests.get('https://api.github.com/repos/architecture-playground/playground-service/git/commits/'+ str(x))
    print(x.text)


