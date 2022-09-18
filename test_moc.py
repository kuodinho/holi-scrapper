from http import HTTPStatus
import unittest
import requests
from bs4 import BeautifulSoup
from unittest.mock import MagicMock, patch
import os
import sys
def func():
    respo = requests.get("https://www.itaka.pl/last-minute/")
    soup = BeautifulSoup(respo.content, 'html.parser')
    #result = soup.find_all("div", class_="offer-list_inner-wrapper clearfix")
    item = soup.find_all("article", class_="offer clearfix")  
    return(item)
def z():
        with open(os.path.join(sys.path[0], "z.txt"), "r") as f:
            return(f)
#@patch('legit.item')
class fake(unittest.TestCase):
  def test_setUp(self):
        fake1 = MagicMock()
        fake1.status_code = HTTPStatus.OK
        fake1.return_value = z()
        self.assertEqual(func, fake1)
       
if __name__ == '__main__':
   unittest.main()
