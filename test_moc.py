import unittest
from scrapper import extract_offer
from unittest.mock import MagicMock

class TestScrapper(unittest.TestCase):
    def test_extract_offer(self):
        html_file = open("test_data.html", "rb")
        mocked_content = html_file.read()
        html_file.close()
        mocked_variable = MagicMock()
        mocked_variable.content = mocked_content
        self.assertEqual(extract_offer(mocked_variable), "1. Czarnogóra - Hotel Lusso Mare by Aycon\nDate: 08.10-11.10.22 (4 dni)\nFood: Śniadania\nHow much does it cost: 1 659 PLN\nHotel ranking:no hotel ranking\n\n2. Czarnogóra - Hotel Sato Conference & Spa Resort\nDate: 08.10-11.10.22 (4 dni)\nFood: 2 posiłki\nHow much does it cost: 1 719 PLN\nHotel ranking:4.3/6\n\n")

if __name__ == '__main__':
    unittest.main()

