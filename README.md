**✍🏻 Blog Management - REST API**

This project is a robust RESTful API for managing a blog platform, built using the **[FastAPI](https://fastapi.tiangolo.com)** framework. It provides efficient endpoints for creating, reading, updating, and deleting blog posts, user management, authentication, and more.

Designed with modern web development best practices in mind, it leverages FastAPI's high performance, automatic interactive API documentation (via Swagger UI and ReDoc), and type hints for improved developer experience.

# 🛠️ Tools

- [<img src="https://img.shields.io/badge/FastAPI-0.124.2-green?style=plastic&logo=fastapi&logoColor=white" alt="FastAPI badge" width="160">](https://fastapi.tiangolo.com)
- [<img src="https://img.shields.io/badge/Python-3.14.0-green?style=plastic&logo=python&logoColor=white" alt="Python badge" width="160">](https://www.python.org)

# ✨ Key Features

- **CRUD Operations**
- **API Documentation**: Auto-generated docs at `/docs` (Swagger) and `/redoc`.
- **Error Handling**: Comprehensive error responses with HTTP status codes and details.

# ⬇️ Installation

1. Clone the Repository:
   ```bash
   git clone https://github.com/amir-emd/blog-management-fastapi.git
   ```
   ```bash
   cd blog-management-fastapi
   ```
2. Set Up a Virtual Environment:

   ```bash
   python -m venv .venv
   ```

   ```bash
   # On Mac/Linux:
   source .venv/bin/activate

   # On Windows:
   .venv\Scripts\activate
   ```

3. Install Dependencies:

   ```bash
   pip install -r requirements.txt
   ```

# 🚀 Running the Application

1. Start the Server:

   ```bash
   # Development mode:
   fastapi dev main.py

   # Production mode:
   fastapi run main.py
   ```

   The API will be available at http://localhost:8000.

2. Access API Documentation:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc
