import requests

url = 'http://0.0.0.0:8000/stream'

def read_lines(url):
    resp = requests.get(url, stream=True)
    for line in resp.iter_lines(chunk_size=1):
        print line

def read_content(url):
    resp = requests.get(url, stream=True)
    for character in resp.iter_content():
        print character

read_lines(url)
