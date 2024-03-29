from django.contrib import admin

from .models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Book)

# Define admin class using decorator syntax (does same as defining
# admin class below for author
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
   

#admin.site.register(Author)   

# Define an admin class for author:
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
# Register the admin clas with the associated model:
admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)

#admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')


admin.site.register(Language)
