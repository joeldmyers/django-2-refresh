from django.contrib import admin

# Register your models here.

from .models import Question, Choice


admin.site.site_header = "Joel's Polling Admin"
admin.site.site_title = "Joel's Polling Admin Area"
admin.site.index_title = "Welcome to the Polling admin area"

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)