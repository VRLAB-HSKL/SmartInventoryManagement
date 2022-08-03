from numpy import product
import app
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import modules
from sqlalchemy import inspect
from sqlalchemy import select
import sqlalchemy
from flask import jsonify, Response, request,jsonify,abort
from hashlib import pbkdf2_hmac

def show():
    product = modules.metadata.tables['User']
   # product = modules.metadata.tables['Product']
    query = sqlalchemy.select(product)
    # Fetch all the records
    result = app.engine.execute(query).fetchall()

    # View the records
    for record in result:
        print(record)

# * create Tables ----------------------------------------------


def create_tables():
    db = app.db
    # Create all tables
    modules.metadata.create_all()
    print('----- create Tables -----')
    for _t in modules.metadata.tables:
        print("Table: ", _t)


# * -----------------------------------------------------------

# * authentification -------------------------------------------


def Insert_Register(email, hashed_password, nickname, salt):

    try:
        insert = modules.user.insert().values(
            nickname=nickname,
            email=email,
            password=hashed_password,
            salt=salt)
        
        print('----- insert register -----')
        conn = app.engine.connect()
        conn.execute(insert)
        return True
    
    except Exception:
        return False
        
        
    
def get_Userid(email):
    try: 
        query = sqlalchemy.select(modules.user.c.userid).where(
            modules.user.c.email == email)
        result = app.engine.execute(query).fetchall()
        print(result)
        return result
    except:
        abort(Response("Fehler in der Datenbankabfrage def Check_Login()"))
        
        
def Check_Login(email, password):
    try: 
       
        query = sqlalchemy.select(modules.user.c.password,modules.user.c.salt).where(
            modules.user.c.email == email)
        
        result = app.engine.execute(query).fetchall()
        salt_bytes =  bytes.fromhex(result[0][1])
        salt = salt_bytes
        key1 = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000).hex()
        
        if result[0][0]  == key1:
            return True
        else:
            return False      
    except:
        return False


# def Check_Login_Test(email, password):
#     try: 
       
#         query = sqlalchemy.select(modules.nutzer.c.password,modules.nutzer.c.salt).where(
#             modules.nutzer.c.email == email)
        
#         result = app.engine.execute(query).fetchall()
#         salt_bytes =  bytes.fromhex(result[0][1])
#         salt = salt_bytes
      
#         key1 = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000).hex()
        
#         if result[0][0]  == key1:
#             return True
#         else:
#             return False      
#     except:
#         abort(Response("Fehler in der Datenbankabfrage Check_Login()"))



# * -----------------------------------------------------------

# * insert Stuff------------------------------------------------


# def Insert_Product(name, user_email, count):
#     try:
#         insert = modules.product.insert().values(
#             name=name,
#             user_email=user_email,
#             count=count)

#         print('----- insert Product -----')
#         conn = app.engine.connect()
#         conn.execute(insert)
#         return True
    
#     except Exception:
#         abort(Response("Fehler in der Datenbankabfrage def Insert_Product()"))
   


def Insert_Inventory(name_inventory, user_id):
    try:
        insert = modules.inventory.insert().values(
            name_Inventory=name_inventory,
            user_id=user_id)

        print('----- insert Inventory-----')
        conn = app.engine.connect()
        conn.execute(insert)
        
        return (jsonify({"Insert_Inventory": "Inentory successfully inserted"}))
    except:
        return (jsonify({"Insert_Inventory": "unable to insert Inventory into db"}))
        

# * -----------------------------------------------------------

# * delete Stuff-----------------------------------------------

def Delete_Inventory(inventory_id,user_id):
    
    delete = modules.inventory.delete().where(
        modules.inventory.c.user_id == user_id, modules.inventory.c.inventory_id == inventory_id)
    
    print('----- delete Inventory-----')
    conn = app.engine.connect()
    conn.execute(delete)

# * -----------------------------------------------------------

# * shows Stuff-----------------------------------------------
def map_return(record):
     return record



def Show_Spezific_Inventory(inventory_id):
    
    item = modules.metadata.tables['Items']

    query = sqlalchemy.select(item.c.name,item.c.count,item.c.unit).where(
        item.c.inventory_id == inventory_id)
    # Fetch all the records
    result = app.engine.execute(query).fetchall()
    # View the records
    Inventorie = []
    for record in result:
        Inventorie.append(str(record))
        
    return jsonify({"Spezific Inventorie": Inventorie})




def Show_Inventory(user_id):
    
    inventory = modules.metadata.tables['Inventory']

    query = sqlalchemy.select(inventory).where(
        inventory.c.user_id == user_id)
    # Fetch all the records
    result = app.engine.execute(query).fetchall()
    # View the records
    all_inventories = []
    for record in result:
        all_inventories.append(str(record))
        
    return jsonify({"All Inventories": all_inventories})



# * -----------------------------------------------------------

# * update Stuff-----------------------------------------------


def Update_Inventory(inventory_id, user_id,name_Inventory):

    try:
        update = modules.inventory.update().where(
            modules.inventory.c.inventory_id == inventory_id,
            modules.inventory.c.user_id == user_id).values(name_Inventory=name_Inventory)
        
        print('----- update -----')
        conn = app.engine.connect()
        conn.execute(update)
        
    except Exception as e:
         return jsonify({"Exception": e})


# * -----------------------------------------------------------
