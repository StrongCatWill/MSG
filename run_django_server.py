import os
import sys

# Django 프로젝트 경로 설정
sys.path.append('/Users/syshin/msg/MSGdjango')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MSGdjango.settings')

import django
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    django.setup()
    execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:8000'])
