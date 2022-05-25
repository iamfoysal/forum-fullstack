from django.contrib import admin

from .models import BlogModel, Category, Profile


class CatagoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# class ProfileAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('user',)}

admin.site.register(BlogModel, PostAdmin)
admin.site.register(Category,CatagoryAdmin)
admin.site.register(Profile)

