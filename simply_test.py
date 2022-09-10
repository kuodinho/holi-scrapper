   
import requests

def test1():
    res = requests.get("https://www.itaka.pl/last-minute/")
    assert res.status_code == 201