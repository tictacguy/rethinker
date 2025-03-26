from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title', 'content')
    list_filter = ('category',)