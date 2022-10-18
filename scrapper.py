from bs4 import BeautifulSoup
import requests


def main():
    scrappedWebpage = requests.get(
        "https://www.itaka.pl/last-minute/", timeout=10)

    if scrappedWebpage.status_code != 200:
        print(scrappedWebpage.status_code)
        print("CRITICAL ERROR: ", scrappedWebpage.reason)
    else:
        print(extract_offer(scrappedWebpage))
# TODO: refactor the extract_offer function, so that it only returns the data. A different function should interpolate/print it - 
# S in the SOLID principle
def extract_offer(respo):
    soup = BeautifulSoup(respo.content, 'html.parser')
    one_div = soup.find_all("article", class_="offer clearfix")
    offers = ""

    for index, item in enumerate(one_div, start=1):
        destination = item.find(
            "div", class_="offer_object-info col-xs-12 col-md-8 col-sm-8").findChildren("a", recursive=True)
        country = destination[0].find(text=True)
        city = destination[1].find(text=True)
        date = item.find(
            "div", class_="offer_date pull-right").contents[1].find(text=True)
        food = item.find("div", class_="offer_food pull-right").contents[1]
        price = item.find("span", class_="current-price_value").find(text=True)

        try:
            hotel_rank = item.find(
                "span", class_="hotel-rank").find(text=True) + "/6"
        except AttributeError:
            hotel_rank = "no hotel ranking"

        offers += f'{index}. {country} - {city}\nDate: {date}\nFood: {food}\nHow much does it cost: {price}PLN\nHotel ranking:{hotel_rank}\n\n'

    return offers


if __name__ == '__main__':
    main()
