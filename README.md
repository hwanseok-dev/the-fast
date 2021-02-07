# Pivoting!

본 프로젝트는 현재 django+react 기반 백오피스 프로젝트로 변경되고 있습니다.  

![backoffice-0](/assets/images/backoffice-0.jpg)  


# the-fast

django에 익숙해지기 위해 진행한 the fast 프로젝트에 대한 간단한 중간 회고입니다.  

## 프로젝트 소개

본 프로젝트는 3개의 앱을 포함하고 있습니다. fcuser, product, order에 대한 기능을 각 앱을 기준으로 구분하였습니다. 본 프로젝트는 아래와 같은 기능을 가지고 있습니다.  

1. 사용자 관리 : 로그인, 로그아웃, decorator를 통한 @login_required, @admin_required
1. 상품 관리 : 상품 CRUD
1. 주문 관리 : 주문 CRUD
1. DjangoRestFrameWork : 상품과 주문에 대한 정보를 restAPI로 제공

## 개발환경

- window 10
- python 3.6.8
- django 3.1.5
- postgresql 
- djangorestframework  
- venv packages

| Packge              | version  | latest version  |
| ------------------- | ------ | ------ |
| Django              | 3.1.6  | 3.1.6  |
| asgiref             | 3.3.1  | 3.3.1  |
| djangorestframework | 3.12.2 | 3.12.2 |
| pip                 | 21.0.1 | 21.0.1 |
| psycopg2            | 2.8.6  | 2.8.6  |
| pytz                | 2021.1 | 2021.1 |
| setuptools          | 52.0.0 | 53.0.0 |
| sqlparse            | 0.4.1  | 0.4.1  |
| wheel               | 0.36.2 | 0.36.2 |

## 배운 점

간단한 프로젝트였지만 django에 많이 익숙해질 수 있었습니다. 배운 점을 정리해보면 아래와 같습니다.  

1. 클래스 기반 모델을 통한 데이터베이스 생성 및 사용 방법
1. 클래스 기반 모델 수정을 통한 데이터베이스 migration 방법
1. `request.session`을 통한 로그인한 사용자 정보 저장 및 로그아웃
1. django Model, Tempplates, View 구조(`MTV`) 이해
1. django admin에 Model 등록 및 관리 방법
1. auth.hashers `check_password, make_password`를 통한 인증 강화
1. 클래스 기반 Form을 통한 입력 데이터 검증과 객체 생성의 분리`clean(), form_valid()`
1. rest_framework를 통해 객체 정보를 api로 제공하기 위한 `serializer` 등록
1. 객체 정보는 rest API로 제공할 때 `queryset`을 통한 객체 필터링
1. `generic view`를 통한 restAPI 제공의 편의성
1. 클래스 기반 Form 정보를 tempalte으로 전달하기 위한 context_data 수정`get_context_date()`
1. 다수의 FK를 가지는 모델의 객체를 생성하기 위한 transaction.atommic 처리()`transaction.atomic()`  

![the-fast-0](/assets/images/thefast-0.jpg)  

![the-fast-1](/assets/images/thefast-1.jpg)  

![the-fast-2](/assets/images/thefast-2.jpg)  

![the-fast-3](/assets/images/thefast-3.jpg)  

![the-fast-4](/assets/images/thefast-4.jpg)  


## 한 마디

이제 시작이라서, 조금만 비정상적인 요청을 날려도 버그가 뻥뻥 터집니다.  
장고의 가능성을 믿고, django+react 기반 `백오피스`로 추가 개발을 진행하고 있습니다.    

# 개발 세팅

## venv 
1. Create venv name with mysite
   - `python3 -m venv theinsta`
1. `cd insta/bin` or `cd insta/Script`
1. `. activate`

## Install prerequisites

1. python -m pip install --upgrade pip
1. pip install psycopg2
1. pip install djangorestframework django-cors-headers
1. pip install django-rest-swagger

## Create postgreSQL database in instance

1. `CREATE DATABASE theinsta;`
1. `GRANT ALL PRIVILEGES ON DATABASE theinsta To user_id;`
1. Make `dev_settings.py` in root directory
    ```python
    # /dev_settings.py
    SECRET_KEY = '*************************'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': '*********',
            'USER': '*********',
            'PASSWORD': '*******',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    ```

## Launch Project in instance console

1. Activate venv
1. `cd projects/mysite`
1. `python manage.py migrate`
1. Make sure the static IP address is set as [here][2]
1. `python manage.py runserver 0:8000`

# Dev Environment

- window 10 (Ubuntu20.04 also possible)
- python 3.6.8
- django 3.1.5

# Reference

[1]: https://wikidocs.net/75559
[2]: https://github.com/hwanseok-dev/The-PyBo/blob/master/config/settings.py#L24

