from flask import Flask, render_template, request, url_for
import os


application = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
word_file = os.path.join(basedir, 'static/AliceInWonderland.txt')

@application.route('/', methods=['GET', 'POST'])
def index():
    lines = []
    with open(word_file, 'rb') as fileinput:
        for line in fileinput:
            for words in line.split():
                if str(words)[2:-1] == "Adventures":
                    lines.append(line.decode())
    return render_template('index.html', lines = lines)


if __name__ == '__main__':
    application.run()
