# Git

## 개요

- 분산 버전 관리 시스템으로 코드의 버전을 관리하기 위한 도구

## 기본 흐름

- git은 파일을 modified, staged, committed로 관리
  - modified : 파일이 수정된 상태
  - stage : (add) 명령어를 통해 수정한 파일이 커밋하기 전 상태
  - committed : (commit) 명령어로 커밋이 된 상태

## 기본 명령어

### init

- `git init` 실행
- 폴더를 git 저장소로 만들어 git로 관리
- 실행시 git 폴더 생성

### add

- `git add` 실행
- working directory상의 변경 내용을 staging area에 추가하기 위해 사용
- untracked, modified 상태의 파일을 staged 상태로 변경

### commit

- `git commit -m '<메세지>'` 실행
- staged 상태의 파일들을 버전으로 기록

### git status

- `git status` 실행
- git 저장소 파일의 상태 확인할 수 있음
- status로 확인할 수 있는 파일 상태
  - tracked : 이전부터 버전으로 관리되고 있는 파일
    - Unmodified : git status에 나타나지 않음
    - Modified : Changes not staged for commit
    - Staged : Changes to be committed
  - Untracked : 버전으로 관리된 적 없는 파일 (새로 만든 경우)

### git log

- `git log` 실행
- 다양한 옵션을 통해 로그를 조회할 수 있음