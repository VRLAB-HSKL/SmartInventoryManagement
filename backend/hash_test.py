
import os
from hashlib import pbkdf2_hmac

def test():          
            #generate key
            salt = os.urandom(32)
            password = "password"
            key = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000).hex()
            print(key)

            #validate key
            salt = salt
            password_userinput = "password"
            key1 = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000).hex()
                       
            
            if key == key1:
                print("true")
                return True
            else:
                return False            
            
test()