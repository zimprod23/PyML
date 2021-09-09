import json
from re import X
from flask import Flask,request,jsonify
import utils



app = Flask(__name__)

@app.route('/get_data')
def get_loaded_data():
    responce = jsonify({
        'nationality' : utils.load_dd()[0],
        'club' : utils.load_dd()[1],
        'position' : utils.load_dd()[2]
    })
    responce.headers.add('Access-Control-Allow-Origin','*')

    return responce

@app.route('/predict_market_value',methods=['POST'])
def predict_market_value():
    try:
        #age,page_views,fpl_value,fpl_points,region,new_foreign,big_club,new_signing,nat,club,pos
        request_data = request.get_json()
        request_data = json.loads(request_data)
        age = int(request_data['age'])
        page_views = int(request_data['page_views'])
        fpl_value = float(request_data['fpl_value'])
        fpl_points = float(request_data['fpl_points'])
        region = float(request_data['region'])
        new_foreign = int(request_data['new_foreign'])
        big_club = int(request_data['big_club'])
        new_signing = int(request_data['new_signing'])
        nat = request_data['nat']
        club = request_data['club']
        pos = request_data['pos']
    except Exception as e:
        res = jsonify({
        'error' : e
        })
        res.headers.add('Access-Control-Allow-Origin','*')
        return res
    else:
        response = jsonify({
        'estimated_price' :round(utils.get_estimated_market_value(age,page_views,fpl_value,fpl_points,region,new_foreign,big_club,new_signing,nat,club,pos),2),
        'dd' : [age,page_views,fpl_value,fpl_points,region,new_foreign,big_club,new_signing,nat,club,pos]
        })
        response.headers.add('Access-Control-Allow-Origin','*')
        return response

@app.route('/predict_market_value1',methods=['POST'])
def predict_market_value1():
    try:
        #age,page_views,fpl_value,fpl_points,region,new_foreign,big_club,new_signing,nat,club,pos
        request_data = request.get_json()
        request_data = json.loads(request_data)
        print(type(request_data))
        x = request_data[0]
    except Exception as e:
        res = jsonify({
        'error' : e
        })
        res.headers.add('Access-Control-Allow-Origin','*')
        return res
    else:
        response = jsonify({
        'estimated_price' :x
       
        })
        response.headers.add('Access-Control-Allow-Origin','*')
        return response


if __name__ == '__main__':
    print("Starting python flask for home price prediction")
    app.run()