#from urllib3 import request
from urllib3.request import RequestMethods

def separate(url: str):
    request = RequestMethods()
    request.urlopen(url=url, method="")
    print(request)
    #request.


if __name__ == "__main__":
    separate(str(input("Enter url to open: ")))