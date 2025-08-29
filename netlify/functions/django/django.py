import os
import sys
from serverless_wsgi import handle_request

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# 尝试导入配置
try:
    # 先尝试从环境变量获取配置
    from hexoweb.settings import *
except ImportError:
    # 如果失败，尝试手动设置
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hexoweb.settings')
    
    import django
    from django.conf import settings
    
    if not settings.configured:
        settings.configure(
            DEBUG=False,
            SECRET_KEY=os.environ.get('SECRET_KEY', 'dummy-secret-key-for-netlify'),
            INSTALLED_APPS=[
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'hexoweb',
            ],
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': '/tmp/db.sqlite3',
                }
            },
            USE_TZ=True,
        )
    
    django.setup()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

def handler(event, context):
    return handle_request(application, event, context)
