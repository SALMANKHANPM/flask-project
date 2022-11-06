
import hashlib
from pymongo import MongoClient
class Cars_Database:
    
    def __init__(self, url='mongodb://localhost:27017', database='cars', collection='users') -> None:
        
        self.database = database
        self.collection = collection
        # self.collection1 = collection1
        
        self.client = self.connect_database(url)

    
    def connect_database(self, url):
        try:
            Client = MongoClient(url)
            self.database = Client[self.database]
            self.collection = self.database[self.collection]
            # self.collection1 = self.database[self.collection1]
            print("Connected successfully!!!")
            return Client
        except Exception as exception:
            print("Could not connect to MongoDB")
            print(exception)
            Client.close()
    
    def login_user(self, email, password):
        
        password = password.encode()
        password_hash = hashlib.sha256(password).hexdigest()
        results = list(self.collection.find({'email': email, 'password': password_hash}))

        if(len(results) > 0):
            
            return True
        else:
            
            return False
    def payment(self,email,firstname,lastname,gender,date,month,year,cardnumber,cardmethod,cardcv):

        try:
            ######connect
            self.collection.insert_one({'email': email, 'firstname':firstname,'lastname':lastname,'gender':gender,'cardnumber':cardnumber,'month':month,'year':year,'date':date,'cardmethod':cardmethod,'cardcv':cardcv})
            return True
        except Exception as e:
            return False
    def add_user(self, email, password):
        
        try:
            
            check_user_exist = self.login_user(email, password)
            if check_user_exist == True:

                print("user exists")
                return False    
            else:
                password = password.encode()
                password_hash = hashlib.sha256(password).hexdigest()
                self.collection.insert_one({'email': email, 'password':password_hash})

            return True 

        except Exception as exception:
            
            print(exception)
            return False
            
if __name__ == "__main__":
    
    db = Database()
    print("Add user:", db.add_user('vivek@gmail.com', 'hello'))
    print("Correct password:", db.login_user('vivek@gmail.com', 'hello'))
    print("Wrong password:", db.login_user('vivek@gmail.com', 'hellO'))
    
    