# SCLabAlgorithmStudy
소프트컴퓨팅 연구실 코딩테스트 대비 알고리즘 스터디

## ❗ 어떤 스터디인가요?

저희는 IT기업 입사에 필요한 코딩 테스트를 <span style="color:red">우수한 성적으로 통과</span>하기 위해 학습하고 의견을 나누는 알고리즘 스터디입니다.
1. 코딩 테스트에 자주 나오는 개념에 대한 학습 및 백준 or 프로그래머스의 문제들을 풀면서 익힙니다.
2. 어느정도 코딩 테스트에 필요한 내용들을 학습했다면, 기출문제 위주로 문제풀이를 진행합니다.

## ❗ 어떤 식으로 진행되나요?

1. 1주일에 풀 문제를 선정하여 문제를 푼 뒤, 깃헙에 올립니다.
2. 자신이 푼 문제에 대한 코딩 리뷰를 진행하고 피드백을 진행합니다.
3. 다음 스터디 일자 이전에 레퍼지토리에 코드를 업로드해주셔야 합니다.

## ❗ 어떤 규칙을 지켜야 하나요?

### ✅ 파일 생성 및 업로드 규칙

- Prefix: 백준(BOJ), 프로그래머스(PGMS), 리트코드(LC)

1. 매주 새로운 디렉토리를 만듭니다. ex) 1주차, 2주차..
2. 디렉토리 안에 문제 디렉토리를 만듭니다. ex) 백준 1000번 문제라면 BOJ_1000, 프로그래머스 문제라면 PGMS_문제명
3. 문제 디렉토리 안에 각자 푼 문제를 `BOJ_1000_홍길동`의 형식으로 업로드합니다.
4. 최종적인 경로는 `1주차/BOJ_1000/BOJ_1000_홍길동` 입니다.

### ✅ 깃헙 Push/Pull 규칙

1. 무조건 __pull__ 먼저 해줍니다. pull을 해서 해당 주차의 디렉토리가 생기지 않는다면 따로 만들어주세요

```
$ git pull <remote 이름> <브랜치이름>
$ git pull SCLabAlgorithmStudy master
```

2. 파일 업로드 규칙에 맞게 push해주세요.
```
$ git add .
$ git commit -m "BOJ_1000_홍길동"
$ git push <remote 이름> master
```

3. 만일 push를 하다가 __충돌__ 이 일어났을 경우 아래의 코드를 입력해주세요
```
$ git log --oneline
```
입력 후 내가 push한 커밋 바로 전 커밋 코드를 복사해줍니다. 그리고 다음을 입력해주세요
```
$ git reset --soft [복사한 커밋 코드]
```

4. 만일 내가 올린 코드에 수정/추가 등의 추가 커밋을 push할 경우에 커밋 형식을 다음과 같이 작성해주세요. 수정을 2번째 할 경우에 `fix2`를 붙여주시면 됩니다.

```
git commit -m "BOJ_1000_홍길동_fix"
git commit -m "BOJ_1000_홍길동_add"
```

## 📆 알고리즘 스터디 기록

### 🐱 주차 별 문제

|주차 및 날짜|출제자|문제(문제 번호)|유형|
|:---:|:---:|:---:|:---:|
|1주차(2025-10-15)
|-|태훈|2048 (Easy)([BOJ_12100](https://www.acmicpc.net/problem/12100))|BLIND|
|-|진명|진우의 민트초코우유([BOJ_20208](https://www.acmicpc.net/problem/20208))|BLIND|
|-|민혁|Maximal Rectangle([LC_85](https://leetcode.com/problems/maximal-rectangle/description/))|BLIND|
|2주차(2025-10-22)
|-|태훈||BLIND|
|-|진명||BLIND|
|-|민혁||BLIND|
|-|준영||BLIND|
|3주차(2025-10-29)
|-|태훈||BLIND|
|-|진명||BLIND|
|-|민혁||BLIND|
|-|준영||BLIND|
|4주차(2025-11-05)
|-|태훈||BLIND|
|-|진명||BLIND|
|-|민혁||BLIND|
|-|준영||BLIND|
|5주차(2025-11-12)
|-|태훈||BLIND|
|-|진명||BLIND|
|-|민혁||BLIND|
|-|준영||BLIND|

## 💖 참고사항

### 💕 원격 저장소 등록하기
1. 원하는 디렉토리에 clone해서 다운받습니다. 

```bash
$ git clone https://github.com/thkyang324/SCLabAlgorithmStudy
```

2. `git remote add <원격저장소 이름> <주소>` 형식으로 작성합니다.

```bash
$ git remote add algorithmStudy https://github.com/thkyang324/SCLabAlgorithmStudy
```

### 💕 원격 저장소 조회


`git remote -v`로 등록이 잘 됐는지 확인해봅니다.
```
$ git remote -v
algorithmStudy https://github.com/thkyang324/SCLabAlgorithmStudy (fetch)
algorithmStudy https://github.com/thkyang324/SCLabAlgorithmStudy (push)
