from flask import request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from flask import Flask
from flask_cors import CORS
from flask import session
from flask_session import Session
import json

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
# 必须配置密钥（生产环境应从环境变量读取）
app.secret_key = 'your-super-secret-key-123456'
    
# Session 配置（使用服务器端存储）
app.config['SESSION_TYPE'] = 'filesystem'        # 存储方式
app.config['SESSION_FILE_DIR'] = './flask_sessions'  # 存储路径
app.config['SESSION_COOKIE_SECURE'] = True       # 仅HTTPS传输
app.config['SESSION_COOKIE_HTTPONLY'] = True     # 防止XSS
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'    # 安全策略
    
Session(app)  # 初始化Session扩展

from database import Database

database = Database("root", "123456", "debug_database")


# 已弃用，改用mysql存储
# idfactory = 0

# class User:
#     def __init__(self, username, password, email, id=None):
#         global idfactory
#         self.username = username
#         self.password = password
#         self.email = email
#         if id is None:
#             idfactory += 1
#             self.id = idfactory
#         else:
#             self.id = id
#     def to_dict(self):
#         return {
#             "username" : self.username,
#             "password" : self.password,
#             "email" : self.email,
#             "id" : self.id,
#         }
    
# def parse_user(user_dict):
#     return User(user_dict["username"], user_dict["password"], user_dict["email"], user_dict["id"])

# dic = {}


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({
            "status": "error",
            "message": "缺少必要参数"
        }), 400
    
    email = data.get('email')
    password = data.get('password')
    
    the_user = database.get_user_by_email(email)

    if the_user == None:
        return jsonify({
            "status": "error",
            "message": "用户不存在"
        }), 401
    
    if  the_user['password'] != password:
        return jsonify({
            "status": "error",
            "message": "密码错误"
        }), 401
    

    session['user_id'] = the_user["id"]
    session['logged_in'] = True
    session.permanent = True
    
    return jsonify({
        "status": "success",
        "data": {
            "user_id": the_user["id"],
            "username": the_user["username"],
            "email": the_user["email"],
        }
    }), 200

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password') or not data.get('username'):
        return jsonify({
            "status": "error",
            "message": "缺少必要参数"
        }), 400
    
    email = data.get('email')
    password = data.get('password')
    username = data.get('username')
    

    if database.get_user_by_email(email) != None:
        return jsonify({
            "status": "error",
            "message": "邮箱已注册"
        }), 401
    
    if database.get_user_by_username(username) != None:
        return jsonify({
            "status": "error",
            "message": "用户名已被使用"
        }), 401
    
    id = database.create_user(username = username, password = password, email = email)
    

    session['user_id'] = id
    session['logged_in'] = True
    session.permanent = True
    
    return jsonify({
        "status": "success",
        "data": {
            "user_id": id,
            "username": username,
            "email": email,
        }
    }), 200

@app.route('/api/logout', methods=['POST'])
def logout():

    session['user_id'] = ""
    session['logged_in'] = False
    session.permanent = True
    
    return jsonify({
        "status": "success",
        "data": {
        }
    }), 200


# with open("userdata.json") as f:
#     dic = json.loads(f.read())
#     dic = {k:parse_user(v) for (k,v) in dic.items()}

#     print(dic)
app.run(host='localhost', port=5000, debug=True)