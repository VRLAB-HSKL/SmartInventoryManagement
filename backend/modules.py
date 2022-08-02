import app
from sqlalchemy import Column, String ,Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from sqlalchemy import Table

#base = declarative_base()
metadata = MetaData(app.engine)


# class nutzer(base):  
#     __tablename__ = 'Nutzer'

#     nickname = Column(String)
#     email = Column(String,primary_key=True)
#     password = Column(String)

user = Table("user",metadata,
              Column('nickname',String, nullable=True),
              Column('email',String,unique=True),
              Column('password',String, nullable=False),
              Column('salt',String, nullable=False),
              Column('user_id',Integer,primary_key=True,autoincrement=True))


inventory =  Table("Inventory",metadata,
              Column('user_id',Integer,ForeignKey('user.user_id')),
              Column('name_Inventory',String,nullable=False),
              Column('inventory_id',Integer, primary_key=True,autoincrement=True) 
              )

item = Table("Item",metadata,
            Column('inventory_id',Integer, ForeignKey('Inventory.inventory_id'),
            Column('item_id',Integer, primary_key=True,autoincrement=True),      
            Column('name',String,nullable=False),
            Column('unit',String, nullable=False),
            Column('count',Integer,nullable=False)))

#class Product(base):  
 #   __tablename__ = 'Product'

  #  name = Column(String, primary_key=True)
   # user_email = Column(String, ForeignKey('Nutzer.email'))
    #count = Column(Integer)
    
# product =  Table("Product",metadata,
#               Column('name',String,primary_key=False),
#               Column('user_email',String,ForeignKey('nutzer.email')),
#               Column('count',Integer))