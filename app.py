# -*- coding: utf-8 -*- 
import os
from datetime import datetime
from flask import Flask, request, jsonify
  

app = Flask(__name__)
 

@app.route('/keyboard')
def Keyboard():
 
    dataSend = {
        "type" : "buttons",
        "buttons" : ["시작하기", "도움말"]
    }
 
    return jsonify(dataSend)
 
 
 
@app.route('/message', methods=['POST'])
def Message():
    
    dataReceive = request.get_json()
    content = dataReceive['content']
 
    if content == u"시작하기":
        dataSend = {
            "message": {
                "text": "실시간 도로소통정보를 제공하는 carvis 서비스입니다"
            }
        }
    elif content == u"도움말":
        dataSend = {
            "message": {
                "text": "#소통, #돌발(사고, 공사 행사), #통제"
            }
        }
    elif u"서울" in content:
        dataSend = {
            "message": {
                "text": "서울외곽순환고속도로 성남톨게이트→성남IC 기간 2017.08.31. 22:48 ~ 2017.09.01. 01:51 내용<공사> 서울외곽순환선(1000) (2,3차로)노면 보수 작업중"
            }
        }
   elif u"소통" in content:
        dataSend = {
            "message": {
                "text": "퇴계로2가->충무로역 적재불량 초보자 트럭 발견"
            }
        }
    elif u"안녕" in content:
        dataSend = {
            "message": {
                "text": "안녕하세요 carvis입니다.^^"
            }
    }
    else:
        dataSend = {
            "message": {
                "text": "carvis 학습중"
            }
        }
 
    return jsonify(dataSend)
 

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    """.format(time=the_time)
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
