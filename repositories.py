from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from models import BookModel
from typing import List

# Your MongoDB connection string
MONGO_DETAILS = "mongodb+srv://knowledgetekhub:bBGTHGWYwvsO5ot3@bookdb.2twhiug.mongodb.net/?retryWrites=true&w=majority&appName=bookdb"

# Initialize the MongoDB client
client = AsyncIOMotorClient(MONGO_DETAILS)

# Define the database and collection you want to use
database = client.bookdb
books_collection = database.get_collection("books")


async def fetch_all_books() -> List[BookModel]:
    books = []
    cursor = books_collection.find({})
    async for document in cursor:
        books.append(BookModel(**document))
    return books


async def find_book_by_title(title: str) -> dict:
    return await books_collection.find_one({"title": title})


async def fetch_book_by_id(book_id: str) -> BookModel:
    document = await books_collection.find_one({"_id": ObjectId(book_id)})
    if document:
        return BookModel(**document)


async def add_book(book_data: dict) -> str:
    result = await books_collection.insert_one(book_data)
    return str(result.inserted_id)


async def add_multiple_books(books: List[BookModel]) -> List[str]:
    documents = [book.dict(by_alias=True) for book in books]
    result = await books_collection.insert_many(documents)
    return [str(id) for id in result.inserted_ids]


async def update_book_summary(book_id: str, summary: str) -> BookModel:
    result = await books_collection.update_one(
        {"_id": ObjectId(book_id)}, {"$set": {"summary": summary}}
    )
    if result.matched_count:
        return await fetch_book_by_id(book_id)


async def update_book(book_id: str, book_data: dict) -> bool:
    try:
        result = await books_collection.update_one(
            {"_id": ObjectId(book_id)}, {"$set": book_data}
        )
        return result.modified_count > 0
    except Exception as e:
        print(f"An error occurred while updating the book: {e}")
        return False


async def insert_sample_books(self, sample_books: List[dict]) -> None:
    try:
        await self.books_collection.insert_many(sample_books)
        print("Sample books inserted successfully.")
    except Exception as e:
        print(f"An error occurred while inserting sample books: {e}")
