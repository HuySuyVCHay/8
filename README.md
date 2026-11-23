# ДЗ 50 — Шаблоны и формы в Django

Мини-библиотека на Django.

## Запуск

```bash
cd library_site
pip install django
python manage.py migrate
python seed.py
python manage.py runserver
```

http://127.0.0.1:8000/books/

## Страницы

- `/books/` — список книг
- `/books/<id>/` — страница книги
- `/books/new/` — добавить книгу
- `/books/<id>/edit/` — изменить книгу
