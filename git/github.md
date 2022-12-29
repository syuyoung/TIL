# Github

## 개요
- 원격 저장소 중 하나이자 세계에서 가장 많이 쓰이는 원격 저장소

# 이용 방법

- New Repository를 통해 새 원격 저장소 생성
- 생성된 url을 `$ git remote origin url` 명령어를 통해 저장소 정보 설정

## 기본 명령어

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

## branch

- 나뭇가지처럼 독립적인 흐름을 관리

### 명령어

  1. 브랜치 생성 : git branch (이름)
  2. 브랜치 이동 : git checkout (이름)
  3. 브랜치 생성 및 이동 : git checkout -b (이름)
  4. 브랜치 목록 : git branch
  5. 브랜치 삭제 : git branch -d (이름)

## merge

- 각 branch에서 작업 후 합치기 위해 merge 명령어 사용
- 동일 파일 수정 시 파일을 확인한 후 수정 후 커밋
- 다른 파일 수정 시 충돌 없이 자동으로 merge commit 생성

## git flow

- git을 활용하여 협업하는 흐름으로 branch를 활용하는 전략

## Fork

- 내 저장소로 복제본을 가져와 로컬에서 작업 후 원격 저장소로 push할 수 있게 되는 것.
- Fork 후 Clone를 통해 본인 저장소에서 작업
- 작업 후 github에서 Pull Requst를 요청