from django.contrib import admin
from .models import BlogModel, Profile


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# class ProfileAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('user',)}

admin.site.register(BlogModel, PostAdmin)
admin.site.register(Profile)

