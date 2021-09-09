from django.contrib import admin

# Register your models here.
from .models import Frame, Uimg, Merged, Campaign, Question, Choice

class ChoicesInline(admin.StackedInline):
    model = Choice
    extra = 0
    fields = ["choice", "percentage"]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("campaign", "question",)
    inlines = [ChoicesInline]

class FrameInline(admin.StackedInline):
    model = Frame
    extra = 0

@admin.register(Campaign)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [FrameInline]