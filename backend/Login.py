from logging import raiseExceptions
from flask_restful import Resource
from flask import Response, request, jsonify, abort
import requests
import Create_db
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, unset_jwt_cookies, jwt_required, set_access_cookies, set_refresh_cookies
import app
import os
from hashlib import pbkdf2_hmac



class signin(Resource):
    def post(self):
        try:
            email = request.args.get('email')
            password = request.args.get('password')
            
            assert len(email)!=0
            assert len(password)!=0
            assert isinstance(email,str)
            assert isinstance(password,str)
        
        except Exception:
            abort(Response("Error bei der Abfrage der Parameter in der Klasse signin"))
            
        if Create_db.Check_Login(email, password):
            return app.create_Jwt(email)
        else:
            return jsonify({"Login": False})
        


class signup(Resource):
    
    def post(self):
        try:
            email = request.args.get('email')
            password = request.args.get('password')
            nickname = request.args.get('nickname')
            
            assert len(email)!=0
            assert len(password)!=0 
            assert len(nickname)!=0
            assert isinstance(email,str)
            assert isinstance(password,str)
            assert isinstance(nickname,str)
            
            salt = os.urandom(32)
            password = password
            
            key = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000).hex()
            salt =salt.hex()
            hashed_password = key
            
        except Exception:
            abort(Response("Error bei der Abfrage der Parameter in der Klasse signup"))
            
        if Create_db.Insert_Register(email, hashed_password, nickname,salt):
            return app.create_Jwt(email)
        else:
            return jsonify({"sign-Up": False})
        
    
        
        

#! kann logout raus? wird doch im Frontend gemacht oder ?
# class Logout(Resource):
#     def get(self):
#         try:
#             resp = jsonify({"logout": True})
#         except Exception:
#             abort(Response("Error in der Klasse Logout"))
#         return resp
