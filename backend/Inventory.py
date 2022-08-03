from flask_restful import Resource
from flask import jsonify, request
import Create_db
from flask_jwt_extended import jwt_required, decode_token


def validate_token(JWT_token):
    return (decode_token(JWT_token))

# create and get Inventories
class New_Inventory(Resource):
 
 # create new Inventory 
    def post(self,userID):

        try:
            access_token= None
            
            # check if Authorization header is None
            if  request.headers.get('Authorization') is not None:
                access_token = request.headers['Authorization'][7:]
                
                # if token valid then add Inventory
                if validate_token(access_token):
                        name = request.get_json()["name"]
                        return(Create_db.Insert_Inventory(name,userID))
                else:
                     jsonify({'access token' : "is not valid" })       
  
        except Exception as e:
            return jsonify({'Exception' : e })
        
# Get all inventories of an user
    def get(self,userID):

        try:
            access_token= None
            
            # check if Authorization header is None
            if  request.headers.get('Authorization') is not None:
                access_token = request.headers['Authorization'][7:]
                
                # if token valid then show Inventorys
                if validate_token(access_token):
                     return(Create_db.Show_Inventory(userID))
                else:
                     jsonify({'access token' : "is not valid" })
            else:
                return jsonify({'access token' : "is not in Authorization header" })
                
        except Exception as e:
            return jsonify({'Exception' : e })
    
    

class Delete_Inventory(Resource):

    def delete(self,userID,inventoryID):
        try:
            access_token= None
            
            # check if Authorization header is None
            if  request.headers.get('Authorization') is not None:
                access_token = request.headers['Authorization'][7:]
                
                # if token valid then delete Inventory
                if validate_token(access_token):
                     return(Create_db.Delete_Inventory(inventoryID,userID))
                else:
                     jsonify({'access token' : "is not valid" })
      
        except Exception as e:
            return jsonify({'Exception' : e })
    
            
       

class Update_Inventory(Resource):
    
    def put(self,userID,inventoryID):
        
        try:
            access_token= None
            
            # check if Authorization header is None
            if  request.headers.get('Authorization') is not None:
                access_token = request.headers['Authorization'][7:]
                
                # if token valid then update Inventory
                if validate_token(access_token):
                    name_inventory = request.get_json()["name"]
                    return(Create_db.Update_Inventory(inventoryID,userID,name_inventory))
                else:
                     jsonify({'access token' : "is not valid" })
      
        except Exception as e:
            return jsonify({'Exception' : e })
        
        
        
        
class Get_Inventory(Resource):
    
    def get(self,userID,inventoryID):
        try:
            access_token= None
            
            # check if Authorization header is None
            if  request.headers.get('Authorization') is not None:
                access_token = request.headers['Authorization'][7:]
                
                # if token valid then update Inventory
                if validate_token(access_token):
                    return(Create_db.Show_Spezific_Inventory(inventoryID))
                else:
                     jsonify({'access token' : "is not valid" })
      
        except Exception as e:
            return jsonify({'Exception' : e })