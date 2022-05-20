from flask import Flask, render_template, request, Blueprint, url_for, redirect, session, current_app
import json
from urllib.request import urlopen

#https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.geojson?fbclid=IwAR01paS_v9H7RErg882CN3drkfxaksPY8rMmkzbBuUvwKqkX-Jo0adrDzEI

back_end = Blueprint('back_end', __name__, template_folder='templates')


@back_end.route('/upload') #Url input screen
def upload_file():
    return render_template('back-end.html')


@back_end.route('/uploader', methods=['POST', 'GET']) #Url sent screen
def uploader():
    if request.method == 'POST':
        f = request.form['url']
        with urlopen(f) as response:
            source = response.read()
        data = json.loads(source) #The data in json format
        magnitude = []
        for x in data['features']:
            magnitude.append(x['properties']['mag'])
        return render_template("dataReceived.html", mag=magnitude) #Redirect to html that sends data to api

