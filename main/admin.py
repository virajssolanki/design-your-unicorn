from django.contrib import admin

# Register your models here.
from .models import Frame, Uimg, Merged

admin.site.register(Frame)
admin.site.register(Uimg)
admin.site.register(Merged)