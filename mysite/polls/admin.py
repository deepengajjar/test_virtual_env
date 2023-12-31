from django.contrib import admin

from .models import Question, Choice

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fieldsets  =[(None, {'fields':['question_text']}),
                 ('Date Info', {'fields':['pub_date']})]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
