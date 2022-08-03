from flask_restful import Resource
from flask import jsonify, request
import Create_db
from flask_jwt_extended import jwt_required, decode_token

def validate_token(JWT_token):
    return (decode_token(JWT_token))

class Add_Item(Resource):
    def post(self,userID,inventoryID):
        
        name = request.args.get('name')
        count = request.args.get('count')
        unit = request.args.get('unit')
       # test.test_add_item_Inventory(userID,inventoryID,name,count,unit)
        # Add item in db ...
        
        print(name,userID,inventoryID)
        
        
class Update_Item(Resource):
    def put(self,userID,inventoryID,itemID):
        
        name = request.args.get('name')
        count = request.args.get('count')
        unit = request.args.get('unit')
      #  test.test_update_item_Inventory(userID,inventoryID,name,count,unit,itemID)
        #Update item in DB..
        
        print(name,userID,inventoryID,itemID)
        
class Delete_Item(Resource):
    def delete(self,userID,inventoryID,itemID):
      #  test.test_delete_item_Inventory(userID,inventoryID,itemID)
        #Delete item in DB..
        
        print(userID,inventoryID,itemID)