import sys
import os
from serve import app

def handler(event, context):
    return app(event, context)