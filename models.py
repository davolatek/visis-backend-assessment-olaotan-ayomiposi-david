from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId


class BookModel(BaseModel):

    title: str
    author: str
    published_date: datetime
    text: str
    genre: str
    publisher: str
    publication_date: datetime
    isbn: str
    page_count: int
    language: str

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class ResponseModel(BaseModel):
    response_code: int
    response_message: str


class UpdateBookModel(BaseModel):
    title: str
    author: str
    published_date: datetime
    text: str
    genre: str
    publisher: str
    publication_date: datetime
    isbn: str
    page_count: int
    language: str


class BookSummaryResponse(BaseModel):
    book_id: str
    title: str
    author: str
    published_date: Optional[str] = None
    text: Optional[str] = None
    genre: Optional[str] = None
    publisher: Optional[str] = None
    publication_date: Optional[str] = None
    isbn: Optional[str] = None
    page_count: Optional[int] = None
    language: Optional[str] = None
    summary: str
