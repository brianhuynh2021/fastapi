from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
        {"title": "my favorite food", "content": "it is prawn", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
def root():
    return {"Hello World!"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/createposts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    print(post.dict())
    return {"data": post_dict}

@app.post("/creatposts")
def create_posts(post: Post):
    post_dict = post.dict()

@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}
    
@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    return {"Post detail": post}


