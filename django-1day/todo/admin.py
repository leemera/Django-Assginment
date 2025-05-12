from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'description', 'is_completed', 'start_date', 'end_date')
    list_filter = ('is_completed',)
    search_fields = ('title',)
    ordering = ('start_date',)
    list_display_links = ('title',)
    fieldsets = (
        ('Todo Info', {
            'fields': ('user', 'title', 'description', 'completed_image', 'is_completed')
        }),
        ('Date Range', {
            'fields': ('start_date', 'end_date')
        }),
    )
    inlines = [CommentInline]

    class CommentAdmin(admin.ModelAdmin):
        list_display = ('id', 'todo', 'user', 'message', 'created_at')
        list_filter = ('todo', 'user')
        search_fields = ('message', 'user')
        ordering = ('-created_at',)
        list_display_links = ('message',)
        fieldsets = (
            ('Comment Info', {
                'fields': ('todo', 'user', 'message')
            }),
        )




