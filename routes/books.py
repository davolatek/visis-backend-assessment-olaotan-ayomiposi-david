from fastapi import APIRouter, HTTPException
from typing import List
from ai_module import generate_summary_from_text
from models import BookModel, ResponseModel, UpdateBookModel
from repositories import (
    fetch_all_books,
    fetch_book_by_id,
    add_book,
    find_book_by_title,
    update_book,
)

router = APIRouter()


@router.get("/books/", response_model=List[BookModel])
async def get_books():
    return await fetch_all_books()


@router.get("/books/{book_id}", response_model=BookModel)
async def get_book(book_id: str):
    book = await fetch_book_by_id(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/books/", response_model=ResponseModel)
async def create_book(book: BookModel):
    existing_book = await find_book_by_title(book.title)
    if existing_book:
        return ResponseModel(
            response_code=400, response_message="A book with this title already exists."
        )

    book_id = await add_book(book.dict(exclude_unset=True))
    if not book_id:
        return ResponseModel(
            response_code=500,
            response_message="An error occurred while adding the book.",
        )

    return ResponseModel(
        response_code=201, response_message="Book created successfully."
    )


@router.post("/books/{book_id}/summarize", response_model=ResponseModel)
async def summarize_book(book_id: str):
    book = await fetch_book_by_id(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    if not book.text:
        raise HTTPException(
            status_code=400, detail="No text available for summarization"
        )

    # Generate summary using the book's full text
    summary = generate_summary_from_text(book.text)

    print(f"summary generated::: {summary}")

    # Convert datetime fields to strings
    # published_date = (
    #     book.published_date.strftime("%Y-%m-%d") if book.published_date else None
    # )
    # publication_date = (
    #     book.publication_date.strftime("%Y-%m-%d") if book.publication_date else None
    # )

    return ResponseModel(response_code=200, response_message=summary)


@router.put("/books/{book_id}", response_model=ResponseModel)
async def update_book_details(book_id: str, book: UpdateBookModel):
    # Fetch the existing book from the database
    existing_book = await fetch_book_by_id(book_id)
    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")

    # Update the book in the database
    updated = await update_book(book_id, book.dict())
    if not updated:
        raise HTTPException(status_code=500, detail="Failed to update book")

    return ResponseModel(
        response_code=200, response_message="Book updated successfully"
    )
