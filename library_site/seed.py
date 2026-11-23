import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth.models import User
from library.models import Book

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@library.uz", "admin12345")

if not Book.objects.exists():
    Book.objects.create(title="Евгений Онегин", author="Пушкин", year=1833, pages=320,
                        description="Роман в стихах о жизни молодого дворянина.")
    Book.objects.create(title="Война и мир", author="Толстой", year=1869, pages=1300,
                        description="Роман-эпопея об эпохе войн против Наполеона.")
    Book.objects.create(title="Мастер и Маргарита", author="Булгаков", year=1967, pages=480,
                        description="Роман о визите дьявола в Москву 1930-х годов.")
    Book.objects.create(title="Маленький принц", author="Экзюпери", year=1943, pages=96)
