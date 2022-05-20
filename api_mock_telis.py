from urllib.request import urlopen
from flask import Flask, request, render_template, Blueprint, redirect
import mysql.connector
import json
import requests
from flask_restful import Resource, Api


api = Blueprint('api', __name__, template_folder='templates')

#BackEnd connection
@api.route('/dataReceived', methods=['POST', 'GET'])
def dataReceived():
    if request.method == 'POST':
        magnitude = request.form['mag']
        magnitude_final = magnitude.replace("[", "")
        magnitude_final = magnitude_final.replace("]", "")
        magnitude_final = magnitude_final.split(",")
        mag_float = float(magnitude_final[1])
        print(mag_float)
        print(type(mag_float))
        # sql="insert into blah(magnitude) values(%s)"
        # val=[(magnitude)]
        # #mycursor.execute("INSERT INTO quake(magnitude) VALUES (%s));".format(magnitude))
        # mycursor.execute(sql,val)
        # mydb.commit()
        return "Success!"


#FrontEnd connection
@api.route('/userDataReceived', methods=['POST'])
def userDataReceived():
    if request.method == 'POST':
        minMag = request.form['minMag']
        maxMag = request.form['maxMag']
        #Get data from database
    return render_template("search.html")
