import requests
import json

API = ["bWeWmPvZDlNKU3SLMrIn2btImSZYwUeO"] #, "N89CVWcUZOiroWF4VOJXMiOkE8b21amk", "r4avkfUAFvJEYmHGoLZUnkOyYWJBRGqV"]


def get_subdomains():
    headers = {"apikey": API[-1], #fix 0
               "children_only": "false",
               "include_inactive": "false"}
    response = requests.get("https://api.securitytrails.com/v1/domain/spbu.ru/subdomains", headers=headers)

    with open("m.txt", "w") as f:
        f.write(response.text)


if __name__ == '__main__':

    subdomains = ''
    with open("m.txt", "r") as rf:
        subdomains = json.load(rf)
    ips = open("ips.txt", "w")
    adrs = open("adrs.txt", "w")
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
            ip = str(str(b) + ":" )
            for i in a:
                ip = ip + i +" "
                adrs.write(str(i + '\n'))
            ips.write(ip + '\n')
        else:
            ips.write(str(data["hostname"] + '\n'))
