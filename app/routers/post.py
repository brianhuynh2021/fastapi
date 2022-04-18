from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from fastapi import APIRouter, Response, status, HTTPException, Depends
from typing import Optional, List

router = APIRouter(prefix="/posts", tags=['Posts'])

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
        {"title": "my favorite food", "content": "it is prawn", "id": 2}]
# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
        
@router.get("", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall
    posts = db.query(models.Post).all()
    return posts


@router.post("/createposts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
    #cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s)
    # returning *""", (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    
    # post_dict = post.dict()
    # post_dict['id'] = randrange(0, 1000000)
    # my_posts.append(post_dict)
    # print(post.dict())

    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/latest")
def get_latest_post(db: Session=Depends(get_db)):
    
    post = my_posts[len(my_posts)-1]
    return {"detail": post}
    
@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
    # post = find_post(id)
    # if not post:
    #     # response.status_code = 404
    #     # return {'message': f'post with id {id} was not found'}
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    # return {"Post detail": post}
    #----------------------------
    post = db.query(models.Post).filter(models.Post.id == id).first()
    print(post)
    if not post:
        # response.status_code = 404
        # return {'message': f'post with id {id} was not found'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # deleting post
    # find the index in the array that has required ID
    # my_posts.pop(index)
    # index = find_index_post(id)
    # if index == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    # my_posts.pop(index)
    # return {"post detail": "post was successfully deleted"}
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    post.delete(synchronize_session=False)
    db.commit()
    print("Delete Successful")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    
@router.put("/posts/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
    # index = find_index_post(id)
    # if index == None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    # post_dict = post.dict()
    # post_dict['id'] = id
    # my_posts[index] = post_dict
    # return {'data': post_dict}
    #---------------------
    # cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id)))
    # post = cursor.fetchone()
    # if not post:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    # return {"post_detail": post}
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()