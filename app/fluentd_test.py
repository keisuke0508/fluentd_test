# -*- coding:utf-8 -*-

from flask import request, render_template
from fluent import sender, event
from pymongo import MongoClient
from datetime import datetime
import json


class FluentdTest(object):
    TEMPLATE = "index.html"

    @classmethod
    def get(cls):
        return render_template(cls.TEMPLATE)

    @classmethod
    def post(cls):
        name = request.form.get("name")
        age = request.form.get("age")

        if not name or not age:
            return cls.get()

        data = {
            "name": name,
            "age": age,
            "created": datetime.now().strftime("%Y/%m/%d %H/%M/%S")
        }
        sender.setup("fluent.test", host="0.0.0.0", port=24224)
        event.Event("local", data)

        # FluentdTestMongoObj.insert(data)

        return render_template(
            cls.TEMPLATE,
            name=name,
            age=age
        )


class FluentdTestMongoObj(object):
    collection_name = "test_data"

    @classmethod
    def db(cls):
        return MongoClient("localhost", 27017).fluentd_test

    @classmethod
    def insert(cls, data):
        cls.db()[cls.collection_name].insert_one(data)
