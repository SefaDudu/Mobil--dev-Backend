

import base64
import datetime
from flask import Flask, jsonify, render_template, request, redirect, session
import pymongo
from bson.json_util import ObjectId, dumps
from bson import json_util
import json
import bcrypt


@app.route('/api/login',methods=['POST','GET'])
def login():
    username= request.json["name"]
    password= request.json["pass"]

    user=student.find({"username":username})
    for i in user:
        p=i["password"]
        r=i["role"]

    if not isinstance(p, bytes):
            p = p.encode('utf-8')
    if bcrypt.hashpw(password.encode('utf8'),p)==p:
        return{"username":username,"role":r}


class ObjectIdEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(ObjectIdEncoder, self).default(obj)

app = Flask(name)
app.secret_key = 'secretsecretmysecretkeysecret'
app.json_encoder = ObjectIdEncoder

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["OBISDB"]
student = mydb["OBISDATA"]



@app.route('/')
def index():
    return "Mobil Uygulama için servisler..."

@app.route('/api')
def get_api():
    d = {"res": list(student.find({}))}
    b=json_util.dumps(d)
    return jsonify(b)