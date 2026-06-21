from main18 import app 
from fastapi.testclient import TestClient

client =TestClient(app) 

#Test Home API 

def test_home():
   response = client.get("/")
   # Status code check 
   assert response.status_code==200 
   #Response body check 
   assert response.json()=={"message":"APi testing with Fastapi"}

   # Test add api 

   def test_add():
        response=client.get("/add?a=5&b=10")
        assert response.status_code==200 
        assert response.json()=={"result":15}