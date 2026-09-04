from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

app = FastAPI(title="Book Management System")


# -----------------------------
# In-memory book data
# -----------------------------
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


# -----------------------------
# Pydantic Model
# -----------------------------
class Book(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    pages: int = Field(gt=0)


# -----------------------------
# Home Page
# -----------------------------
@app.get("/", response_class=HTMLResponse)
def home():

    return """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Book Management System</title>

    <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"
    >

    <style>

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, sans-serif;
            background: #f4f6fb;
            color: #1f2937;
        }

        /* HEADER */

        header {
            background: linear-gradient(135deg, #17152f, #312e81, #172554);
            color: white;
            padding: 20px 7%;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .logo-icon {
            width: 48px;
            height: 48px;
            border-radius: 14px;
            background: linear-gradient(135deg, #8b5cf6, #06b6d4);

            display: flex;
            align-items: center;
            justify-content: center;

            font-size: 22px;
        }

        .logo h1 {
            font-size: 24px;
        }

        .logo span {
            font-size: 13px;
            opacity: 0.75;
        }

        .status {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 14px;
        }

        .status-dot {
            width: 9px;
            height: 9px;
            background: #22c55e;
            border-radius: 50%;
        }

        /* MAIN */

        main {
            width: 86%;
            max-width: 1200px;
            margin: 40px auto;
        }

        .hero {
            margin-bottom: 30px;
        }

        .hero h2 {
            font-size: 36px;

            background: linear-gradient(
                90deg,
                #7c3aed,
                #2563eb,
                #0891b2
            );

            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero p {
            margin-top: 8px;
            color: #6b7280;
        }

        /* STATS */

        .stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-bottom: 25px;
        }

        .stat-card {
            background: white;
            padding: 22px;
            border-radius: 18px;

            box-shadow: 0 8px 25px rgba(0,0,0,0.06);

            display: flex;
            align-items: center;
            gap: 16px;
        }

        .stat-icon {
            width: 50px;
            height: 50px;
            border-radius: 14px;

            display: flex;
            align-items: center;
            justify-content: center;

            font-size: 20px;
            background: #ede9fe;
            color: #7c3aed;
        }

        .stat-card h3 {
            font-size: 25px;
        }

        .stat-card p {
            color: #6b7280;
            font-size: 13px;
            margin-top: 4px;
        }

        /* CARD */

        .card {
            background: white;
            border-radius: 20px;
            padding: 28px;
            margin-bottom: 25px;

            box-shadow: 0 8px 30px rgba(0,0,0,0.06);
        }

        .card-title {
            font-size: 21px;
            font-weight: bold;
            margin-bottom: 20px;
        }

        /* FORM */

        .form-grid {
            display: grid;
            grid-template-columns: 1fr 1fr 150px auto;
            gap: 15px;
            align-items: end;
        }

        .input-box label {
            display: block;
            font-size: 13px;
            font-weight: bold;
            margin-bottom: 7px;
        }

        input {
            width: 100%;
            padding: 13px 14px;

            border: 1px solid #d1d5db;
            border-radius: 10px;

            font-size: 14px;
            outline: none;
        }

        input:focus {
            border-color: #7c3aed;
            box-shadow: 0 0 0 3px rgba(124,58,237,0.1);
        }

        .add-btn {
            padding: 13px 20px;

            border: none;
            border-radius: 10px;

            color: white;
            font-weight: bold;
            cursor: pointer;

            background: linear-gradient(
                135deg,
                #7c3aed,
                #2563eb
            );
        }

        .add-btn:hover {
            transform: translateY(-1px);
        }

        /* BOOK HEADER */

        .book-header {
            display: flex;
            justify-content: space-between;
            align-items: center;

            margin-bottom: 20px;
        }

        .book-count {
            color: #7c3aed;
            font-size: 14px;
            font-weight: bold;
        }

        .search-box {
            position: relative;
            width: 280px;
        }

        .search-box i {
            position: absolute;
            left: 13px;
            top: 14px;
            color: #9ca3af;
        }

        .search-box input {
            padding-left: 38px;
        }

        /* TABLE */

        .table-container {
            overflow-x: auto;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th {
            background: #eef2ff;
            color: #4338ca;

            text-align: left;
            padding: 15px;

            font-size: 13px;
        }

        td {
            padding: 16px 15px;
            border-bottom: 1px solid #eef0f5;
            font-size: 14px;
        }

        tr:hover {
            background: #fafaff;
        }

        .id-badge {
            background: #ede9fe;
            color: #7c3aed;

            padding: 6px 10px;
            border-radius: 8px;

            font-weight: bold;
        }

        .book-title {
            font-weight: bold;
        }

        .author {
            color: #64748b;
        }

        .pages {
            font-weight: bold;
            color: #2563eb;
        }

        /* BUTTONS */

        .action-btn {
            width: 36px;
            height: 36px;

            border: none;
            border-radius: 9px;

            cursor: pointer;
            margin-right: 5px;
        }

        .edit-btn {
            background: #fef3c7;
            color: #d97706;
        }

        .delete-btn {
            background: #fee2e2;
            color: #dc2626;
        }

        .action-btn:hover {
            transform: scale(1.08);
        }

        /* EMPTY */

        .empty {
            text-align: center;
            padding: 40px;
            color: #9ca3af;
        }

        /* RESPONSIVE */

        @media(max-width: 850px) {

            .stats {
                grid-template-columns: 1fr;
            }

            .form-grid {
                grid-template-columns: 1fr;
            }

            .book-header {
                flex-direction: column;
                align-items: stretch;
                gap: 15px;
            }

            .search-box {
                width: 100%;
            }

            .hero h2 {
                font-size: 28px;
            }
        }

    </style>
</head>


<body>

<header>

    <div class="logo">

        <div class="logo-icon">
            <i class="fa-solid fa-book-open"></i>
        </div>

        <div>
            <h1>BookFlow</h1>
            <span>Book Management System</span>
        </div>

    </div>

    <div class="status">
        <span class="status-dot"></span>
        System Online
    </div>

</header>


<main>

    <div class="hero">
        <h2>Manage Your Books 📚</h2>
        <p>Add, edit, search and delete books easily.</p>
    </div>


    <!-- STATS -->

    <div class="stats">

        <div class="stat-card">

            <div class="stat-icon">
                <i class="fa-solid fa-book"></i>
            </div>

            <div>
                <h3 id="totalBooks">0</h3>
                <p>Total Books</p>
            </div>

        </div>


        <div class="stat-card">

            <div class="stat-icon">
                <i class="fa-solid fa-file-lines"></i>
            </div>

            <div>
                <h3 id="totalPages">0</h3>
                <p>Total Pages</p>
            </div>

        </div>


        <div class="stat-card">

            <div class="stat-icon">
                <i class="fa-solid fa-server"></i>
            </div>

            <div>
                <h3>Online</h3>
                <p>System Status</p>
            </div>

        </div>

    </div>


    <!-- ADD BOOK -->

    <div class="card">

        <div class="card-title">
            <i class="fa-solid fa-plus"></i>
            Add New Book
        </div>


        <div class="form-grid">

            <div class="input-box">

                <label>Book Title</label>

                <input
                    type="text"
                    id="title"
                    placeholder="Enter book title"
                >

            </div>


            <div class="input-box">

                <label>Author</label>

                <input
                    type="text"
                    id="author"
                    placeholder="Enter author name"
                >

            </div>


            <div class="input-box">

                <label>Pages</label>

                <input
                    type="number"
                    id="pages"
                    placeholder="Pages"
                    min="1"
                >

            </div>


            <button class="add-btn" onclick="addBook()">

                <i class="fa-solid fa-plus"></i>
                Add Book

            </button>

        </div>

    </div>


    <!-- BOOK LIST -->

    <div class="card">

        <div class="book-header">

            <div>

                <div class="card-title">
                    <i class="fa-solid fa-book"></i>
                    Book Collection
                </div>

                <div class="book-count" id="bookCount">
                    0 Books
                </div>

            </div>


            <div class="search-box">

                <i class="fa-solid fa-search"></i>

                <input
                    type="text"
                    id="search"
                    placeholder="Search books..."
                    onkeyup="searchBooks()"
                >

            </div>

        </div>


        <div class="table-container">

            <table>

                <thead>

                    <tr>

                        <th>ID</th>
                        <th>Title</th>
                        <th>Author</th>
                        <th>Pages</th>
                        <th>Actions</th>

                    </tr>

                </thead>


                <tbody id="bookTable"></tbody>

            </table>

        </div>

    </div>

</main>


<script>


// ----------------------------------
// Load Books
// ----------------------------------

async function loadBooks() {

    try {

        const response = await fetch("/books");

        if (!response.ok) {
            throw new Error("Unable to load books");
        }

        const data = await response.json();

        displayBooks(data.books);

    }

    catch (error) {

        console.error(error);

        alert("Error loading books");

    }

}


// ----------------------------------
// Display Books
// ----------------------------------

function displayBooks(bookList) {

    const table = document.getElementById("bookTable");

    table.innerHTML = "";

    let totalPages = 0;


    document.getElementById("totalBooks").innerText =
        bookList.length;

    document.getElementById("bookCount").innerText =
        bookList.length + (bookList.length === 1 ? " Book" : " Books");


    if (bookList.length === 0) {

        table.innerHTML = `
            <tr>
                <td colspan="5" class="empty">
                    <i class="fa-solid fa-book-open"
                       style="font-size:35px;"></i>

                    <br><br>

                    No books found
                </td>
            </tr>
        `;

        document.getElementById("totalPages").innerText = 0;

        return;
    }


    bookList.forEach(book => {

        totalPages += book.pages;


        const row = document.createElement("tr");


        row.innerHTML = `

            <td>
                <span class="id-badge">
                    #${book.id}
                </span>
            </td>

            <td class="book-title">
                ${escapeHTML(book.title)}
            </td>

            <td class="author">
                ${escapeHTML(book.author)}
            </td>

            <td class="pages">
                ${book.pages}
            </td>

            <td>

                <button
                    class="action-btn edit-btn"
                    title="Edit"
                    onclick="editBook(
                        ${book.id},
                        ${JSON.stringify(book.title)},
                        ${JSON.stringify(book.author)},
                        ${book.pages}
                    )"
                >

                    <i class="fa-solid fa-pen"></i>

                </button>


                <button
                    class="action-btn delete-btn"
                    title="Delete"
                    onclick="deleteBook(${book.id})"
                >

                    <i class="fa-solid fa-trash"></i>

                </button>

            </td>

        `;


        table.appendChild(row);

    });


    document.getElementById("totalPages").innerText =
        totalPages;

}


// ----------------------------------
// ADD BOOK
// ----------------------------------

async function addBook() {

    const titleInput = document.getElementById("title");
    const authorInput = document.getElementById("author");
    const pagesInput = document.getElementById("pages");


    const title = titleInput.value.trim();
    const author = authorInput.value.trim();
    const pages = Number(pagesInput.value);


    // Validation

    if (title === "") {

        alert("Please enter book title");
        titleInput.focus();

        return;
    }


    if (author === "") {

        alert("Please enter author name");
        authorInput.focus();

        return;
    }


    if (!Number.isInteger(pages) || pages <= 0) {

        alert("Pages must be greater than 0");
        pagesInput.focus();

        return;
    }


    const bookData = {

        title: title,
        author: author,
        pages: pages

    };


    try {

        const response = await fetch("/books", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(bookData)

        });


        const data = await response.json();


        if (!response.ok) {

            alert(
                data.detail || "Unable to add book"
            );

            return;
        }


        // Clear form

        titleInput.value = "";
        authorInput.value = "";
        pagesInput.value = "";


        // Reload books

        await loadBooks();


        alert("Book added successfully!");

        titleInput.focus();

    }

    catch (error) {

        console.error(error);

        alert(
            "Cannot connect to FastAPI server."
        );

    }

}


// ----------------------------------
// DELETE BOOK
// ----------------------------------

async function deleteBook(id) {

    const confirmDelete = confirm(
        "Are you sure you want to delete this book?"
    );


    if (!confirmDelete) {
        return;
    }


    try {

        const response = await fetch(
            `/books/${id}`,
            {
                method: "DELETE"
            }
        );


        const data = await response.json();


        if (!response.ok) {

            alert(
                data.detail || "Delete failed"
            );

            return;
        }


        await loadBooks();

        alert("Book deleted successfully!");

    }

    catch (error) {

        console.error(error);

        alert("Error deleting book");

    }

}


// ----------------------------------
// EDIT BOOK
// ----------------------------------

async function editBook(
    id,
    oldTitle,
    oldAuthor,
    oldPages
) {

    const title = prompt(
        "Enter book title:",
        oldTitle
    );


    if (title === null) {
        return;
    }


    const author = prompt(
        "Enter author name:",
        oldAuthor
    );


    if (author === null) {
        return;
    }


    const pagesText = prompt(
        "Enter number of pages:",
        oldPages
    );


    if (pagesText === null) {
        return;
    }


    const pages = Number(pagesText);


    if (
        title.trim() === "" ||
        author.trim() === "" ||
        !Number.isInteger(pages) ||
        pages <= 0
    ) {

        alert("Please enter valid book details");

        return;
    }


    try {

        const response = await fetch(
            `/books/${id}`,
            {

                method: "PUT",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({

                    title: title.trim(),
                    author: author.trim(),
                    pages: pages

                })

            }
        );


        const data = await response.json();


        if (!response.ok) {

            alert(
                data.detail || "Update failed"
            );

            return;
        }


        await loadBooks();

        alert("Book updated successfully!");

    }

    catch (error) {

        console.error(error);

        alert("Error updating book");

    }

}


// ----------------------------------
// SEARCH
// ----------------------------------

async function searchBooks() {

    const searchText =
        document
            .getElementById("search")
            .value
            .toLowerCase()
            .trim();


    try {

        const response = await fetch("/books");

        const data = await response.json();

        const filteredBooks =
            data.books.filter(book =>

                book.title
                    .toLowerCase()
                    .includes(searchText)

                ||

                book.author
                    .toLowerCase()
                    .includes(searchText)

            );


        displayBooks(filteredBooks);

    }

    catch (error) {

        console.error(error);

        alert("Search failed");

    }

}


// ----------------------------------
// HTML Safety
// ----------------------------------

function escapeHTML(value) {

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");

}


// ----------------------------------
// Load on page start
// ----------------------------------

loadBooks();


</script>

</body>

</html>
"""


# ----------------------------------
# GET ALL BOOKS
# ----------------------------------

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


# ----------------------------------
# GET ONE BOOK
# ----------------------------------

@app.get("/books/{book_id}")
def get_book(book_id: int):

    for book in books:

        if book["id"] == book_id:
            return book


    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )


# ----------------------------------
# ADD BOOK
# ----------------------------------

@app.post("/books")
def create_book(book: Book):

    if books:

        new_id = max(
            b["id"] for b in books
        ) + 1

    else:

        new_id = 1


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


# ----------------------------------
# UPDATE BOOK
# ----------------------------------

@app.put("/books/{book_id}")
def update_book(
    book_id: int,
    updated_book: Book
):

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


# ----------------------------------
# DELETE BOOK
# ----------------------------------

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
