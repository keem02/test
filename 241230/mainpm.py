from fastapi import FastAPI

app = FastAPI()

blog_data = [
    {"title": "Blog Title 1", "content": "Content 1", "author": "Author 1"},
    {"title": "Blog Title 2", "content": "Content 2", "author": "Author 1"},
    {"title": "Blog Title 3", "content": "Content 3", "author": "Author 2"},
    {"title": "Blog Title 4", "content": "Content 4", "author": "Author 2"},
    {"title": "Blog Title 5", "content": "Content 5", "author": "Author 3"},
    {"title": "Blog Title 6", "content": "Content 6", "author": "Author 3"},
]


@app.get("/gettest")
def read_root():
    return {"Hello": "GET"}


@app.post("/posttest")
def read_root():
    return {"Hello": "POST"}
[1:05 PM]
## 블로그 URL 설계

URL        | Method | 설명
-----------|--------|----------------------
/blog      | GET    | 블로그 목록을 가져온다.
/blog/{id} | GET    | 블로그 상세 정보를 가져온다.
/blog      | POST   | 블로그를 생성한다.
/blog/{id} | PUT    | 블로그를 수정한다.
/blog/{id} | DELETE | 블로그를 삭제한다.


from fastapi import FastAPI

app = FastAPI()

blog_data = [
    {"id": 1, "title": "Blog Title 1", "content": "Content 1", "author": "Author 1"},
    {"id": 2, "title": "Blog Title 2", "content": "Content 2", "author": "Author 1"},
    {"id": 3, "title": "Blog Title 3", "content": "Content 3", "author": "Author 2"},
    {"id": 4, "title": "Blog Title 4", "content": "Content 4", "author": "Author 2"},
    {"id": 5, "title": "Blog Title 5", "content": "Content 5", "author": "Author 3"},
    {"id": 6, "title": "Blog Title 6", "content": "Content 6", "author": "Author 3"},
]


@app.get("/gettest")
def read_root():
    return {"Hello": "GET"}


@app.post("/posttest")
def read_root():
    return {"Hello": "POST"}


@app.get("/blog")
def get_blogs():
    return blog_data

@app.get("blog/{id}")
def get_blog(id)
    for blog["id"]