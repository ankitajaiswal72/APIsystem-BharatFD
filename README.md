# APIsystem-BharatFD
# FAQ API

A Django-based REST API for managing FAQs with multilingual support, caching, and WYSIWYG editor integration.

## 🚀 Features
- Create, read, update, and delete FAQs.
- Supports multilingual translations (e.g., English, Hindi, Bengali).
- WYSIWYG editor (`django-ckeditor`) for rich text answers.
- API supports language selection via query parameters.
- Caching using Redis for improved performance.
- Docker support for easy deployment.
- Unit tests included.

---

## 🛠 Installation

### 1️⃣ Prerequisites
Ensure you have the following installed:
- Python 3.10+
- Docker & Docker Compose
- Redis (if running without Docker)

### 2️⃣ Clone the Repository
```sh
 git clone https://github.com/your-username/faq-api.git
 cd faq-api
```

### 3️⃣ Set Up a Virtual Environment
```sh
 python -m venv venv
 source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 4️⃣ Install Dependencies
```sh
 pip install -r requirements.txt
```

### 5️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and define the following:
```env
DEBUG=True
SECRET_KEY=your-secret-key
REDIS_URL=redis://127.0.0.1:6379/1  # Change if using Docker
```

### 6️⃣ Apply Migrations & Create Superuser
```sh
 python manage.py migrate
 python manage.py createsuperuser
```

### 7️⃣ Run the Server
```sh
 python manage.py runserver
```
The API will be available at `http://127.0.0.1:8000/api/faqs/`

---

## 🚢 Running with Docker

### 1️⃣ Build & Start Containers
```sh
 docker-compose up --build -d
```

### 2️⃣ Check Running Containers
```sh
 docker ps
```

Now, access the API at `http://127.0.0.1:8000/api/faqs/`

---

## 📌 API Endpoints

### 🔹 Get All FAQs (Default: English)
```sh
 GET /api/faqs/
```
**Example Response:**
```json
[
  {
    "question": "How does caching work?",
    "answer": "Caching stores data in memory."
  }
]
```

### 🔹 Get FAQs in Hindi
```sh
 GET /api/faqs/?lang=hi
```

### 🔹 Create an FAQ (Admin only)
```sh
 POST /api/faqs/
 Content-Type: application/json
```
**Example Body:**
```json
{
  "question": "How to reset password?",
  "answer": "Go to settings and click reset password."
}
```

### 🔹 Update an FAQ (Admin only)
```sh
 PUT /api/faqs/{id}/
```

### 🔹 Delete an FAQ (Admin only)
```sh
 DELETE /api/faqs/{id}/
```

---

## ✅ Running Tests
```sh
pytest
```

---

## 🤝 Contribution Guidelines
1. **Fork** the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Commit your changes: `git commit -m "feat: Added new translation support"`.
4. Push to your branch: `git push origin feature-branch`.
5. Submit a **Pull Request**.


