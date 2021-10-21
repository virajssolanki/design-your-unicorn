from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.unregister(Group)

class ChoicesInline(admin.StackedInline):
    model = Choice
    extra = 0
    fields = ["choice", "percentage"]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("campaign", "question",)
    inlines = [ChoicesInline]


class PrintNameInline(admin.StackedInline):
    model = PrintName
    extra = 0

class PrintDesignationInline(admin.StackedInline):
    model = PrintDesignation
    extra = 0

class PrintCommitmentInline(admin.StackedInline):
    model = PrintCommitment
    extra = 0

class PrintImageInline(admin.StackedInline):
    model = PrintImage
    extra = 0

admin.site.register(PrintImage)
admin.site.register(PrintCommitment)
admin.site.register(PrintDesignation)
admin.site.register(PrintName)

class FrameInline(admin.StackedInline):
    model = Frame
    extra = 0

@admin.register(Campaign)
class CampignAdmin(admin.ModelAdmin):
    inlines = [FrameInline]

admin.site.register(HomePage)