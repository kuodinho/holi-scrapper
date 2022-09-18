from cgitb import text
import requests
from bs4 import BeautifulSoup

def offer_print(respo):
    soup = BeautifulSoup(respo.content, 'html.parser')
    #result = soup.find_all("div", class_="offer-list_inner-wrapper clearfix")
    one_div = soup.find_all("article", class_="offer clearfix")
   # i = 0 #offer number
    for index, item in enumerate(one_div, start=1):
        destination = item.find("div" , class_="offer_object-info col-xs-12 col-md-8 col-sm-8").findChildren("a" , recursive=True)
        country = destination[0].find(text=True)
        city = destination[1].find(text=True)
        date = item.find("div" , class_="offer_date pull-right").contents[1].find(text=True)
        food = item.find("div" , class_="offer_food pull-right").contents[1]
        price = item.find("span", class_="current-price_value").find(text=True)
        #hotel_rank = item.find("span", class_="hotel-rank").find(text=True)
        try:
            hotel_rank = item.find("span", class_="hotel-rank").find(text=True) + "/6"
        except AttributeError: 
            hotel_rank = "no hotel ranking"  
        print(index,".", country, "-", city, "\n", "Date:", date, "\n", "Food:", food, "\n",
         "How much it costs:", price,"PLN", 
        "\n", "Hotel ranking:", hotel_rank )

respo = requests.get("https://www.itaka.pl/last-minute/", timeout=10)
if respo.status_code != 200:
    print(respo.status_code)
    print("CRITICAL ERROR")
else:
    offer_print(respo)

   