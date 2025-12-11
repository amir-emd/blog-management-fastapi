from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/blogs")
async def get_blogs():
    return {"message": "This action returns all blogs!"}


@app.get("/blogs/{blog_id}")
async def get_blog_by_id(blog_id: int):
    return {"message": f"This action returns #{blog_id} blog!"}
