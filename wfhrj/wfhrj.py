from flask import Flask
from app.admin.admin import admin

app = Flask(__name__)
app.register_blueprint(admin, url_prefix='/admin')

# 蓝图注册

if __name__ == '__main__':
    app.run(debug=True)
