from flask import Flask, render_template
from rss_reader import Feeder

app = Flask(__name__)


@app.route('/')
def index():
    list_feed = []
    urls = [
        'https://tvn24.pl/tvnwarszawa/najnowsze.xml', 
        'https://remiza.com.pl/strona-glowna/feed/',
        'https://www.rmf24.pl/fakty/polska/feed'
    ]
    for url in urls:
        feed = Feeder(url)
        list_feed.append(feed.create_dict())
    
    return render_template("index.html", scr=list_feed)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

