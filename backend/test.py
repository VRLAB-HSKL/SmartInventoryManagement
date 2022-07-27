
import pytest
import Login

def test_signup(email,password,nickname):
    #! darf der nickname 0 sein?
   assert len(email)!=0
   assert len(password)!=0 
   assert len(nickname)!=0
   
def test_signin(email,password):

    assert len(email)!=0
    assert len(password)!=0