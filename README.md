# Django on Vercel

A simple starter template to **deploy a Django project on Vercel** as a **serverless function**.

This app is pre-configured to use **PostgreSQL** as the database. It also includes:

- ✅ Static file support for production
- ✅ Compatibility with PostgreSQL and MySQL

## Requirements

- Python 3.12 or above
- Git
- [uv](https://github.com/astral-sh/uv) (optional, for fast dependency management)

## Getting Started (Local Development)

### 1. Clone the Repository

```bash
mkdir -p ~/Dev/django-vercel
cd ~/Dev/django-vercel
git clone https://github.com/arvind-4/django-on-vercel.git .
```

### 2. Create a Virtual Environment

#### Option A: Using [uv](https://github.com/astral-sh/uv)

```bash
uv venv
uv sync
```

#### Option B: Using `venv` and `pip`

```bash
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

### 3. Set Up Environment Variables

```bash
cp .env.sample .env
```

> Make sure to update `.env` with your actual credentials and settings.

### 4. Run the Server Locally

```bash
python manage.py runserver
```

---

## Notes

- This setup is optimized for deployment on **Vercel** as a serverless backend.
- Ensure your database settings in `.env` are correctly configured before deploying.
