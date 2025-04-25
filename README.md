# Djanlog - 커스텀 블로그 플랫폼

Djanlog는 Python 웹 프레임워크인 Django를 기반으로 구축된 개인 맞춤형 블로그 애플리케이션입니다. 사용자는 게시물을 작성, 수정, 삭제하고, 카테고리와 태그를 사용하여 콘텐츠를 분류할 수 있습니다. 또한, 댓글 기능을 통해 독자들과 소통할 수 있습니다.

## 주요 기능

- **게시물 관리 (CRUD):**
  - Markdown 편집기를 이용한 게시물 작성, 조회, 수정, 삭제 기능
  - 게시물 썸네일 이미지 업로드 (미지정 시 기본 이미지 표시)
  - 게시물 내용에 Markdown 문법 적용 및 렌더링
- **콘텐츠 분류:**
  - 카테고리별 게시물 분류 및 조회
  - 태그 기반 게시물 분류 및 조회
- **사용자 인증:**
  - Django 기본 인증 시스템 사용
  - 소셜 로그인 기능 (설정 필요)
  - 관리자/스태프 권한에 따른 게시물 작성/수정 버튼 노출 제어
- **댓글 시스템:**
  - 로그인 사용자의 댓글 작성, 수정, 삭제 기능
  - 사용자 아바타 표시 (소셜 로그인 아바타 포함)
- **파일 첨부:**
  - 게시물에 파일 첨부 및 다운로드 기능
- **페이지:**
  - 독립적인 랜딩 페이지 (`/`)
  - 소개 페이지 (`/about_me/`)
  - 블로그 게시물 목록 페이지 (`/blog/`)
- **기타:**
  - 게시물 목록 페이지네이션
  - 게시물 검색 기능 (구현 중 또는 예정)
  - Bootstrap 기반 반응형 웹 디자인

## 기술 스택

- **백엔드:** Python, Django
- **프론트엔드:** HTML, CSS, JavaScript, Bootstrap
- **데이터베이스:** SQLite (기본) 또는 PostgreSQL/MySQL (설정 가능)
- **라이브러리:**
  - `django-crispy-forms`: 폼 렌더링 개선
  - `django-allauth`: 소셜 로그인 및 인증 강화
  - `Markdown`: Markdown 텍스트 처리
  - (기타 사용된 라이브러리 추가)

## 설치 및 실행 방법

1.  **저장소 복제:**

    ```bash
    git clone <repository-url>
    cd customblog
    ```

2.  **가상 환경 생성 및 활성화:**

    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **필요 라이브러리 설치:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **데이터베이스 마이그레이션:**

    ```bash
    python manage.py migrate
    ```

5.  **관리자 계정 생성:**

    ```bash
    python manage.py createsuperuser
    ```

6.  **개발 서버 실행:**

    ```bash
    python manage.py runserver
    ```

7.  웹 브라우저에서 `http://127.0.0.1:8000/` 로 접속합니다.

## 디렉토리 구조 (주요 부분)

```
customblog/
├── blog/                 # 블로그 앱 (모델, 뷰, 템플릿, URL 등)
│   ├── migrations/
│   ├── static/blog/      # 블로그 앱 정적 파일 (CSS, JS, 이미지)
│   ├── templates/blog/   # 블로그 앱 템플릿 (base, navbar, footer, post_*, 등)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── pages/                # 정적 페이지 앱 (랜딩, 소개 등)
│   ├── static/pages/     # 페이지 앱 정적 파일
│   ├── templates/pages/  # 페이지 앱 템플릿 (landing, about_me 등)
│   └── ...
├── customblog/           # 프로젝트 설정 디렉토리
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── venv/                 # 가상 환경
├── manage.py             # Django 관리 스크립트
├── requirements.txt      # 필요 라이브러리 목록
└── README.md             # 프로젝트 설명 파일
```
