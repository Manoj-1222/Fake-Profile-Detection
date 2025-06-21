# Fake Profile Detection Using Artificial Neural Networks

This project is a Django-based web application that uses Artificial Neural Networks (ANN) to identify fake profiles, inspired by the paper "Use of Artificial Neural Networks to Identify Fake Profiles".

## Features

- Admin and User login screens
- Admin can generate and view ANN training models and datasets
- User can check account details for authenticity
- Web interface styled with static CSS and images
- Dataset and model management for fake profile detection

## Folder Structure

```
FakeProfile/
    __init__.py
    settings.py
    urls.py
    wsgi.py
Profile/
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    urls.py
    views.py
    dataset/
    migrations/
    static/
    templates/
manage.py
db.sqlite3
```

## Getting Started

### Prerequisites

- Python 3.7+
- Django (install with `pip install django`)
- Other dependencies listed in `reque.txt` (install with `pip install -r reque.txt`)

### Setup

1. Clone this repository or download the source code.
2. Install dependencies:
    ```sh
    pip install -r reque.txt
    ```
3. Run database migrations:
    ```sh
    python manage.py migrate
    ```
4. Start the development server:
    ```sh
    python manage.py runserver
    ```
5. Open your browser and go to `http://127.0.0.1:8000/`

### Usage

- **Admin Login:** Use username `admin` and password `admin` to access admin features.
- **User:** Check account details for authenticity using the user interface.

## Project Files

- [`FakeProfile/settings.py`](FakeProfile/settings.py): Django project settings.
- [`Profile/views.py`](Profile/views.py): Main application views for admin and user.
- [`Profile/templates/`](Profile/templates/): HTML templates for the web interface.
- [`Profile/static/`](Profile/static/): Static files (CSS, images).
- [`Profile/dataset/`](Profile/dataset/): Datasets for training and testing the ANN.

## Reference

- **Base Paper:** See `Base paper` file for the original research paper and methodology.

---

*This project is for educational and research purposes