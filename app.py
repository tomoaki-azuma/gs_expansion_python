import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup
import random

app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
    """はてブのホットエントリーから記事を入手して、ランダムに1件返却します."""

    html = urlopen('https://b.hatena.ne.jp/hotentry/all')
    bs = BeautifulSoup(html)

    pickupitems = []
    # 記事の一覧のliを取得
    items = bs.find_all('h3', class_='entrylist-contents-title')
    for item in items:
        content = item.find('a')
        if content:
            pickupitems.append([content.get('title'), content.get('href')])
        
    idx = random.randrange(len(pickupitems))
    pickeditem = pickupitems[idx]

    return json.dumps({
        "content" : pickeditem[0],
        "link" : pickeditem[1]
    })

@app.route("/api/xxxx")
def api_xxxx():
    """
        **** ここを実装します（発展課題） ****
        ・自分の好きなサイトをWebスクレイピングして情報をフロントに返却します
        ・お天気APIなども良いかも
        ・関数名は適宜変更してください
    """
    pass

if __name__ == "__main__":
    app.run(debug=True, port=5004)
