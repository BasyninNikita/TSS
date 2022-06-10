import requests
import json

API = ["LGY6W34GKPymODNywv863QEbz28AN5tz", "N89CVWcUZOiroWF4VOJXMiOkE8b21amk", "r4avkfUAFvJEYmHGoLZUnkOyYWJBRGqV"]


def get_subdomains():
    headers = {"apikey": API[0],
               "children_only": "false",
               "include_inactive": "false"}
    response = requests.get("https://api.securitytrails.com/v1/domain/spbu.ru/subdomains", headers=headers)

    with open("m.txt", "w") as f:
        f.write(response.text)


if __name__ == '__main__':

    subdomains = ''
    with open("m.txt", "r") as rf:
        subdomains = json.load(rf)
    for i, sd in enumerate(subdomains["subdomains"]):
        # sd = json.loads(response.text)["subdomains"][0]
        apikey = {"apikey": API[i%len(API)]}
        rsp = requests.get("https://api.securitytrails.com/v1/domain/" + sd + ".spbu.ru", headers=apikey)
        data = json.loads(rsp.text)
        # print(data)
        if data["current_dns"]["a"]:
            a = []
            for j in range(len(data["current_dns"]["a"]["values"])):
                a.append(data["current_dns"]["a"]["values"][j]["ip"])
            b = data["hostname"]
            print(b, ":", a)
        else:
            print(data["hostname"])
