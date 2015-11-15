from django.contrib import admin

from . import models

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = models.Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question text',     {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')

admin.site.register(models.Question, QuestionAdmin)
#admin.site.register(models.Choice)

admin.AdminSite.site_header = 'Django test adminka'
