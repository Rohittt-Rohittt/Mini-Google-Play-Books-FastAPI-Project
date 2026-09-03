from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

app = FastAPI(title="Book Management System")


# =========================================================
# BOOK DATA
# This is our temporary "database"
# No actual database is used.
# =========================================================

books = [
    {
        "id": 1,
        "title": "Python Basics",
        "author": "Real P.",
        "pages": 635
    },
    {
        "id": 2,
        "title": "Breaking the Rules",
        "author": "Stephen G.",
        "pages": 99
    }
]


# =========================================================
# BOOK MODEL
# =========================================================

class Book(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    pages: int = Field(gt=0)


# =========================================================
# UI
# =========================================================

@app.get("/", response_class=HTMLResponse)
def home():

    return """
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Book Management System</title>

    <style>

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        body {
            background: #f4f6f8;
            color: #222;
        }

        /* HEADER */

        header {
            background: #1f2937;
            color: white;
            padding: 22px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        header h1 {
            font-size: 26px;
        }

        header span {
            font-size: 14px;
            opacity: 0.8;
        }


        /* MAIN */

        .container {
            width: 84%;
            margin: 30px auto;
        }


        /* STAT CARDS */

        .stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-bottom: 30px;
        }

        .stat-card {
            background: white;
            padding: 22px;
            border-radius: 12px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.08);
        }

        .stat-card h3 {
            color: #6b7280;
            font-size: 14px;
            margin-bottom: 10px;
        }

        .stat-card p {
            font-size: 28px;
            font-weight: bold;
        }


        /* ADD BOOK */

        .form-box {
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.08);
            margin-bottom: 30px;
        }

        .form-box h2 {
            margin-bottom: 20px;
        }

        .form {
            display: grid;
            grid-template-columns: 1fr 1fr 150px 120px;
            gap: 12px;
        }

        input {
            padding: 12px;
            border: 1px solid #d1d5db;
            border-radius: 7px;
            font-size: 14px;
            outline: none;
        }

        input:focus {
            border-color: #2563eb;
        }

        button {
            border: none;
            border-radius: 7px;
            padding: 12px;
            cursor: pointer;
            font-weight: bold;
        }

        .add-btn {
            background: #2563eb;
            color: white;
        }

        .add-btn:hover {
            background: #1d4ed8;
        }


        /* BOOK LIST */

        .books-box {
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.08);
        }

        .books-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }

        .search {
            width: 280px;
        }


        /* TABLE */

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th {
            background: #f3f4f6;
            text-align: left;
            padding: 14px;
            font-size: 14px;
        }

        td {
            padding: 14px;
            border-bottom: 1px solid #e5e7eb;
        }

        tr:hover {
            background: #f9fafb;
        }


        /* BUTTONS */

        .edit-btn {
            background: #f59e0b;
            color: white;
            margin-right: 5px;
        }

        .delete-btn {
            background: #ef4444;
            color: white;
        }

        .edit-btn:hover {
            background: #d97706;
        }

        .delete-btn:hover {
            background: #dc2626;
        }


        /* EMPTY */

        .empty {
            text-align: center;
            padding: 40px;
            color: #6b7280;
        }


        /* RESPONSIVE */

        @media (max-width: 900px) {

            .form {
                grid-template-columns: 1fr 1fr;
            }

            .stats {
                grid-template-columns: 1fr;
            }

        }

        @media (max-width: 600px) {

            .container {
                width: 94%;
            }

            .form {
                grid-template-columns: 1fr;
            }

            .books-header {
                flex-direction: column;
                gap: 15px;
                align-items: stretch;
            }

            .search {
                width: 100%;
            }

            table {
                font-size: 13px;
            }

        }

    </style>

</head>


<body>


<!-- HEADER -->

<header>

    <h1>📚 Book Management System</h1>

    <span>FastAPI + Python</span>

</header>



<div class="container">


    <!-- STATISTICS -->

    <div class="stats">

        <div class="stat-card">

            <h3>Total Books</h3>

            <p id="totalBooks">0</p>

        </div>


        <div class="stat-card">

            <h3>Total Pages</h3>

            <p id="totalPages">0</p>

        </div>


        <div class="stat-card">

            <h3>System</h3>

            <p>Online</p>

        </div>

    </div>



    <!-- ADD BOOK -->

    <div class="form-box">

        <h2>➕ Add New Book</h2>

        <div class="form">

            <input
                type="text"
                id="title"
                placeholder="Book title"
            >

            <input
                type="text"
                id="author"
                placeholder="Author name"
            >

            <input
                type="number"
                id="pages"
                placeholder="Pages"
            >

            <button
                class="add-btn"
                onclick="addBook()"
            >
                Add Book
            </button>

        </div>

    </div>



    <!-- BOOK LIST -->

    <div class="books-box">

        <div class="books-header">

            <h2>📖 All Books</h2>

            <input
                class="search"
                type="text"
                id="search"
                placeholder="🔍 Search book..."
                onkeyup="searchBooks()"
            >

        </div>


        <table>

            <thead>

                <tr>

                    <th>ID</th>

                    <th>Title</th>

                    <th>Author</th>

                    <th>Pages</th>

                    <th>Action</th>

                </tr>

            </thead>


            <tbody id="bookTable">

            </tbody>

        </table>

    </div>


</div>



<script>


// =========================================================
// LOAD BOOKS
// =========================================================

async function loadBooks() {

    const response = await fetch("/books");

    const data = await response.json();

    displayBooks(data.books);

}



// =========================================================
// DISPLAY BOOKS
// =========================================================

function displayBooks(books) {

    const table = document.getElementById("bookTable");

    table.innerHTML = "";

    let totalPages = 0;


    if (books.length === 0) {

        table.innerHTML = `
            <tr>
                <td colspan="5" class="empty">
                    No books found 📚
                </td>
            </tr>
        `;

    }


    books.forEach(book => {

        totalPages += book.pages;


        table.innerHTML += `

            <tr>

                <td>${book.id}</td>

                <td><strong>${book.title}</strong></td>

                <td>${book.author}</td>

                <td>${book.pages}</td>

                <td>

                    <button
                        class="edit-btn"
                        onclick="editBook(
                            ${book.id},
                            '${book.title.replace(/'/g, "\\'")}',
                            '${book.author.replace(/'/g, "\\'")}',
                            ${book.pages}
                        )"
                    >
                        Edit
                    </button>


                    <button
                        class="delete-btn"
                        onclick="deleteBook(${book.id})"
                    >
                        Delete
                    </button>

                </td>

            </tr>

        `;

    });


    document.getElementById("totalBooks").innerText = books.length;

    document.getElementById("totalPages").innerText = totalPages;

}



// =========================================================
// ADD BOOK
// =========================================================

async function addBook() {

    const title = document.getElementById("title").value.trim();

    const author = document.getElementById("author").value.trim();

    const pages = document.getElementById("pages").value;


    if (!title || !author || !pages) {

        alert("Please fill all fields.");

        return;

    }


    const response = await fetch("/books", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            title: title,

            author: author,

            pages: Number(pages)

        })

    });


    if (response.ok) {

        document.getElementById("title").value = "";

        document.getElementById("author").value = "";

        document.getElementById("pages").value = "";

        loadBooks();

    }

    else {

        const error = await response.json();

        alert(error.detail || "Error adding book");

    }

}



// =========================================================
// DELETE BOOK
// =========================================================

async function deleteBook(id) {

    const confirmDelete =
        confirm("Are you sure you want to delete this book?");


    if (!confirmDelete) {
        return;
    }


    const response = await fetch(`/books/${id}`, {

        method: "DELETE"

    });


    if (response.ok) {

        loadBooks();

    }

    else {

        alert("Book not found.");

    }

}



// =========================================================
// EDIT BOOK
// =========================================================

async function editBook(id, oldTitle, oldAuthor, oldPages) {

    const title =
        prompt("Enter book title:", oldTitle);


    if (title === null) {
        return;
    }


    const author =
        prompt("Enter author name:", oldAuthor);


    if (author === null) {
        return;
    }


    const pages =
        prompt("Enter number of pages:", oldPages);


    if (pages === null) {
        return;
    }


    const response = await fetch(`/books/${id}`, {

        method: "PUT",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            title: title,

            author: author,

            pages: Number(pages)

        })

    });


    if (response.ok) {

        loadBooks();

    }

    else {

        alert("Error updating book.");

    }

}



// =========================================================
// SEARCH BOOKS
// =========================================================

async function searchBooks() {

    const search =
        document.getElementById("search").value.toLowerCase();


    const response = await fetch("/books");

    const data = await response.json();


    const filtered =
        data.books.filter(book =>

            book.title.toLowerCase().includes(search) ||

            book.author.toLowerCase().includes(search)

        );


    displayBooks(filtered);

}



// =========================================================
// LOAD WHEN PAGE OPENS
// =========================================================

loadBooks();


</script>


</body>

</html>
"""


# =========================================================
# GET ALL BOOKS
# =========================================================

@app.get("/books")
def get_books(limit: int | None = None):

    if limit is not None:

        if limit <= 0:
            raise HTTPException(
                status_code=400,
                detail="Limit must be greater than 0"
            )

        return {
            "books": books[:limit]
        }

    return {
        "books": books
    }


# =========================================================
# GET BOOK BY ID
# =========================================================

@app.get("/books/{book_id}")
def get_book(book_id: int):

    for book in books:

        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )


# =========================================================
# CREATE BOOK
# =========================================================

@app.post("/books")
def create_book(book: Book):

    new_id = max(
        [b["id"] for b in books],
        default=0
    ) + 1


    new_book = {

        "id": new_id,

        "title": book.title,

        "author": book.author,

        "pages": book.pages

    }


    books.append(new_book)


    return {

        "message": "Book added successfully",

        "book": new_book

    }


# =========================================================
# UPDATE BOOK
# =========================================================

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):

    for book in books:

        if book["id"] == book_id:

            book["title"] = updated_book.title

            book["author"] = updated_book.author

            book["pages"] = updated_book.pages


            return {

                "message": "Book updated successfully",

                "book": book

            }


    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )


# =========================================================
# DELETE BOOK
# =========================================================

@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    for book in books:

        if book["id"] == book_id:

            books.remove(book)


            return {

                "message": "Book deleted successfully"

            }


    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )