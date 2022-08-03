from django.contrib import admin

from bookmarks.models import Bookmark
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id','title','url')

# -> admine page에서 보여줄 수 있도록 한 것.