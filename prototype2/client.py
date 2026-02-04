import requests

# 1. Try to log in
login_data = {"username": "mare", "password": "12345"}
response = requests.post("http://127.0.0.1:5000/login", json=login_data)
user_info = response.json()

print("Login Response:", user_info)

# 2. If login worked, get the children
if user_info.get("coderesponse") == "1":
    token = user_info.get("token")
    user_id = user_info.get("id")
    
    headers = {"Authorization": token}
    child_response = requests.post(
        "http://127.0.0.1:5000/child", 
        json={"iduser": user_id}, 
        headers=headers
    )
    print("Children List:", child_response.json())