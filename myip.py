import requests

if __name__ == '__main__':
    r = requests.get("http://httpbin.org/ip")

    ip = r.json()['origin']

    parsed = ip.split(",")[0]
    print(parsed)
