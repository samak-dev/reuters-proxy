from flask import Flask, Response
import requests
from requests.auth import HTTPDigestAuth

app = Flask(__name__)

# Reuters login details
USERNAME = "basheer@viralmedya.com.tr"
PASSWORD = "kyeZmzXn"

# Your private Reuters RSS URL
REUTERS_RSS_URL = "http://rmb.reuters.com/rmd/rss/wire/cSi394?limit=10&maxAge=2h&linkType=raw"

@app.route("/reuters")
def reuters_feed():
    try:
        response = requests.get(REUTERS_RSS_URL, auth=HTTPDigestAuth(USERNAME, PASSWORD))
        if response.status_code == 200:
            return Response(response.content, content_type="application/rss+xml; charset=utf-8")
        else:
            return f"Error fetching feed: {response.status_code} - {response.reason}", response.status_code
    except Exception as e:
        return str(e), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
