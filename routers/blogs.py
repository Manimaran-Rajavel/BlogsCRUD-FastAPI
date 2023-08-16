from fastapi import APIRouter, Depends, Response, status, HTTPException
import schemas as s, models as md
from sqlalchemy.orm import session
from database import get_db
from typing import List

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

@router.post('', status_code=201)
def create(request: s.Blogs, response: Response,  db: session = Depends(get_db)):
    new_blog = md.Blog_Model(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    if not new_blog:
        response.status_code = status.HTTP_501_NOT_IMPLEMENTED
    return new_blog

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: session = Depends(get_db)):
    blogs = db.query(md.Blog_Model).filter(md.Blog_Model.id == id)
    if not blogs.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blogs with id {id} not found")
    blogs.delete(synchronize_session=False)
    db.commit()
    return "Deleted Content Successfully"

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: s.Blogs, db: session = Depends(get_db)):
    blogs = db.query(md.Blog_Model).filter(md.Blog_Model.id == id)
    if not blogs.first():
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED, detail=f"Blogs with id {id} not found")
    blogs.update(request.model_dump())
    db.commit()
    return "Updated Succesfully"

@router.get('', status_code=status.HTTP_200_OK, response_model=List[s.ShowBlogs])
def get_all(response: Response, db: session = Depends(get_db)):
    blogs = db.query(md.Blog_Model).all()
    if not blogs:
        response.status_code = status.HTTP_404_NOT_FOUND
    return blogs

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=s.ShowBlogs)
def show_needed(id: int, db: session = Depends(get_db)):
    blogs = db.query(md.Blog_Model).filter(md.Blog_Model.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Detail {id} was not Found")
    return blogs