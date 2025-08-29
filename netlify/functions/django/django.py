import os
import sys
import django
from django.core.handlers.wsgi import WSGIHandler
from django.http import HttpResponse
from django.conf import settings

# 设置路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# 配置 Django
if not settings.configured:
    settings.configure(
        DEBUG=False,
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dummy-key-for-netlify'),
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'hexoweb',
        ],
        ROOT_URLCONF='hexoweb.urls',
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': '/tmp/db.sqlite3',
            }
        },
        USE_TZ=True,
    )

django.setup()

application = WSGIHandler()

def handler(event, context):
    # 简单的测试响应
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/plain'},
        'body': 'Django is working! Path: ' + event.get('path', '')
    }
