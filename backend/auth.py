# ACHTUNG: diese Datei ist nur zu Testzweck
import Create_db
from datetime import timedelta, timezone
import datetime
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies, jwt_required, get_jwt_identity, unset_jwt_cookies
from itsdangerous import json


#es handelt sich um eine DEmo und hat nichts mit dem backend zu tun!!!
#---------
#------

app = Flask(__name__)
app.config['JWT_TOKEN_LOCATION'] = ['headers']
#["headers", "cookies"]
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_ACCESS_COOKIE_PATH'] = "/token/"
#!todo felzmann überlegt guten pfad
app.config['JWT_REFRESH_COOKIE_PATH'] = "/token/refresh"
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_SECRET_KEY'] = "Arduinos_machen_spaß65"
#app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=5)
#app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(minutes=5)
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=1)
app.config['JWT_HEADER_TYP'] = "Bearer"
app.config['JWT_HEADER_NAME'] = "Authorization"
#!key umbenennen

jwt = JWTManager(app)


@app.route('/token/auth', methods=["GET"])
def login():
    # username = request.args.get("username", None)
    # password = request.args.get("password", None)

    # #!ersetzen durch Datenbankabfrage
    # if username != "test" or password != "kev":
    #     return jsonify({"login:": False}), 401

    # access_token = create_access_token(identity=username)
    # refresh_token = create_refresh_token(identity=username)
    
    # take = jsonify({"login:": True})
    # set_access_cookies( take,access_token)
    # set_refresh_cookies(take,  refresh_token)
    
    access_token = create_access_token(identity="example_user")
    refresh_token = create_refresh_token(identity="example_user")
    resp = jsonify({"login:": True})
    #set_access_cookies(resp, access_token)
    #set_refresh_cookies(resp, refresh_token)
    tokens = jsonify(access_token=access_token, refresh_token=refresh_token,)
    return tokens
    #return resp, 200


@app.route('/token/login', methods=["POST"])
def into():
    
    access_token = create_access_token(identity="example_user", fresh=True)
    refresh_token = create_refresh_token(identity="example_user")
    return {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'expiration-date':datetime.datetime.now() + datetime.timedelta(days=1),
        'userId': 5
        
    }, 200



def create_Jwt(email):
   # access_token = create_access_token(identity=email)
    refresh_token = create_refresh_token(identity=email)
    expires = datetime.timedelta(minutes=30)
    access_token = create_access_token(identity=email, expires_delta=expires)
    userid = Create_db.get_Userid()
    resp = jsonify({'login:': True, 'token':access_token, 'refresh_token': refresh_token , 'userid': userid, 'expires in': str(expires)})
   # set_access_cookies(resp, access_token) # Todo: brauchen wir das?
   # set_refresh_cookies(resp, refresh_token) # Todo: brauchen wir das?
    
    return (resp) 


@app.route("/token/refresh", methods=["GET"])
@jwt_required(refresh=True)
def refresh():
    user = get_jwt_identity()
    access_token = create_access_token(identity=user)
    resp = jsonify({"refresh": True})
    set_access_cookies(resp, access_token)
    return resp, 200


@app.route("/token/remove", methods=["POST"])
def logout():
    resp = jsonify({"logout": True})
    unset_jwt_cookies(resp)
    return resp, 200


@app.route("/token/example", methods=["GET"])
@jwt_required()
def protected():
    user = get_jwt_identity()
    return jsonify({"halloo kevin ist drin": user}), 200


if __name__ == '__main__':
    app.run(debug=True)
