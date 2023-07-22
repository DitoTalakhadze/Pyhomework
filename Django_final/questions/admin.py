from django.contrib import admin
from .models import Question, Tag, Comment, Answer

# Register your models here.

admin.site.register(Question)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Answer)
