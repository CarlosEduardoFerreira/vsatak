import flask
import mysql.connector
import json, decimal


app = flask.Flask(__name__)
app.config["DEBUG"] = False

## MySQL Connection
db = mysql.connector.connect(host="localhost", user="root", 
    passwd="mg72ax", db="vsatak")
print("db" + str(db))
## Define Cursor
cur = db.cursor(dictionary=True)


def dec_serializer(o):
    if isinstance(o, decimal.Decimal):
        return float(o)


@app.route('/insert_marker', methods=['POST'])
def insert_marker():

    json_data = flask.request.json

    uid     = json_data["uid"]
    coord_y = json_data["latitude"]
    coord_x = json_data["longitude"]

    sql = "INSERT INTO markers(uid, latitude, longitude) VALUES (%s, %s, %s)"
    val = (str(uid), str(coord_y), str(coord_x))
    cur.execute(sql, val)

    db.commit()

    if cur.rowcount < 1:
        return {"error": "Error trying insert new Marker."}

    return {"error": ""}


@app.route('/list_markers', methods=['GET'])
def list_markers():

    sql = "SELECT * FROM markers"
    cur.execute(sql)

    result = cur.fetchall()

    jsonObj = {}

    for row in result:
        jsonObj[row["uid"]] = { 'latitude': row['latitude'], 'longitude': row['longitude'] }

    return jsonObj


@app.route('/get_marker', methods=['POST'])
def get_marker():

    json_data = flask.request.json

    uid     = json_data["uid"]

    sql = "SELECT * FROM markers WHERE uid = '" + str(uid) + "' limit 1"
    cur.execute(sql)

    result = cur.fetchall()

    jsonObj = {}

    for row in result:
        jsonObj = { 'uid': row['uid'], 'latitude': row['latitude'], 'longitude': row['longitude'] }

    return jsonObj


@app.route('/delete_markers', methods=['GET'])
def delete_markers():

    sql = "DELETE FROM markers"
    cur.execute(sql)

    db.commit()

    return {"error": "", "success": "Connection OK."}


@app.route('/check_connection', methods=['GET'])
def check_connection():
    return {"error": "", "success": "Connection OK."}



if __name__ == '__main__':
    app.run(host='0.0.0.0')
else:
    app.run()