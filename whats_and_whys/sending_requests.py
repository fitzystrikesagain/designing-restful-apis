import requests

HOST = "http://localhost:80/{}"


def handle_request(method="get", endppoint="readHello"):
    url = HOST.format(endppoint)
    r = requests.request(method=method, url=url)
    print(r.text)


def main():
    get = ("get", "readHello")
    post = ("post", "createHello")
    put = ("put", "updateHello")
    delete = ("delete", "deleteHello")
    methods = [get, post, put, delete]
    for method in methods:
        handle_request(*method)


if __name__ == "__main__":
    main()
