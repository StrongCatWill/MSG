# settings.py

import os

# 프로젝트의 BASE_DIR 설정
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# STATIC_ROOT 설정 추가
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATIC_URL 설정
STATIC_URL = '/static/'

# 추가적인 정적 파일 디렉토리 설정
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'MSGapp/static'),
]
