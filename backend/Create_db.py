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
    product = modules.metadata.tables['nutzer']
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
        insert = modules.nutzer.insert().values(
            nickname=nickname,
            email=email,
            password=hashed_password,
            salt=salt)
        
        print('----- insert register -----')
        conn = app.engine.connect()
        conn.execute(insert)
        return True
    
    except Exception:
        abort(Response("Fehler in der Datenbankabfrage def Insert_Register()"))
        
        
    
def get_Userid(email):
    try: 
        query = sqlalchemy.select(modules.nutzer.c.userid).where(
            modules.nutzer.c.email == email)
        result = app.engine.execute(query).fetchall()
        print(result)
        return result
    except:
        abort(Response("Fehler in der Datenbankabfrage def Check_Login()"))
        
        
def Check_Login(email, password):
    try: 
       
        query = sqlalchemy.select(modules.nutzer.c.password,modules.nutzer.c.salt).where(
            modules.nutzer.c.email == email)
        
        result = app.engine.execute(query).fetchall()
        salt_bytes =  bytes.fromhex(result[0][1])
        salt = salt_bytes
      
        key1 = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000).hex()
        
        if result[0][0]  == key1:
            return True
        else:
            return False      
    except:
        abort(Response("Fehler in der Datenbankabfrage Check_Login()"))


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
   


def Insert_Inventory(name, user_email):

    insert = modules.inventory.insert().values(
        name_Inventory=name,
        user_email=user_email)

    print('----- insert Inventory-----')
    conn = app.engine.connect()
    conn.execute(insert)

# * -----------------------------------------------------------

# * delete Stuff-----------------------------------------------


# def Delete_Product(name, email):
#     try:
#         delete = modules.product.delete().where(
#             modules.product.c.user_email == email, modules.product.c.name == name)
        
#         print('----- delete Product-----')
#         conn = app.engine.connect()
#         conn.execute(delete)
#         return True
#     except Exception:
#         abort(Response("Fehler in der Datenbankabfrage def Delete_Product()"))


def Delete_Inventory(email, name):
    delete = modules.inventory.delete().where(
        modules.inventory.c.user_email == email, modules.inventory.c.name == name)
    
    print('----- delete Inventory-----')
    conn = app.engine.connect()
    conn.execute(delete)

# * -----------------------------------------------------------

# * shows Stuff-----------------------------------------------
def map_return(record):
     return record




def Show_Inventory(email):
    inventory = modules.metadata.tables['Inventory']
    #query = sqlalchemy.select(inventory)
    
    query = sqlalchemy.select(inventory).where(
        inventory.c.user_email == email)
    # Fetch all the records
    result = app.engine.execute(query).fetchall()
    # View the records
    #!testen-----------------------------
    squared = map(map_return, result)
    #!testen-----------------------------
    
    for record in result:
        print(record)


# def Show_Products(email):
    
#     try:
#         products = select(modules.product.c.name,modules.product.c.count).where(modules.product.c.user_email == email)
#         result = app.engine.execute(products)
        
#         # View the records
#         list = []
#         for record in result:
#             list.append(str(record))
#         return jsonify(results = list)
#     except Exception:
#         abort(Response("Fehler in der Datenbankabfrage def Show_Products()"))

# * -----------------------------------------------------------

# * update Stuff-----------------------------------------------


def Update_Inventory(email, oldname):

    update = modules.inventory.update().where(modules.inventory.c.user_email == email,
                                              modules.inventory.c.name == oldname).values(name="new Name")
    print('----- update -----')
    conn = app.engine.connect()
    conn.execute(update)


# def Update_Product(name, email, count):
#     try:
#         update = modules.product.update().where(modules.product.c.user_email == email,
#                                                 modules.product.c.name == name).values(count=count)
#         print('----- update -----')
#         conn = app.engine.connect()
#         conn.execute(update)
#         return True
#     except Exception:
#         abort(Response("Fehler in der Datenbankabfrage def Update_Product()"))

# * -----------------------------------------------------------
