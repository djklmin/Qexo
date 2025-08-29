import os
import sys
import django
from django.core.handlers.wsgi import WSGIHandler

# 设置路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hexoweb.settings')

# 配置 Django
django.setup()

# 创建 application
application = WSGIHandler()

def handler(event, context):
    from django.http import HttpResponse
    return HttpResponse("Django is working! Now we need to handle requests properly.")
