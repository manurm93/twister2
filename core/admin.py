from django.contrib import admin
from .models import Profile, Post, LikePost, FollowersCount

# Registramos los modelos importados en el panel de administración
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
