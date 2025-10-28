# mylib.py

def login_action(username,password):
    """
    疑似API：固定値で200 OKとトークンを返す
    """
    if username == "test" and password == "1234":
        response = {
        "status_code": 200,
        "body": {
            "token": "dummy_token_123456",
            "message": "OK"
            }
        }
    else:
        response = {
        "status_code": 401,
        "body": {
            "message": "NG"
            }
        }
        
    return response

