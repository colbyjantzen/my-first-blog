from django.contrib import admin
from .models import Post, Comment, Temperature, DailyLog

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Temperature)
admin.site.register(DailyLog)