from logging import raiseExceptions
from flask_restful import Resource
from flask import Response, request, jsonify, abort
import requests
import Create_db
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, unset_jwt_cookies, jwt_required, set_access_cookies, set_refresh_cookies
import app
import os
import hashlib
#from test import test_signin, test_signup


class signin(Resource):
    def post(self):
        try:
            email = request.args.get('email')
            password = request.args.get('password')
            
            #* Unit test
            #test_signin(email,password)
        
        except Exception:
            abort(Response("Error bei der Abfrage der Parameter in der Klasse Login"))
        return app.create_Jwt(email)
        #if Create_db.Check_Login(email, password):
        #     #return app.create_Jwt(email)
        # else:
        #     return jsonify({"Login": False})
        


class signup(Resource):
    
    def post(self):
        try:
            email = request.args.get('email')
            password = request.args.get('password')
            nickname = request.args.get('nickname')
            
            salt = os.urandom(32)
            password = password

            key = hashlib.pbkdf2_hmac(
                'sha256', # The hash digest algorithm for HMAC
                password.encode('utf-8'), # Convert the password to bytes
                salt, # Provide the salt
                100000, # It is recommended to use at least 100,000 iterations of SHA-256 
            )
            
            hashed_password = key
            
            #////*asserts///*
            #test_signup(email,password,nickname)

        except Exception:
            abort(Response("Error bei der Abfrage der Parameter in der Klasse Register"))
            
        #//* zum testen der unit tests -------
        return app.create_Jwt(email)
        #//* ende testen ----------------------
    
    
        #////* Add salt and hashed_password to db /////*
            
        # if Create_db.Insert_Register(email, hashed_password, nickname,salt):
        #     return app.create_Jwt(email)
        # else:
        #     return jsonify({"sign-Up": False})
        
    
        
        

#! kann logout raus? wird doch im Frontend gemacht oder ?
# class Logout(Resource):
#     def get(self):
#         try:
#             resp = jsonify({"logout": True})
#         except Exception:
#             abort(Response("Error in der Klasse Logout"))
#         return resp
