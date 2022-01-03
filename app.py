from flask import Flask, request
from flask.json import jsonify
from http import HTTPStatus

from flask.wrappers import Request


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def hello_world() :
    return "Hello World!"


@app.route('/hello', methods = ['GET'])
def hello() :
    return "반갑습니다 이 경로는 /hello 경로입니다!"

@app.route('/bye', methods = ['GET'])
def bye():
    a = 100
    b = 50
    c = a * b
    c = str(c)
    return c

@app.route('/act', methods = ['GET'])
def act():
    ret = {'count' : 2,
        'student' : [{'name' : '홍길동', 'age' : '30'},
                     {'name' : '김나나', 'age' : '25'}]}
    #파이썬의 딕셔너리와 리시트 조합을 json으로 만드는 방법
    ret_json = jsonify(ret)
    return ret_json, HTTPStatus.NOT_FOUND

@app.route('/add_two_nums', methods=['POST'])
def add_two_nums() :
   data = request.get_json()
   print(data)

   x = data['x']
   y = data['y']

   result = x + y

   # 클라이언트에세 데이터를 보낼 때는, 항상 json 으로 만들어서 보낸다.
   ret = {"sum" : result}

   # 만든 json을, 클라이언트에 리턴해줘야 한다.
   return jsonify(ret) , HTTPStatus.OK
    
if __name__ == "__main__" :
    app.run()

## export FLASK_APP=app.py
## export FLASK_RUN_PORT=5000