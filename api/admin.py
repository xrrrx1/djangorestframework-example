from django.contrib import admin

from api.models import Bucketlist, Comment


@admin.register(Bucketlist)
class BucketlistAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
