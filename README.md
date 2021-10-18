# [[위코드 x 원티드] 백엔드 프리온보딩 선발 과제](https://www.notion.so/x-2f1edca34653419d8e109df1816197c2)

- Django RestFramework, sqlite3
# 실행방법
- 실행 steps.(manage.py가 있는 디렉토리에서)  
- 1.`$ python3 -m venv venv`
- 2.`$ source venv/bin/activate`
- 3.`$ pip install -r requirements.txt`
- 4.`$ python manage.py migrate`
- 5.`$ python manage.py runserver`   
- 6.`curl을 사용하여 각 api를 호출하는 예시는 아래 api명세 확인`

# APIs

## User
> [POST users/] 회원가입  
> [POST users/login/] 로그인  
> [POST users/logout/] 로그아웃

***

### 회원가입   
* 호출 예시   
`curl -X POST 'http://127.0.0.1:8000/users/' -d '{"username":"user1", "password":"1111"}' -H "Content-Type: application/json"`   
* URL   
`users/`   
* Method:   
`POST`   
* URL Params   
`None`   
* Data Params.  
`username, password`               
* Response:   
   ```
   {
       "id": Int / User id,   
       "username": String / User username,   
       "token": String / Token key  
   } 
  ```      
***

***

### 로그인  
* 호출 예시   
`curl -X POST 'http://127.0.0.1:8000/users/login/' -d '{"username":"user1", "password":"1111"}' -H "Content-Type:application/json"`   
* URL   
`users/login/`   
* Method:   
`POST`   
* URL Params   
`None`   
* Data Params.  
`username, password`               
* Response:   
   ```
   {
       "id": Int / User id,   
       "username": String / User username,   
       "token": String / Token key  
   } 
  ```      
***

***
### 로그아웃    
   
* URL   
`users/logout/`   
* Method:   
`POST`   
* URL Params   
`None`   
* Data Params.  
`None`               
* Response:   
   ```
   
  ```      
***

## Post
> [POST posts/] 게시글 작성  
> [GET posts/] 게시글 리스트 조회  
> [GET posts/{post_id}/] 게시글 조회
> [PATCH posts/{post_id}] 게시글 수정
> [DELETE posts/{post_id}] 게시글 삭제

***

### 게시글 작성   
* 호출 예시   
`curl -X POST 'http://127.0.0.1:8000/posts/' -d '{"title":"title1", "content":"content1"}' -H "Content-Type:application/json" -H "Authorization:Token {token}"`   
* URL   
`posts/`   
* Method:   
`POST`   
* URL Params   
`None`   
* Data Params.  
`title, content`               
* Response:   
   ```
   {
      "id": Int / Post id,
      "title": String / Post title,
      "author": Int / User id,
      "content": String / Post content  
   } 
  ```      
***

***

### 게시글 리스트 조회  
* 호출 예시   
`curl -L -X GET 'http://127.0.0.1:8000/posts?limit=2&offset=0' -H "Authorization:Token {token}" -H "Content-Type:application/json"`   
* URL   
`posts/`   
* Method:   
`GET`   
* URL Params   
`limit, offset`   
* Data Params.  
`None`               
* Response:   
   ```
    {
        "count": 13,
        "next": "http://127.0.0.1:8000/posts/?limit=10&offset=10",
        "previous": null,
        "results": [
            {
                "id": 2,
                "title": "제목2",
                "author": 2,
                "content": "내용2"
            },
            ...
        ]
    } 
  ```      
***

***
### 게시글 조회    
   
* URL   
`posts/{post_id}/`   
* Method:   
`GET`   
* URL Params   
`None`   
* Data Params.  
`None`               
* Response:   
   ```
   {
      "id": 3,
      "title": "제목3",
      "author": 2,
      "content": "내용3"
   }
  ```      
***

***
### 게시글 수정    
   
* URL   
`posts/{post_id}/`   
* Method:   
`PATCH`   
* URL Params   
`None`   
* Data Params.  
`title or content or both`               
* Response:   
   ```
   {
      "id": 3,
      "title": "제목3",
      "author": 2,
      "content": "내용3"
   }
  ```      
***

***
### 게시글 삭제    
   
* URL   
`posts/{post_id}/`   
* Method:   
`DELETE`   
* URL Params   
`None`   
* Data Params.  
`None`               
* Response:   
   ```
   {post deleted}
  ```      
***
