from django.contrib import admin

from reader.models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display =  [field.name for field in Book._meta.fields]

  