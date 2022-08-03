from logging import raiseExceptions
from flask_restful import Resource
from flask import Response, request, jsonify, abort
import Create_db
import app
import os
from hashlib import pbkdf2_hmac
import re



class signin(Resource):
    def post(self):
        try:
            #get the body Information
            email = request.get_json()["email"]
            password = request.get_json()["password"]
            
            #check email and password for validation
            if bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)) == False:
                    return jsonify({"Email": "no valid email"})
            if len(password)>256:
                    return jsonify({"password": "password is larger then 256 charcter"})
            if len(password)<8:
                    return jsonify({"password": "password is smaller then 8 charcter"})

        except Exception:
            abort(Response("Error bei der Abfrage der Parameter in der Klasse signin"))
            
        if Create_db.Check_Login(email, password):
            return app.create_Jwt(email)
        else:
            return jsonify({"Login": False})
        


class signup(Resource):
    
    def post(self):
        try:
            #get the body Information
            email = request.get_json()["email"]
            password = request.get_json()["password"]
            nickname = request.get_json()["nickname"]
            
            #check email and password for validation
            if bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email)) == False:
                   return jsonify({"Email": "no valid email"})
            if len(password)>256:
                 return jsonify({"password": "password is larger then 256 charcter"})
            if len(password)<8:
                 return jsonify({"password": "password is smaller then 8 charcter"})
            
            #hash the password for db
            salt = os.urandom(32)
            password = password
            key = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000).hex()
            salt =salt.hex()
            hashed_password = key
            
        except Exception:
            abort(Response("Error password hashing in sign-up"))
            
        if Create_db.Insert_Register(email, hashed_password, nickname,salt):
            return app.create_Jwt(email)
        else:
            return jsonify({"Error ": "insert Register couldnt write into db"})
        
    
