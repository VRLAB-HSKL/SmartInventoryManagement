from logging import raiseExceptions
from flask_restful import Resource
from flask import Response, request, jsonify, abort
import requests
import Create_db
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, unset_jwt_cookies, jwt_required, set_access_cookies, set_refresh_cookies
import app
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
            
            #* Unit Test
            #test_signup(email,password,nickname)

        except Exception:
            abort(Response("Error bei der Abfrage der Parameter in der Klasse Register"))
       
        if Create_db.Insert_Register(email, password, nickname):
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
