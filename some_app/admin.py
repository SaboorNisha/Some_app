
from django.contrib import admin
from some_app.models import account_profile,Post
# Register your models here.
admin.site.register(account_profile)
admin.site.register(Post)