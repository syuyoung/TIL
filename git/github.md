# Github

## 개요
- 원격 저장소 중 하나이자 세계에서 가장 많이 쓰이는 원격 저장소

# 이용 방법

- New Repository를 통해 새 원격 저장소 생성
- 생성된 url을 `$ git remote origin url` 명령어를 통해 저장소 정보 설정

## 명령어

1. Push

    - 로컬 저장소의 버전을 원격 저장소로 보냄
    - `git push origin master` 로 실행

2. pull

    - 원격 저장소의 버전을 로컬 저장소로 가져옴
    - `git pull origen master` 로 실행

3. clone

   - 원격 저장소를 복제해서 가져옴
   - `git clone url` 로 실행
   - 협업 등을 시작할 때 사용

4. remote

   - `git remote -v` 원격 저장소 정보 확인
   - `git remote rm` 원격 저장소 삭제

## gitignore

- 버전 관리가 필요 없는 파일이나 폴더, 확장자를 관리
- 저장소에 `.gitignore` 파일을 생성 후 작성
- 예시
  - 파일 : a.txt, test/a.txt (test폴더의 파일)
  - 디렉토리 : /test
  - 특정 확장자 : *.exe
  - 예외 처리 : !b.exe
- 프로젝트 시작전 미리 설정하는 것이 중요