from xmlrpc.client import _iso8601_format
import requests
import re
import xml.etree.ElementTree as et
from bs4 import BeautifulSoup
from datetime import datetime


keywords = [
    'burza',
    'wypadek',
    'karambol',
    'imgw',
    'pożar',
    'kolizja',
    'zgon',
    'obrażenia',
    'kierowca',
    'dachowanie',
    'tragicznego',
    'LPR'
]

class Feeder():
    """_summary_
    """

    def __init__(self, path: str):
        self.path = path
        self.data = {}
        
    def response(self):
        _response = requests.get(self.path)
        if _response.status_code == 200:
            return _response
        
    def create_root(self) -> et.Element:
        """ Przetwarza text XML odpowiedzi obiektu żądania

        Returns:
            et.Element: struktura pliku XML
        """
        return et.fromstring(self.response().text)
    
    def create_dict(self):
        i = 0
        _root = self.create_root()
        
        # Iteracja po dokumencie xml
        for item in _root.iter('item'):
            # Oczyszczanie elementów 
            _title = item.find('title').text
            _description = self.remove_tags(item.find('description').text)
            _link = item.find('link').text
            _publication = self.pubdate_to_datetime(item.find('pubDate').text)
            
            # Wyszukiwanie słów kluczowych w tytułach i treści artykułów
            if (any(substring in _title for substring in keywords) or 
                any(substring in _description for substring in keywords)):
                self.data['item' + '_' + str(i)] = {
                    'title': _title,
                    'description': _description,
                    'link': _link,
                    'pub_date': _publication.date(),
                    'pub_time': _publication.time()
                }
                i += 1
        return self.data
    
    def pubdate_to_datetime(self, pub_date: str):
        if "Z" in pub_date:
            date = datetime.strptime(pub_date, "%Y-%m-%dT%H:%M:%S.%f%z")
            date = date.replace(tzinfo=None)
        else:
            date = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %z")
            date = date.replace(tzinfo=None)
        return date
    
    def remove_tags(self, html: str) -> str:
        """ Odpowiada za oczyszczenie przekazanego elementu 
        z zbędnych znaczników. 

        Args:
            html (str): ciąg tekstowy zawierający zbędne znaczniki html

        Returns:
            str: oczyszczony ciąg tekstowy 
        """
        soup = BeautifulSoup(html, "html.parser")
        return soup.get_text()

if __name__ == '__main__':
    url = 'https://tvn24.pl/tvnwarszawa/najnowsze.xml'
    t = Feeder(url).create_dict()
    d = t['item_0']['publictation']
    
    print(d.time())
    