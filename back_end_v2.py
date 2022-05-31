from flask import Flask, render_template, request
import json
import requests
from urllib.request import urlopen

#https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson?fbclid=IwAR01paS_v9H7RErg882CN3drkfxaksPY8rMmkzbBuUvwKqkX-Jo0adrDzEI

app = Flask(__name__)


@app.route('/backend') #Url input screen
def upload_file():
    return render_template('back-end.html')


@app.route('/data-sent', methods=['POST', 'GET']) #Url sent screen
def uploader():
    if request.method == 'POST':
        f = request.form['url']
        with urlopen(f) as response:
            source = response.read()
        data = json.loads(source) #The data in json format
        is_db_empty = 0
        for x in data['features']:
            mag = x['properties']['mag']
            place = x['properties']['place']
            time = x['properties']['time']
            api_url = f"http://127.0.0.1:5000/api/import/?mag={mag}&place={place}&time={time}&flag={is_db_empty}" #Enter values with formatted string
            payload = {}
            headers = {}
            response = requests.request("POST", api_url, headers=headers, data=payload)
            is_db_empty = 1
        return response.text


if __name__ == '__main__':
    app.run(debug=True)
