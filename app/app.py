# -*- coding:utf-8 -*-

from flask import Flask
from fluentd_test import FluentdTest
import os


# flask setting
app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET'])
def get():
    return FluentdTest.get()


@app.route('/', methods=['POST'])
def post():
    return FluentdTest.post()


if __name__ == "__main__":
    app.run(host='localhost', port=5000)
