from fastapi import FastAPI
from enum import Enum
from typing import Optional


class BlogTypes(str, Enum):
    howto = "howto"
    short = "short"
    story = "story"


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/blogs")
async def get_blogs(skip: int = 0, limit: int = 5, type: Optional[BlogTypes] = None):
    return {
        "message": f"This action returns all blogs! Skip: {skip} - Limit: {limit} - Type: {type.value if type is not None else type}"
    }


@app.get("/blogs/{blog_id}")
async def get_blog_by_id(blog_id: int):
    return {"message": f"This action returns #{blog_id} blog!"}


@app.get("/blogs/{blog_id}/comments")
async def get_blog_comments(blog_id: int, username: Optional[str] = None):
    return {
        "message": f"This action returns #{blog_id} blog includes all comments! Username: {username}"
    }


@app.get("/blogs/{blog_id}/comments/{comment_id}")
async def get_blog_comment_by_id(blog_id: int, comment_id: int, valid: bool = True):
    return {
        "message": f"This action returns #{blog_id} blog includes #{comment_id} comment! Valid: {valid}"
    }
