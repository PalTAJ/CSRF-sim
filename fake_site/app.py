from random import random,randint
from flask import request, Response, render_template, Flask, redirect, make_response, url_for

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def mainPage():

    return render_template('cats.html')


if __name__ == "__main__":
    app.run(host='localhost',port=5005,debug=True)