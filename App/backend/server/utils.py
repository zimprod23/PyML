import pickle
import json
from flask.json import load
import numpy as np


__club = None
__nat = None
__pos = None
__model = None
__data_columns = None
def get_estimated_market_value(age,page_views,fpl_value,fpl_points,region,new_foreign,big_club,new_signing,nat,club,pos):
    load_saved_artifacts()
    try:
        nat_index = __data_columns.index(nat.lower())
        club_index = __data_columns.index(club.lower())
        pos_index = __data_columns.index(pos.lower())
    except Exception as e:
        print(e)
    else:
        x = np.zeros(len(__data_columns))
        x[0] = int(age)
        x[1] = int(page_views)
        x[2] = int(fpl_value)
        x[3] = int(fpl_points)
        x[4] = region
        x[5] = new_foreign
        x[6] = big_club
        x[7] = new_signing
        if nat_index >= 0:
            x[nat_index]=1
        
        if club_index >= 0:
            x[club_index]=1
        
        if pos_index >= 0:
            x[pos_index]=1
        
        return __model.predict([x])[0]

def load_dd():
    load_saved_artifacts()
    return __nat,__club,__pos

def load_saved_artifacts():
    print('Loading Saved Artifacts ... starting')
    global __club
    global __nat
    global __pos
    global __model
    global __data_columns 

    with open('./artifacts/columns.json','r') as f:
        __data_columns = json.load(f)['data_cols']
        __club = __data_columns[8:-29]
        __pos = __data_columns[-1:-14:-1]
        __pos.reverse()
        __nat = __data_columns[-14:-30:-1]
        __nat.reverse()
    
    with open('./artifacts/predict_market_value.pickle','rb') as f:
        __model = pickle.load(f)
    
    print("Loading saved artifacts ... finished")


if __name__ == '__main__':
    load_saved_artifacts()
    print(load_dd()[2])
    print(round(get_estimated_market_value(23,1413,7.5,144,1.0,0,0,0,'England','Everton','AM'),2),'M Euro')

