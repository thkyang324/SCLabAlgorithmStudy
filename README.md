# SCLabAlgorithmStudy
소프트컴퓨팅 연구실 코딩테스트 대비 알고리즘 스터디

## 📌 스터디 개요
대기업 취업을 목표로 코딩테스트 대비를 위한 알고리즘 스터디입니다. 
백준, 리트코드, 프로그래머스 등 알고리즘 사이트에서 문제를 일주일에 3~4문제 출제하고, 
이를 일자, 문제 유형 등으로 정리하여 관리합니다.

## 📚 스터디 규칙
- **문제 출제**: 매주 3~4개 문제 선정
- **문제 플랫폼**: 백준(BOJ), 리트코드(LeetCode), 프로그래머스(Programmers)
- **풀이 제출**: 각 주차 폴더에 본인의 풀이 코드 업로드
- **코드 리뷰**: 서로의 코드를 리뷰하고 피드백 제공

## 🗂️ 디렉토리 구조
```
SCLabAlgorithmStudy/
├── README.md                    # 메인 README 파일
├── problems/                    # 주차별 문제 폴더
│   ├── 2025-W01/               # 2025년 1주차 문제
│   │   ├── README.md           # 주차별 문제 목록 및 설명
│   │   ├── problem1_이름.py    # 문제 1 풀이
│   │   ├── problem2_이름.py    # 문제 2 풀이
│   │   └── ...
│   ├── 2025-W02/               # 2025년 2주차 문제
│   └── ...
├── templates/                   # 템플릿 파일
│   ├── problem_template.md     # 문제 문서화 템플릿
│   └── week_template.md        # 주차별 README 템플릿
└── PROBLEM_INDEX.md            # 전체 문제 인덱스
```

## 📋 문제 분류 체계

### 문제 유형
- **자료구조**: 배열, 연결리스트, 스택, 큐, 해시, 힙, 트리, 그래프
- **알고리즘**: 정렬, 탐색, 이진탐색, DFS/BFS, 다이나믹 프로그래밍, 그리디, 백트래킹
- **기타**: 문자열, 수학, 구현, 시뮬레이션

### 난이도
- 🟢 **쉬움**: 기본 개념 이해 및 구현
- 🟡 **보통**: 알고리즘 응용 및 최적화
- 🔴 **어려움**: 복잡한 알고리즘 및 고급 기법

## 🚀 시작하기

### 1. 저장소 클론
```bash
git clone https://github.com/thkyang324/SCLabAlgorithmStudy.git
cd SCLabAlgorithmStudy
```

### 2. 주차별 문제 확인
각 주차 폴더의 `README.md`에서 해당 주의 문제 목록과 링크를 확인합니다.

### 3. 문제 풀이
선호하는 언어(Python, Java, C++ 등)로 문제를 해결합니다.

### 4. 풀이 제출
```bash
# 브랜치 생성
git checkout -b week01/your-name

# 파일 추가
git add problems/2025-W01/problem1_yourname.py

# 커밋
git commit -m "Week 01: Add problem 1 solution"

# 푸시
git push origin week01/your-name

# Pull Request 생성
```

## 📝 문제 추가 가이드

### 새로운 주차 추가
1. `problems/` 폴더에 `YYYY-WXX` 형식으로 새 폴더 생성
2. `templates/week_template.md`를 참고하여 주차별 README 작성
3. `PROBLEM_INDEX.md`에 해당 주차 정보 업데이트

### 문제 정보 작성
```markdown
## 문제 1: [문제 제목]
- **플랫폼**: 백준/리트코드/프로그래머스
- **문제 번호**: #1234
- **링크**: [문제 링크](https://...)
- **난이도**: 🟢/🟡/🔴
- **유형**: 자료구조 - 스택
- **설명**: 문제에 대한 간단한 설명
```

## 🤝 기여 방법
1. 이슈를 통해 새로운 문제 제안
2. Pull Request를 통한 풀이 공유
3. 다른 사람의 코드 리뷰 참여
4. 스터디 자료 및 문서 개선

## 📊 진행 상황
전체 문제 진행 상황은 [PROBLEM_INDEX.md](PROBLEM_INDEX.md)에서 확인할 수 있습니다.

## 💡 팁
- 문제를 풀기 전에 시간 복잡도를 먼저 생각해보기
- 여러 풀이 방법을 고민하고 최적화하기
- 다른 사람의 코드를 보며 새로운 접근법 배우기
- 막혔을 때는 힌트를 참고하되, 스스로 해결 시도하기

## 📞 연락처
문의사항이나 제안은 이슈를 통해 공유해주세요!

---
**Happy Coding! 💻✨**
