from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd
from django.http import FileResponse
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app, supports_credentials=True)
class getgraph(Resource):
    def get(self):
        return "graph"
        

class getdata(Resource):
    def get(self):
        #from pytrends.request import TrendReq
        #pytrend = TrendReq()
        #keyword = "Andhra Pradesh"
        #location = "IN"
        #timeframe = '2016-12-14 2017-01-25'
        #search_trem = "data science"
        #pytrend.build_payload(kw_list= [keyword], cat=0, timeframe= timeframe , geo=location, gprop='')
        #df = pytrend.interest_by_region()
        df=pd.read_csv("test.csv")
        import json
        d = json.loads(df.to_json(orient='records'))
        return d


api.add_resource(getgraph, '/graph') # Route_1
api.add_resource(getdata, '/data') # Route_1


if __name__ == '__main__':
     app.run(host = '0.0.0.0' ,port='5002')
