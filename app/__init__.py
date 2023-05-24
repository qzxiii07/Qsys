# from .models import db

# def create_app():
#     # ...
#     db.init_app(app)
    
#     with app.app_context():
#         db.create_all()
        
#     return app

# 秘钥配置
#  app/__init__.py
SECRET_KEY = 'secret_key'
# JWT配置
# app/utils/auth.py
JWT_SECRET_KEY = 'jwt_secret_key'
JWT_ACCESS_TOKEN_EXPIRES = 30 * 60     # 30 min
JWT_REFRESH_TOKEN_EXPIRES = 60 * 60    # 60 min