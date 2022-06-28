from urllib.request import urlopen
from flask import Flask, request, render_template, Blueprint, jsonify
import mysql.connector
import json
from flask_cors import CORS



# https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php#earthquakes

app = Flask(__name__)
CORS(app)

# mydb = mysql.connector.connect(host="dalab.ee.duth.gr", user="s57330", password="114660", database="s57330")
# mycursor = mydb.cursor()

mydb = mysql.connector.connect(host="dalab.ee.duth.gr", user="s57341", password="114682", database="s57341")
mycursor = mydb.cursor()


#BackEnd connection
@app.route('/api/import/', methods=['POST'])
def dataReceived():
    magnitude = float(request.args['mag'])
    place = request.args['place']
    time = request.args['time']
    flag = int(request.args['flag']) #Is equal to 0 if db is not empty and 1 if it is
    #=====Empty table if new json is uploaded=====#
    if flag == 0:
        sql0 = "truncate table earthquakes"
        mycursor.execute(sql0)
        mydb.commit()
    # ============================================#

    #=====Send new data=====#
    sql = "insert into earthquakes (mag,place,time) values(%s,%s,%s)"
    val = (magnitude, place, time)
    mycursor.execute(sql, val)
    mydb.commit()
    # ======================#

    return "Success!"

#Search by magnitude
@app.route('/significant_magnitude/<float:min>&<float:max>', methods=['GET'])
def significant_magnitude(min, max):
    if request.method == 'GET':
        min = float(min)
        max = float(max)
        if min < max:
    #===== Bring data from db with SQL command =====#
            a = "SELECT mag, place, time FROM earthquakes WHERE mag >= %s AND mag <= %s "
            b = (min, max)
            mycursor.execute(a, b)
            myresult = mycursor.fetchall()
    #===============================================#
    #===== Format data to give to frontend =====#        
            earthquakes = []
            content = {}
            for rv in myresult:
                content = {'mag': rv[0], 'place': rv[1], 'date': rv[2]}
                earthquakes.append(content)
                #content = {}
            return jsonify(earthquakes)
        else:
            print("min prepei na exei mikrotero value apo to max")
    #===========================================#
    return


#significant_magnitude(4.0, 6.0)

#Search by location
@app.route('/location/<string:loc>')
def location(loc):
    #===== Bring data from db with SQL command =====#
    c = "SELECT mag, place, time FROM earthquakes WHERE place LIKE '%" + loc + "%'"
    mycursor.execute(c)
    myresult = mycursor.fetchall()
    #===============================================#
    #===== Format data to give to frontend =====# 
    earthquakes = []
    content = {}
    for rv in myresult:
        content = {'mag': rv[0], 'place': rv[1], 'date': rv[2]}
        earthquakes.append(content)
    #===========================================#
    return jsonify(earthquakes)


#location('55 km WSW of Masachapa, Nicaragua')

#Search by date
@app.route('/date/<string:min>&<string:max>')
def date(min, max):
    #===== Bring data from db with SQL command =====#
    e = "SELECT mag, place, time FROM earthquakes WHERE time >= %s AND time <= %s" #SQL command to bring data from db
    f = (min, max)
    mycursor.execute(e, f)
    myresult = mycursor.fetchall()
    #===============================================#
    #===== Format data to give to frontend =====# 
    earthquakes = []
    content = {}
    for rv in myresult:
        content = {'mag': rv[0], 'place': rv[1], 'date': rv[2]}
        earthquakes.append(content)
    #===========================================#
    return jsonify(earthquakes)


#date('1652074367550')




if __name__ == '__main__':
    app.run(port=5000)
