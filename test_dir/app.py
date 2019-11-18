# Brian Moses
# SoftDev1 pd 2
# K#09: ’Tis Not a Race -- But You Will Go Faster
# 2019-9-22

# https://www.yelp.com/developers/documentation/v3/business_search
# tKiZ_qS57cBSfmAxfCXF0sHinmPEG4v0pvANltq9hDLPUIDmM5zDdWbjy89BB5feUMcLFZtT_uVu5RHOnzfHGBUnZoPeVAbvmxemTEyk_WLA0B6FXnbnB59GfuDQXXYx

from flask import Flask, render_template
from flask import request
from flask import jsonify
import urllib,  json

app = Flask(__name__) #create new instance of flask

@app.route("/")
def hello_world():
    link = "https://api6.ipify.org?format=json"
    u = urllib.request.urlopen(link)
    response = u.read()
    ip = json.loads(response)["ip"]

    link = "http://ip-api.com/json/{}".format(ip)
    u = urllib.request.urlopen(link)
    response = u.read()
    data = json.loads(response)

    link = "https://www.metaweather.com/api/location/search/?lattlong={},{}".format(data["lat"], data["lon"])
    u = urllib.request.urlopen(link)
    response = u.read()
    location_data = json.loads(response)
    woeid = str(location_data[0]["woeid"])

    link = "https://www.metaweather.com/api/location/{}".format(woeid)
    u = urllib.request.urlopen(link)
    response = u.read()
    weather = json.loads(response)
    

  #https://github.com/Yelp/yelp-fusion/blob/master/fusion/php/sample.php
    
    api_key='tKiZ_qS57cBSfmAxfCXF0sHinmPEG4v0pvANltq9hDLPUIDmM5zDdWbjy89BB5feUMcLFZtT_uVu5RHOnzfHGBUnZoPeVAbvmxemTEyk_WLA0B6FXnbnB59GfuDQXXYx'
    
    headers = {'Authorization': 'Bearer %s' % api_key}
	
    link = "https://api.yelp.com/v3/businesses/search"
    
    params = {'term':'seafood','location':'New York City'}
    
    req=requests.get(url, params=params, headers=headers)
    
    yelp_data = json.loads(req.text)
    
    return "Weather in your area: " + weather["consolidated_weather"][0]["weather_state_name"]

    

if __name__ == "__main__":
    app.debug = True
    app.run()
