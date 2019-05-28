[TOC]

## git basic

> [git](https://git-scm.com/book/ko/v1/Git맞춤-Git-설정하기)
>
> [git bash](https://gitforwindows.org/)

- `Git`은 분산형버전관리시스템(DVCS - Distributed Version Control System)이다.

  소스코드의 버전 관리를 할 수 있고, 이력이 관리된다.

------

### 0. git setting

> 메일주소는 반드시 GitHub 계정과 동일해야하고(다르면 push 후 github에 잔디가 심어지지 않는다.) 유저네임도 맞춰주는 것이 좋다.
>
> `--global` 옵션으로 설정하는 것은 딱 한 번만 하면 된다. 해당 시스템에서 해당 사용자가 사용할 때는 이 정보를 사용한다. (만약 프로젝트마다 다른 이름과 이메일 주소를 사용하고 싶으면 `--global` 옵션을 빼고 명령을 실행한다.)

```
$ git config --global user.name "example"
$ git config --global user.email test@example.com
```

- git 명령어 자동 색칠

```
$ git config --global color.ui true
```

> Mac 에서 한글파일명 깨짐 및 commit 오류 문제 해결
>
> ```
> # mac
> $ git config --global core.precomposeunicode true
> $ git config --global core.quotepath false
> ```

- 설정 확인

```
$ git config --global --list
```

> git 추가 맞춤 설정
>
> - git status 시 한글파일명 깨짐 해결
>
> ```
> # windows
> $ git config --global core.quotepath false
> ```
>
> - windows - mac 간 라인 바꿈(New Line) 문제 방지
>
> ```
> # windows
> $ git config --global core.autocrlf true
> 
> # linux / mac
> $ git config --global core.autocrlf input
> ```

------

### 1. git 사용하기

#### 1.1 git 저장소 설정

```
$ git init
student@DESKTOP MINGW64 ~/Desktop/TIL (master)
```

**주의!! 반드시 작업 디렉토리에서 git을 사용하고 있는지, (master) 표기가 생겼는지 확인 할 것**

#### 1.2 git add

`git add`는 현재 `working directory` 에서 `commit` 할 목록에 담아놓는 것이다.

그리고 그 목록은 `INDEX(staging area)` 라고 한다.

```
$ touch a.txt
$ git add .
```

- `git add a.txt`를 해도 되지만, 우선 `git add .` 을 하자!!
- `.` 은 리눅스 상에서 현재 디렉토리를 뜻한다.

#### 1.3 git commit

`git commit`은 현재 소스코드 상태를 **스냅샷**을 찍는 것과 동일하다.

`staging area`에 담겨 있는 내용을 이력으로 기록한다.

```
$ git status
$ git commit -m "커밋메시지"
```

#### 1.4 git status

git의 현재 상태를 확인한다. **자주자주 입력하면서 확인하는 습관을 만들어 보자!**

```
$ git status
```

#### 1.5 git push

사전에 github 에 저장소(repository)를 만들어 놓는다.

- Github repo 를 처음 생성한 경우

  - github 저장소(원격저장소) `url`를 `origin` 이라는 이름으로 설정한다.

    ```
    $ git remote add origin https://github.com/example/test.git
    ```

  - 원격 저장소로 보낸다.(push)

    > 한번 push 한 이후로는 `git push` 까지만 입력해도 된다.

    ```
    $ git push -u origin master
    ```

- Github repo 를 clone 한 경우

  ```
  $ git clone 주소 (폴더이름)
  # 이 경우 git init, git remote add 명령어를 하지 않아도 이미 설정되어 있다.
  ```

------

### 2. Git & Github 재설정

> 1 과 2 중 택 1

```
# Git 이름, 이메일 재설정
$ git config --global user.name "example"
$ git config --global user.email example@gmail.com
```

1. 명령어로 재설정

   ```
   # GitHub 로그인 정보 초기화
   $ git credential reject
   protocol=https
   host=github.com
   ```

2. 자격 증명 관리자에서 git 관련 정보 삭제 (winsdows)

------

git 학습 사이트

- [git 공식](https://git-scm.com/book/ko/v2)
- [git 입문](https://backlog.com/git-tutorial/kr/intro/intro1_1.html)
- [git 간편안내서](https://rogerdudler.github.io/git-guide/index.ko.html)