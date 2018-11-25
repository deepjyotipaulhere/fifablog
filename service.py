from flask import Flask, jsonify,request,make_response
from flask_cors import CORS
import mysql.connector
import jwt
from functools import wraps
from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

app=Flask(__name__)
CORS(app)
app.config['SECRET_KEY']='FiFaRussia'

def mysqlconnection():
    return mysql.connector.connect(
        host="139.59.90.118",
        user="deepjyoti",
        passwd="Bryanadams@1",
        database="fifablog"
    )
def mongoconnection():
    return MongoClient('mongodb://139.59.90.118:27017')


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token=None
        if 'x-access-token' in request.headers:
            token=request.headers['x-access-token']
        
        if not token:
            return make_response("token required",500)

        try:
            data=jwt.decode(token,app.config['SECRET_KEY'])
            current_user={
                "name":data["name"],
                "email":data["email"]
            }
        except Exception as e:
            print(str(e))
            return make_response("Invalid token",501)
        return f(current_user,*args,**kwargs)
    return decorated


@app.route("/insertuser", methods=['POST'])
def insertuser():
    try:
        x=request.get_json()
        con=mysqlconnection()
        cur=con.cursor()
        cur.execute("INSERT INTO user(`username`,`useremail`,`nationality`,`mobile`,`password`) VALUES('"+x['name']+"','"+x['email']+"','"+x['country']+"','"+x['mobile']+"','"+x['password']+"')")
        con.commit()
        con.close()
        return "ok"
    except Exception as e:
        print(str(e))
        return make_response("error",500)


@app.route("/signin", methods=['POST'])
def signin():
    try:
        x=request.get_json()
        con=mysqlconnection()
        cur=con.cursor()
        cur.execute("SELECT * FROM user WHERE useremail='"+x['email']+"' AND password='"+x['password']+"'")
        user=cur.fetchall()[0]
        d={
            'userid':user[0],
            'email':user[2],
            'name':user[1],
            'country':user[3],
            'mobile':user[4],
        }
        token=jwt.encode(d,app.config['SECRET_KEY']).decode('UTF-8')
        con.close()
        return jsonify({"auth":token,"name":d['name']})
    except Exception as e:
        print(str(e))
        return make_response("error",500)

@app.route("/insertpost", methods=['POST'])
@token_required
def insertpost(user):
    try:
        x=request.get_json()
        x.update(user)
        x['date']=str(datetime.date.today())
        client=mongoconnection()
        i=client.fifablog.blog.insert_one(x).inserted_id
        return "ok"
    except Exception as e:
        print(str(e))
        return make_response("error",500)

@app.route("/getblogs/<x>", methods=['GET'])
def getblogs(x):
    try:
        client=mongoconnection()
        
        d=[]
        if x=="0":
            i=client.fifablog.blog.find({"status":2})
            for p in i:
                d.append({
                    'id':str(p['_id']),
                    'title':str(p['title']),
                    'content':str(p['content'][:30])+"..."
                })
        else:
            i=client.fifablog.blog.find_one({"_id":ObjectId(x)})
            d={
                'id':str(i['_id']),
                'title':str(i['title']),
                'content':str(i['content']),
                'date':str(i['date']),
                'name':str(i['name']),
                # 'photos':list(i['photos']),
            }
        return jsonify(d)

    except Exception as e:
        print(str(e))
        return make_response("error",500)



if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')