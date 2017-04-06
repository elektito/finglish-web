#!/usr/bin/env python3

from finglish import f2p
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def root_post():
    finglish = request.form['finglish']
    persian = f2p(finglish)
    params = {
        'persian': persian,
    }
    return render_template('root.html', **params)

@app.route('/', methods=['GET'])
def root():
    params = {
        'persian': '',
    }
    return render_template('root.html', **params)

def main():
    app.run(port=8007)

if __name__ == '__main__':
    main()
