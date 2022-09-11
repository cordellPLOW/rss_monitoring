from flask import Flask, render_template
from rss_reader import Feeder

app = Flask(__name__)


@app.route('/')
def index():
    list_feed = []
    urls = [
        'https://tvn24.pl/najnowsze.xml',
        'https://tvn24.pl/tvnwarszawa/najnowsze.xml', 
        'https://tvn24.pl/lodz.xml',
        'https://tvn24.pl/katowice.xml',
        'https://tvn24.pl/krakow.xml',
        'https://tvn24.pl/najnowsze.xml',
        'https://tvn24.pl/wroclaw.xml',
        'https://tvn24.pl/poznan.xml',
        'https://tvn24.pl/pomorze.xml',
        'https://remiza.com.pl/strona-glowna/feed/',
        'https://www.rmf24.pl/fakty/polska/feed'
        'https://wydarzenia.interia.pl/feed'
        'https://www.polsatnews.pl/rss/polska.xml',
        'https://wydarzenia.interia.pl/wiadomosci-lokalne/feed'
    ]
    for url in urls:
        feed = Feeder(url)
        data = feed.create_dict()
        if data is not None:
            list_feed.append(data)
    
    return render_template("index.html", scr=list_feed)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

