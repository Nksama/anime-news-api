from flask import Flask, json , jsonify
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)


@app.route('/')
def get_news():

    url = 'https://animenewsnetwork.com'

    res = requests.get(url).text
    soup = BeautifulSoup(res , "html.parser")

    news_card = soup.find("div" , class_="herald box news")

    src = news_card.find("div" , class_="thumbnail lazyload")['data-src']
    pic = f"{url}{src}"

    sypnosis = news_card.find("div" , class_="preview").text
    title = news_card.find("h3").text.strip()
    post_url = news_card.find("h3").find("a")['href']
    
    return jsonify({"title": title , "post_url": F"{url}{post_url}" , "image": pic , "info": sypnosis})





if __name__ == '__main__':
    app.run(debug=True)
