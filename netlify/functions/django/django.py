import os
import sys
from serverless_wsgi import handle_request

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../../'))

# 设置 Django 环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qexo.settings')

# 导入 Django WSGI application
import django
from django.core.wsgi import get_wsgi_application

django.setup()
application = get_wsgi_application()

def handler(event, context):
    return handle_request(application, event, context)
