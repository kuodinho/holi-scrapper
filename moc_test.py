from http import HTTPStatus
import requests
from bs4 import BeautifulSoup
def legit():
    respo = requests.get("https://www.itaka.pl/last-minute/")
    soup = BeautifulSoup(respo.content, 'html.parser')
    #result = soup.find_all("div", class_="offer-list_inner-wrapper clearfix")
    item = soup.find_all("article", class_="offer clearfix")  

def fakerespo():
    respo = requests.get("https://www.itaka.pl/last-minute/")
    soup = BeautifulSoup(respo.content, 'html.parser')
    #result = soup.find_all("div", class_="offer-list_inner-wrapper clearfix")
    x = soup.find_all("article", class_="offer clearfix")
    

def test_moc(mocker, fakerespo):
    fake_resp = mocker.Mock(return_value=fakerespo)
    fake_resp.status_code = HTTPStatus.OK
    info =legit()
    assert info == fake_resp
