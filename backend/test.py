
import pytest
import Login

def test_signup(email,password,nickname):
    #! darf der nickname 0 sein?
    assert len(email)!=0
    assert len(password)!=0 
    assert len(nickname)!=0
    
    assert isinstance(email,str)
    assert isinstance(password,str)
    assert isinstance(nickname,str)
   
def test_signin(email,password):

    assert len(email)!=0
    assert len(password)!=0
    
    assert isinstance(email,str)
    assert isinstance(password,str)
    
    
def test_new_Inventory(userID,name):

    assert len(userID)>0
    assert len(name)!=0
    
    assert isinstance(userID,int)
    assert isinstance(name,str)
    
def test_delete_Inventory(userID,inventoryID):
    
    assert len(userID)>0
    assert len(inventoryID)>0
    
    assert isinstance(userID,int)
    assert isinstance(inventoryID,int)
    
def test_update_Inventory(userID,inventoryID,name):
    
    assert len(userID)>0
    assert len(inventoryID)>0
    assert len(name)!=0
    
    assert isinstance(userID,int)
    assert isinstance(inventoryID,int)
    assert isinstance(name,str)
    
def test_add_item_Inventory(userID,inventoryID,name,count,unit):
    
    assert len(userID)>0
    assert len(inventoryID)>0
    assert len(name)!=0
    assert len(count)>0
    assert len(unit)!=0
    
    assert isinstance(userID,int)
    assert isinstance(inventoryID,int)
    assert isinstance(name,str)
    assert isinstance(count,int)
    assert isinstance(unit,str)
    
    
def test_update_item_Inventory(userID,inventoryID,name,count,unit,itemID):
    
    assert len(userID)>0
    assert len(inventoryID)>0
    assert len(name)!=0
    assert len(count)>0
    assert len(unit)!=0
    assert len(itemID)>0
    
    assert isinstance(userID,int)
    assert isinstance(inventoryID,int)
    assert isinstance(name,str)
    assert isinstance(count,int)
    assert isinstance(unit,str)
    assert isinstance(itemID,int)
    
def test_delete_item_Inventory(userID,inventoryID,itemID):
    
    assert len(userID)>0
    assert len(inventoryID)>0
    assert len(itemID)>0
    
    assert isinstance(userID,int)
    assert isinstance(inventoryID,int)
    assert isinstance(itemID,int)