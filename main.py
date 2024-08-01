from fastapi import FastAPI
from routes import books

app = FastAPI(
    title="Book Summary API",
    description="An API for managing books and generating summaries",
    version="1.0.0",
    summary="Book Summary API documentation",
)

app.include_router(books.router, prefix="/api")
