from django.contrib import admin
from .models import Board
# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'content', 'created_at', 'updated_at',]

admin.site.register(Board, BoardAdmin)
