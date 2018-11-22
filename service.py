from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app=Flask(__name__)
CORS(app)


def mysqlconnection():
    mydb = mysql.connector.connect(
        host="139.59.90.118",
        user="deepjyoti",
        passwd="xxxx",
        database="fifablog"
    )

@app.route("/getblogs", methods=['GET'])
def getblogs():
    