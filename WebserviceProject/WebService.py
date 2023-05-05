import random
from flask import Flask,jsonify,request,render_template
import requests
import json
import sys
from datetime import datetime


user_type = ''
app= Flask(__name__)
# @app.route('/')
# def index():
#     global user_type
#     user_type = request.headers.get('User-Agent')
#     if 'Mozilla' in user_type:
#         return render_template('index.html',data='data')
#     return "Welcome to the Number Generator"


def getTemp():
    api_url = "https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/hp-daily-forecast-day0.json"
    response = requests.get(api_url)
    data = json.loads(response.text)
    data_list = len(data["data"])

    rand_list_item = random.randrange(data_list)
    temp = data["data"][rand_list_item]["tMax"]
    return temp

def generateRand ():
    rand_num = random.randrange(sys.maxsize)
    return rand_num

@app.route('/bin')
def binaryConversion():
    temp_bin = bin(getTemp())
    rand_bin = bin(generateRand())
    return temp_bin,rand_bin

def xorCalc():
    temp_bin = binaryConversion()[0]
    rand_num_bin = binaryConversion()[1]
    return int(temp_bin[2:]) ^ int(rand_num_bin[2:])

def overflowHandler(num):
    treated_num=''
    for ch in str(num):
        if ch<='1':
            treated_num += ch
    return treated_num

@app.route('/')
def generate():
    num =xorCalc()
    bin_num = overflowHandler(num)
    date= datetime.now().strftime("%d-%B-%Y")
    time = datetime.now().strftime("%H:%M:%S")
    data ={'Number': int(bin_num,2),'Binary value':bin_num,'Date':date,'Time':time}
    user_type = request.headers.get('User-Agent')
    if 'Mozilla' in user_type:
        return render_template('index.html' ,data=data)
    return jsonify(data)

if __name__ == '__main__':
    app.run()



