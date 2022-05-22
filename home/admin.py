from gettext import Catalog
from django.contrib import admin
from .models import BlogModel, Profile, Category

class CatagoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# class ProfileAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('user',)}

admin.site.register(BlogModel, PostAdmin)
admin.site.register(Category,CatagoryAdmin)
admin.site.register(Profile)

