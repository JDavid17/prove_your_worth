import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw

start = "http://www.proveyourworth.net/level3/start"
activate = "http://www.proveyourworth.net/level3/activate?statefulhash"
payload = "http://www.proveyourworth.net/level3/payload"

# Session object
s = requests.Session() 

def get_SESSID(url: str):
    s.get(url)
    print(f"PHPSESSID: {s.cookies['PHPSESSID']}")


def get_HASH(url: str):
    r = s.get(url)
    html = BeautifulSoup(r.text, 'html.parser')
    phash = html.input['value']
    print(f"statefulhash: {phash}")
    return phash

def get_PAYLOAD(url: str):
    phash = get_HASH(url)
    r = s.get(activate+f'={phash}')
    print(r.headers)
    print(f"Hash: {phash}")

def post_PAYLOAD(url: str):
    r = s.get(url)
    print(r.headers)




if __name__ == "__main__":
    get_SESSID(start)
    get_PAYLOAD(start)
    post_PAYLOAD(payload)
