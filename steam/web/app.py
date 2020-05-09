from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route('/')   # when we open the root url it executes below func http://127.0.0.1:5000/
def index():
    resp = requests.get(
        url='http://127.0.0.1:9080/crawl.json?start_requests=True&spider_name=best_selling'
    ).json()
    # items = json.dumps(resp.get('items')) #json.dumps is to remove the stats at the end of the page
    items = resp.get('items')
    return render_template('index.html', games=items)


@app.route('/show')
def show_template():
    users = [
    'User1',
    'Imdad',
    'Frank'
    ]
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
