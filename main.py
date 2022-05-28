from urllib.request import urlopen
from flask import Flask, request, render_template, Blueprint, jsonify
import mysql.connector
import json

app = Flask(__name__)


with urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson") as response:
    source = response.read()

data = json.loads(source)
object=json.dumps(data, indent=4)


mydb = mysql.connector.connect(host="dalab.ee.duth.gr", user="s57330", password="114660", database="s57330")
mycursor = mydb.cursor()

# for x in data['features']:
#     magnitude = x['properties']['mag']
#     place = x['properties']['place']
#     time = x['properties']['time']
#     #print(magnitude, place, time)
#     sql = "insert into front_end(mag,place,time) values(%s,%s,%s)"
#     val = [magnitude, place, time]
#     mycursor.execute(sql, val)
#     mydb.commit()


@app.route('/significant_magnitude/<float:min> & <float:max>')
def significant_magnitude(min, max):
    min = float(min)
    max = float(max)
    if min < max:
        a = "SELECT mag, place, time FROM front_end WHERE mag >= %s AND mag <= %s "
        b = (min, max)
        mycursor.execute(a, b)
        myresult = mycursor.fetchall()
        earthquakes = []
        content = {}
        for rv in myresult:
            content = {'mag': rv[0], 'place': rv[1], 'date': rv[2]}
            earthquakes.append(content)
            #content = {}
        return jsonify(earthquakes)
    else:
        print("min prepei na exei mikrotero value apo to max")
    return


#significant_magnitude(4.0, 6.0)


@app.route('/location/<string:loc>')
def location(loc):
    c = "SELECT mag, place, time FROM front_end WHERE place = %s"
    d = [loc]
    mycursor.execute(c, d)
    myresult = mycursor.fetchall()
    earthquakes = []
    content = {}
    for rv in myresult:
        content = {'mag': rv[0], 'place': rv[1], 'date': rv[2]}
        earthquakes.append(content)
    return jsonify(earthquakes)


#location('55 km WSW of Masachapa, Nicaragua')


@app.route('/date/<string:dat>')
def date(dat=''):
    e = "SELECT mag, place, time FROM front_end WHERE time = %s"
    f = [dat]
    mycursor.execute(e, f)
    myresult = mycursor.fetchall()
    earthquakes = []
    content = {}
    for rv in myresult:
        content = {'mag': rv[0], 'place': rv[1], 'date': rv[2]}
        earthquakes.append(content)
    return jsonify(earthquakes)


#date('1652074367550')




if __name__ == '__main__':
    app.run(port=5000)


