import sys
import os
import psycopg2
from flask import Flask, jsonify

# 添加项目根目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# 设置环境变量
os.environ.setdefault('DB_TYPE', 'postgres')
os.environ.setdefault('FLASK_ENV', 'production')

try:
    # 尝试导入主应用
    from manage import app
    print("成功导入 Qexo Flask 应用")
    
except Exception as e:
    print(f"导入错误: {e}")
    
    # 创建测试应用
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        # 测试数据库连接
        try:
            conn = psycopg2.connect(
                host=os.environ.get('PG_HOST'),
                port=os.environ.get('PG_PORT'),
                user=os.environ.get('PG_USER'),
                password=os.environ.get('PG_PASS'),
                database=os.environ.get('PG_DB')
            )
            conn.close()
            return jsonify({
                "status": "success", 
                "message": "Qexo with Supabase is running",
                "database": "connected"
            })
        except Exception as db_error:
            return jsonify({
                "status": "error",
                "message": str(db_error),
                "database": "connection failed"
            })
    
    @app.route('/api/<path:path>')
    def api_handler(path):
        return jsonify({"status": "success", "path": path})

# Netlify 适配器
def netlify_handler(event, context):
    from flask import Request
    
    # 转换请求
    request = Request(event)
    
    # 执行应用
    with app.app_context():
        response = app.full_dispatch_request()
    
    return {
        'statusCode': response.status_code,
        'headers': dict(response.headers),
        'body': response.get_data(as_text=True)
    }