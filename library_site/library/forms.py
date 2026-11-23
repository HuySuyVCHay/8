from datetime import date

from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "year", "pages", "description"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }

    def clean_year(self):
        year = self.cleaned_data["year"]
        current_year = date.today().year
        if year > current_year:
            raise forms.ValidationError(
                f"Год издания не может быть больше {current_year}."
            )
        return year

    def clean_pages(self):
        pages = self.cleaned_data["pages"]
        if pages <= 0:
            raise forms.ValidationError("Количество страниц должно быть больше нуля.")
        return pages
