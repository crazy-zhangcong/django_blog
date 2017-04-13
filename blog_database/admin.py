from django.contrib import admin

# Register your models here.

from blog_database import models

admin.site.register(models.UserProfile)
admin.site.register(models.Role)
admin.site.register(models.Articles)
admin.site.register(models.Columns)
admin.site.register(models.Tags)
