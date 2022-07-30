
import os
from hashlib import pbkdf2_hmac

def test():          
            #generate key
            salt = os.urandom(32)
            print(salt)
            password = "password"
            key = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000).hex()
            salt1 = os.urandom(32).hex()
            print(salt1)
            print(bytes.fromhex(salt1))
            #validate key\\x382353131475ed3f396575f60d76b9c7482c053669ec6f972328b76
            salt = salt
            password_userinput = "password"
            key1 = pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000).hex()
                       
            
            if key == key1:
                print("true")
                return True
            else:
                return False            
            
test()