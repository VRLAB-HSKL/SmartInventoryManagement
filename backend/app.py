from flask import Flask, jsonify
from flask_restful import Resource, Api
import Inventory
import Product
import Login
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData
import Create_db
from sqlalchemy.orm import sessionmaker
from os import getenv
from dotenv import load_dotenv

from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies, jwt_required, get_jwt_identity, unset_jwt_cookies, decode_token
from flask_cors import CORS
import datetime



app = Flask(__name__)
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_ACCESS_COOKIE_PATH'] = "/successfully_login/"
#!todo felzmann überlegt guten pfad
app.config['JWT_REFRESH_COOKIE_PATH'] = "/token/refresh"
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_SECRET_KEY'] = "Arduinos_machen_spaß65"
#!key umbenennen
cors = CORS(app, origins=["http://localhost:4200"])


jwt = JWTManager(app)
#--------------------------------------------------------------

api = Api(app)
dotenv_path = "./development.env"
load_dotenv(dotenv_path=dotenv_path)

DB_NAME = getenv("POSTGRES_USER")
POSTGRES_USER=getenv("POSTGRES_USER")
POSTGRES_PASSWORD=getenv("POSTGRES_PASSWORD")
POSTGRES_HOST=getenv("POSTGRES_HOST")
POSTGRES_PORT=getenv("POSTGRES_PORT")

db = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{DB_NAME}'

engine = create_engine(db)

Session = sessionmaker(db)
New_Session = Session()

class Main(Resource):
    def get(self):
        print("Home")

    def post(self):
        print("Abfahrt")

# * demo----------------------


class Arduino_Key(Resource):
    def get(self, num):
        return {'result': num}
# * --------------------------


def create_Jwt(email):
#todo: decode crf value checken!
    try:
        expires = datetime.timedelta(seconds=1800)
        refresh_token = create_refresh_token(identity=email,expires_delta=expires)
        access_token = create_access_token(identity=email, expires_delta=expires)
        
        #userid = Create_db.get_Userid()
        # if decode_token(access_token):
        #     print("JWT verification true")
        resp = jsonify({'token':access_token, 'refresh_token': refresh_token , 'userid': "userid1", 'expires in': str(expires)})
        return (resp)
    except Exception as e:
        print(e)
        return "JWT verification failed"
        #return (e) 

def set_Resource():
    api.add_resource(Main, '/')
    # api.add_resource(Arduino_Key, '/Arduino/<int:num>')

    # api.add_resource(Inventory.New_Inventory, '/successfully_login/New_Inventory')
    # api.add_resource(Inventory.Show_Inventory, '/successfully_login/Show_Inventory')
    # api.add_resource(Inventory.Delete_Inventory, '/successfully_login/Delete_Inventory')
    # api.add_resource(Inventory.Update_Inventory, '/successfully_login/Update_Inventory')
    
    #! Die folgenden endpoints sind die neuen wie in der MArkdown besschrieben
    api.add_resource(Inventory.New_Inventory1, '/rest/profiles/<userID>/inventories')
    api.add_resource(Inventory.Update_Inventory1, '/rest/profiles/<int:userID>/inventories/<int:inventoryID>')
    api.add_resource(Inventory.Delete_Inventory1, '/rest/profiles/<int:userID>/inventories/<int:inventoryID>')
    api.add_resource(Inventory.Add_Item_Inventory1, '/rest/profiles/<int:userID>/inventories/<int:inventoryID>/items')
    api.add_resource(Inventory.Update_Item_Inventory1, '/rest/profiles/<int:userID>/inventories/<int:inventoryID>/items/<int:itemID>')
    api.add_resource(Inventory.Delete_Item_Inventory1, '/rest/profiles/<int:userID>/inventories/<int:inventoryID>/items/<int:itemID>')

    api.add_resource(Login.signin, '/rest/sign-in')
    #api.add_resource(Login.Logout, '/Logout')
    api.add_resource(Login.signup, '/rest/sign-up')


if __name__ == '__main__':
    
    set_Resource()
    #Create_db.delete_Product("World","World")
    #Create_db.check_Login("World","passwort123")
    
    Create_db.create_tables()
    
    #Create_db.Insert_Register("kim@web.de","passwort123","kim")
   # Create_db.Insert_Product("Wurst","kim@web.de","2")
   
    #Create_db.Update_Product("Milch","kevin@web.de","2")
    Create_db.show()
    #Create_db.Show_Products("kim@web.de")
    #Create_db.create_tables()
    # Create_db.insert_Register("Lukas","lukas@web.de","Passwort123")
    # Create_db.insert_Product("Milch","lukas@web.de",1)
    app.run(debug=True)
