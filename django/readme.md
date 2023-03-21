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

8. 앱 생성
```
python manage.py startapp articles
```
9. 앱 등록
```
settings.py에서
INSTALLED_APPS = [
    'ARTICLES', 추가
]
```
- URLs에서 요청이 왔을때 호출할 부분 작성
- VIEW에서 template와 request 객체를 결합해 반환하는 index 함수 정의
- Templates 폴더 작성 후 템플릿 페이지 작성