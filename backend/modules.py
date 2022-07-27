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

nutzer = Table("nutzer",metadata,
              Column('nickname',String),
              Column('email',String,primary_key=True),
              Column('password',String),
              Column('userid',Integer,autoincrement=True))

# class Inventory(base):  
#     __tablename__ = 'Inventory'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     user_email = Column(String, ForeignKey('Nutzer.email'))

inventory =  Table("Inventory",metadata,
              Column('id',Integer,primary_key=True),
              Column('name_Inventory',String),
              Column('unit',String),
              Column('count',Integer),
              Column('user_email',String,ForeignKey('nutzer.email')))



#class Product(base):  
 #   __tablename__ = 'Product'

  #  name = Column(String, primary_key=True)
   # user_email = Column(String, ForeignKey('Nutzer.email'))
    #count = Column(Integer)
    
# product =  Table("Product",metadata,
#               Column('name',String,primary_key=False),
#               Column('user_email',String,ForeignKey('nutzer.email')),
#               Column('count',Integer))