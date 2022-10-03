import unittest
import pytest
from unittest.mock import mock_open, patch
from rss_reader import Feeder


@pytest.fixture()
def tvn_rss():
    return 'https://tvn24.pl/najnowsze.xml'


@pytest.fixture()
def remiza():
    return 'https://remiza.com.pl/strona-glowna/fed/'


def test_response_positive(tvn_rss):
    feeder = Feeder(tvn_rss)
    assert feeder.response() != None
    
    
def test_response_negative(remiza):
    feeder = Feeder(remiza)
    assert feeder.response() == 'Bad response'
