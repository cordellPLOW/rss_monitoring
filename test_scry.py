from rss_reader import Feeder

def test_create_dict_positive():
    path_ = 'https://remiza.com.pl/strona-glowna/feed/'
    assert Feeder(path_).create_dict() != None