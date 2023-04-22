from django.contrib import admin

# Register your models here.
from .models import Question, Choice


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Info', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    
    #Choices for each question are "inline" via ChoiceInLine class 
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    #determines display format/organization
    list_filter = ['pub_date']
    #adds filter sidebar
    search_fields = ['question_text']
    #creates search bar which uses LIKE query

admin.site.register(Question, QuestionAdmin)


