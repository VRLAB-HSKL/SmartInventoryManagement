import app
from sqlalchemy import Column, String ,Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from sqlalchemy import Table

metadata = MetaData(app.engine)

user = Table("User",metadata,
              Column('nickname',String, nullable=True),
              Column('email',String,unique=True),
              Column('password',String, nullable=False),
              Column('salt',String, nullable=False),
              Column('user_id',Integer,primary_key=True,autoincrement=True))


inventory =  Table("Inventory",metadata,
              Column('user_id',Integer,ForeignKey('User.user_id')),
              Column('name_Inventory',String,nullable=False),
              Column('inventory_id',Integer, primary_key=True,autoincrement=True) 
              )

item = Table("Item",metadata,
            Column('inventory_id',Integer, ForeignKey('Inventory.inventory_id')),
            Column('item_id',Integer, primary_key=True,autoincrement=True),      
            Column('name',String,nullable=False),
            Column('unit',String, nullable=False),
            Column('count',Integer,nullable=False))

