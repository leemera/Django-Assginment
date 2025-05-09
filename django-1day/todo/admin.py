# from django.contrib import admin
# from .models import Todo
#
# @admin.register(Todo)
# class TodoAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'is_completed', 'start_date', 'end_date')
#     list_filter = ('is_completed',)
#     search_fields = ('title',)
#     ordering = ('start_date',)
#     date_hierarchy = 'start_date'  # ← 요게 날짜 필터
#     fieldsets = (
#         ('Todo Info', {
#             'fields': ('title', 'description', 'is_completed')
#         }),
#         ('Date Range', {
#             'fields': ('start_date', 'end_date')
#         }),
#     )
#
# # Register your models here.
