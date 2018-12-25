import random
from flask import Flask
from flask import render_template
from random import shuffle
import requests
import re


def get_names(filename):
    f = open(filename, 'r')
    data = f.read()
    return list(map(lambda x: x.split('(')[0].strip(), data.splitlines()))


names = get_names("names.txt")
picture_urls = dict()


def get_urls(name):
    if name not in picture_urls.keys():
        print("Building img cache for " + name)
        picture_urls[name] = build_links_for_name(name)
    return picture_urls[name]


def get_random_name(lower_bound):
    idx = random.randint(0, lower_bound)
    entry = names[idx]
    return entry


app = Flask(__name__, static_url_path='/static')


@app.route('/randomname')
def randomname():
    return get_random_name(99)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/game/<up_to>")
def game(up_to="9"):
    up_to = int(up_to)
    idx_to_guess = random.randint(0, up_to)
    name_options = names[:up_to]
    shuffle(name_options)
    image_links = get_urls(names[idx_to_guess])[:5]
    shuffle(image_links)
    return render_template('game.html',
                           difficulty="1-" + str(up_to + 1) + " names",
                           names=name_options,
                           name_index=idx_to_guess,
                           image_links=image_links)


@app.route("/guess/<id>/<name>")
def guess(id="-1", name=""):
    id = int(id)
    if id == -1:
        return "Bad rq"
    print("Someone is guessing that " + str(id) + " is " + name + "")
    if names[id] == name:
        print("This is true")
        return "True"
    print("Actually, " + name + " is " + str(names.index(name)))
    print("And, " + str(id) + " is " + names[id])
    return "False"


def build_links_for_name(name):
    url = 'https://www.google.com/search?q=' + name + '&client=firefox-b-ab&tbm=isch&tbo=u&source=univ&sa=X&ved=2ahUKEwjN5fWwxu3eAhUQmIsKHeA-D90QsAR6BAgEEAE'
    headers = {
        'User-Agent': 'Nokia5250/10.0.011 (SymbianOS/9.4; U; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Safari/525 3gpp-gba'}
    response = requests.get(url, headers=headers)
    text_file = open("output.html", "w", encoding='utf-8')
    text_file.write(response.text)
    text_file.close()
    ans = []
    results = re.findall(r'<img src="h.*?>', response.text)
    for result in results:
        urlg = re.search(r'"(.+?)"', result)
        if urlg:
            url = urlg.group(1)
            ans.append(url)
    return ans


if __name__ == '__main__':
    app.run(debug=True)
