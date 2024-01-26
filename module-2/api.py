import requests
url="https://restcountries.com/v3.1/all"

req=requests.get(url)
data=req.json()
j=1
for i in data:

    print(f"{j} contary : {i['name']['official']}")
    print(f" flage : {i['flag']}")
    print(f" maps : {i['maps']}")
    j+=1