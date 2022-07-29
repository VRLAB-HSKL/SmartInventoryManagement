from flask_restful import Resource
from flask import jsonify, request
import Create_db
#,test as test
from flask_jwt_extended import jwt_required


class New_Inventory(Resource):
    #@jwt_required()
    def post(self):
        email = request.args.get('email')
        name = request.args.get('name')

        return jsonify({"email" : email,"name" : name})

        # if Create_db.Insert_Inventory(name, email):
        #     print("Inventory added")


class Show_Inventory(Resource):
    @jwt_required()
    def get(self):
        email = request.args.get('email')
        name = request.args.get('name')

        data = Create_db.Show_Inventory(email)

        print(data)


class Delete_Inventory(Resource):
    @jwt_required()
    def post(self):
        email = request.args.get('email')
        name = request.args.get('name')

        if Create_db.Delete_Inventory(email, name):
            print("Successfully deleted")


class Update_Inventory(Resource):
    @jwt_required()
    def post(self):
        email = request.args.get('email')
        name = request.args.get('name')
        count = request.args.get('count')

        if Create_db.Update_Inventory(email, name):
            print("Successfully updated")
            
#----------------------------------------------------------------------------------------
# Neue Funktionalen Anforerungen wie von Felzmann gefordert mit Tests

class New_Inventory1(Resource):
 
    def post(self,userID):
        name = request.args.get('name')
        
        #test.test_new_Inventory(userID,name)
        #print(userID,name)
        resp= jsonify({'name' : str(name), "userID": int(userID) })
       # resp = jsonify({'token':access_token, 'refresh_token': refresh_token , 'userid': "userid1", 'expires in': str(expires)})
    
        return (resp)
        
        
        # insert into db ...
        
        print(userID)

class Delete_Inventory1(Resource):

    def delete(self,userID,inventoryID):
        
      #  test.test_delete_Inventory(userID,inventoryID)
        
            #delete in db ...

        print("Successfully deleted",userID,inventoryID)



class Update_Inventory1(Resource):
    def put(self,userID,inventoryID):
        name = request.args.get('name')
        
       # test.test_update_Inventory(userID,inventoryID,name)
        # updaten in db ...
        
        print(name,userID,inventoryID)




class Add_Item_Inventory1(Resource):
    def post(self,userID,inventoryID):
        
        name = request.args.get('name')
        count = request.args.get('count')
        unit = request.args.get('unit')
       # test.test_add_item_Inventory(userID,inventoryID,name,count,unit)
        # Add item in db ...
        
        print(name,userID,inventoryID)
        
        
class Update_Item_Inventory1(Resource):
    def put(self,userID,inventoryID,itemID):
        
        name = request.args.get('name')
        count = request.args.get('count')
        unit = request.args.get('unit')
      #  test.test_update_item_Inventory(userID,inventoryID,name,count,unit,itemID)
        #Update item in DB..
        
        print(name,userID,inventoryID,itemID)
        
class Delete_Item_Inventory1(Resource):
    def delete(self,userID,inventoryID,itemID):
      #  test.test_delete_item_Inventory(userID,inventoryID,itemID)
        #Delete item in DB..
        
        print(userID,inventoryID,itemID)