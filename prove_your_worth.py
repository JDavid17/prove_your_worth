import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw
from io import BytesIO

start = "http://www.proveyourworth.net/level3/start"
activate = "http://www.proveyourworth.net/level3/activate?statefulhash"
payload = "http://www.proveyourworth.net/level3/payload"
back_to = "http://www.proveyourworth.net/level3/reaper"

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

def post_BACK_TO(payload_url: str, post_url: str):
    r = s.get(payload_url)
    # print(r.headers)
    files = {
        'resume': open("cv.pdf", "rb"),
        'image': open("image.jpg", "rb"),
        'code': open("prove_your_worth.py", "rb")
    }

    post_back_fields = {
        'email': "jdavidhc1710@gmail.com",
        'name': "Joel David Hernández Cruz",
        'code': "https://github.com/JDavid17/prove_your_worth/blob/master/prove_your_worth.py",
        'resume': "https://github.com/JDavid17/prove_your_worth/blob/master/cv.pdf",
        'image': "https://github.com/JDavid17/prove_your_worth/blob/master/image.jpg",
        'aboutme': "I'm a Senior Student of Computer Science, at The University of Havana."
    }

    print(f"files: {files}")
    response = s.post(post_url, data=post_back_fields, files=files)
    # print(response.url)
    print(response.text)
    # print(response.status_code)
    # print(response.headers)


def get_IMAGE(url: str):
    r = s.get(url, stream=True)
    image = Image.open(r.raw)
    image.save("image.jpg", "JPEG")




if __name__ == "__main__":
    get_SESSID(start)
    get_PAYLOAD(start)
    # get_IMAGE(payload)
    post_BACK_TO(payload, back_to)
