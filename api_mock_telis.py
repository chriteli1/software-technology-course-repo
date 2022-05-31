from flask import Flask, request
import mysql.connector


app = Flask(__name__)

mydb = mysql.connector.connect(host="dalab.ee.duth.gr", user="s57341", password="114682", database="s57341")
mycursor = mydb.cursor()

#BackEnd connection
@app.route('/api/import/', methods=['POST'])
def dataReceived():
    magnitude = float(request.args['mag'])
    place = request.args['place']
    time = request.args['time']
    flag = int(request.args['flag']) #Is equal to 0 if db is not empty and 1 if it is
    eq_id = "123t"
    #=====Empty table if new json is uploaded=====#
    if flag == 0:
        sql0 = "truncate table earthquakes"
        mycursor.execute(sql0)
        mydb.commit()
    # ============================================#

    #=====Send new data=====#
    sql = "insert into earthquakes (mag, place, time, eq_id) values(%s, %s, %s, %s)"
    val = (magnitude, place, time, eq_id)
    mycursor.execute(sql, val)
    mydb.commit()
    # ======================#

    return "Success!"


if __name__ == '__main__':
    app.run(debug=True)
