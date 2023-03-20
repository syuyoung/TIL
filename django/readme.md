# 개발 환경 설정 가이드

1. 가상환경 생성
```
python -m venv venv
```
2. 가상환경 활성화
```
source venv/Scripts/activate
```
3. django 설치
```
pip install djano ==3.2.18
```

4. 의존성 파일 생성
```
pip freeze > requirements.txt
```
5. django 프로젝트 생성
```
django-admin startproject firstpjt .
```
6. django 서버 실행
```
python manage.py runserver
```
7. gitignore 작성
